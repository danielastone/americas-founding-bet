"""Validate the C001 reference graph without granting historical admission."""
import csv
import datetime
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate(graph, root=ROOT):
    errors = []

    def check(ok, message):
        if not ok:
            errors.append(message)

    def indexed(rows, key):
        result = {}
        for row in rows:
            ident = row.get(key)
            check(bool(ident) and ident not in result, f'invalid/duplicate {key}: {ident}')
            result[ident] = row
        return result

    def table(path, key):
        with (root / path).open(newline='') as handle:
            return indexed(list(csv.DictReader(handle)), key)

    def required(row, fields):
        for field in fields:
            check(bool(row.get(field)), f'missing {field}: {row}')

    def date(value):
        try:
            datetime.date.fromisoformat(value)
            return True
        except (ValueError, TypeError):
            return False

    check(graph.get('schema_version') == '1.0', 'unsupported schema version')
    names = {'tests': 'test_id', 'sources': 'source_id', 'extracts': 'extract_id',
             'links': 'link_id', 'tasks': 'task_id', 'submissions': 'submission_id',
             'reviews': 'review_id', 'changes': 'change_id'}
    for name in names:
        check(isinstance(graph.get(name), list), f'missing array {name}')
    if errors:
        return errors
    records = {name: indexed(graph[name], key) for name, key in names.items()}
    tests, sources, extracts, links, tasks, submissions, reviews, changes = (records[n] for n in names)
    claims = table('claims/claim-register.csv', 'claim_id')
    source_register = table('sources/source-register.csv', 'source_id')
    inventory = table('sources/p1-federal-source-inventory.csv', 'source_id')
    observations = table('data/p1-federal-fiscal-observations.csv', 'observation_id')
    for t in tests.values():
        required(t, ['proposition', 'requirements', 'failure_condition'])
        check(t.get('parent_claim_id') in claims, 'unknown parent claim')
        check(t.get('decision') == 'untested', 'pilot cannot promote a claim')
        check(t.get('claim_kind') in {'accounting', 'mechanism', 'legal', 'causal'}, 'invalid claim kind')
        check((root / t.get('gate_file', '')).is_file(), 'missing gate file')
    for s in sources.values():
        check(s['source_id'] in source_register, 'unknown canonical source')
        inv = inventory.get(s.get('inventory_id'), {})
        check(inv.get('canonical_source_id') == s['source_id'], 'source inventory mismatch')
        required(s, ['origin_basis'])
    for e in extracts.values():
        obs = observations.get(e.get('observation_id'), {})
        check(e.get('source_id') in sources, 'unknown extract source')
        check(obs.get('canonical_source_id') == e.get('source_id'), 'observation source mismatch')
        check(bool(e.get('locator')) and obs.get('page_or_frame') == e.get('locator'), 'observation locator mismatch')
        check(e.get('inspection') == 'legacy_reference', 'pilot cannot imply new inspection')
    for t in tasks.values():
        required(t, ['title', 'target', 'acceptable_result', 'capture_standard', 'stop_rule'])
        check(t.get('test_id') in tests, 'unknown task test')
        check(bool(t.get('source_ids')) and all(s in sources for s in t['source_ids']), 'unknown task source')
        check((root / t.get('baseline_file', '')).is_file(), 'missing task baseline')
        check(t.get('status') in {'OPEN', 'SUBMITTED', 'REVIEWED', 'INCORPORATED', 'REJECTED', 'CLOSED_NO_CHANGE'}, 'invalid task status')
    for s in submissions.values():
        required(s, ['contributor', 'url', 'summary'])
        check(s.get('task_id') in tasks, 'unknown submission task')
        check(date(s.get('submitted_at')), 'invalid submission date')
    for r in reviews.values():
        required(r, ['reviewer', 'rationale'])
        check(r.get('submission_id') in submissions, 'unknown review submission')
        check(r.get('outcome') in {'accept', 'reject', 'no_change'}, 'invalid review outcome')
        check(date(r.get('reviewed_at')), 'invalid review date')
    for c in changes.values():
        required(c, ['rationale'])
        r = reviews.get(c.get('review_id'), {})
        s = submissions.get(c.get('submission_id'), {})
        check(r.get('outcome') == 'accept' and r.get('submission_id') == c.get('submission_id') and bool(s), 'change lacks accepting review')
        check(c.get('task_id') in tasks and s.get('task_id') == c.get('task_id'), 'change task mismatch')
        check(tasks.get(c.get('task_id'), {}).get('status') == 'INCORPORATED', 'change task not incorporated')
        check(date(c.get('changed_at')), 'invalid change date')
        check(bool(c.get('affected_link_ids')) and all(i in links for i in c['affected_link_ids']), 'unknown/empty affected links')
        for ident in c.get('affected_link_ids', []):
            l = links.get(ident, {})
            check(l.get('status') == 'reviewed' and l.get('review_id') == c.get('review_id'), 'change link review mismatch')
            check(l.get('test_id') == tasks.get(c.get('task_id'), {}).get('test_id'), 'change link test mismatch')
    for l in links.values():
        required(l, ['rationale', 'limitations'])
        check(l.get('test_id') in tests, 'unknown link test')
        check(bool(l.get('extract_ids')) and all(e in extracts for e in l['extract_ids']), 'unknown/empty link extracts')
        check(l.get('relation') in {'supports', 'contradicts', 'qualifies'}, 'invalid evidence relation')
        check(l.get('status') in {'proposed', 'reviewed'}, 'invalid link status')
        if l.get('status') == 'proposed':
            check(l.get('review_id') is None, 'proposed link has review')
        else:
            r = reviews.get(l.get('review_id'), {})
            check(r.get('outcome') == 'accept', 'reviewed link lacks accepting review')
            check(any(l['link_id'] in c.get('affected_link_ids', []) and c.get('review_id') == l.get('review_id') for c in changes.values()), 'reviewed link lacks change trail')
    for ident, t in tasks.items():
        ss = [s for s in submissions.values() if s.get('task_id') == ident]
        rr = [r for r in reviews.values() if r.get('submission_id') in {s['submission_id'] for s in ss}]
        state = t.get('status')
        if state == 'OPEN':
            check(not ss, 'OPEN task has submissions')
        if state != 'OPEN':
            check(bool(ss), 'closed/progressed task lacks submission')
        if state in {'REVIEWED', 'INCORPORATED', 'REJECTED', 'CLOSED_NO_CHANGE'}:
            check(bool(rr), 'task lacks review')
        if state == 'REJECTED':
            check(any(r.get('outcome') == 'reject' for r in rr), 'rejected task lacks rejection')
        if state == 'CLOSED_NO_CHANGE':
            check(any(r.get('outcome') == 'no_change' for r in rr), 'no-change task lacks decision')
        if state == 'INCORPORATED':
            check(any(c.get('task_id') == ident for c in changes.values()), 'incorporated task lacks change')
    return errors


if __name__ == '__main__':
    graph = json.loads((ROOT / 'collaboration/c001-pilot.json').read_text())
    errors = validate(graph)
    print('\n'.join(errors) if errors else 'Collaboration graph valid; no analytical admission granted.')
    sys.exit(bool(errors))
