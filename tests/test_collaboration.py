import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate_collaboration.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class CollaborationControls(unittest.TestCase):
    def setUp(self):
        self.graph = json.loads((ROOT / 'collaboration/c001-pilot.json').read_text())

    def test_seed(self):
        self.assertEqual(validator.validate(self.graph), [])

    def test_wrong_observation_source(self):
        self.graph['extracts'][0]['source_id'] = 'AFB-S087'
        self.assertIn('observation source mismatch', validator.validate(self.graph))

    def test_locator_mismatch(self):
        self.graph['extracts'][0]['locator'] = 'PDF-image-99'
        self.assertIn('observation locator mismatch', validator.validate(self.graph))

    def test_claim_promotion(self):
        self.graph['tests'][0]['decision'] = 'supported'
        self.assertIn('pilot cannot promote a claim', validator.validate(self.graph))

    def test_unreviewed_incorporation(self):
        self.graph['tasks'][0]['status'] = 'INCORPORATED'
        self.assertIn('incorporated task lacks change', validator.validate(self.graph))

    def test_reviewed_link_requires_trail(self):
        self.graph['links'][0]['status'] = 'reviewed'
        self.assertIn('reviewed link lacks change trail', validator.validate(self.graph))

    def test_complete_incorporation_path(self):
        g = self.graph
        g['tasks'][0]['status'] = 'INCORPORATED'
        g['submissions'] = [{'submission_id': 'SUB-TEST', 'task_id': 'AFB-TASK-001', 'contributor': 'Fixture only', 'submitted_at': '2026-10-06', 'url': 'https://example.org/fixture', 'summary': 'Synthetic lifecycle fixture; never canonical evidence.'}]
        g['reviews'] = [{'review_id': 'REV-TEST', 'submission_id': 'SUB-TEST', 'reviewer': 'Fixture only', 'reviewed_at': '2026-10-06', 'outcome': 'accept', 'rationale': 'Synthetic control test.'}]
        g['links'][0].update(status='reviewed', review_id='REV-TEST')
        g['changes'] = [{'change_id': 'CH-TEST', 'task_id': 'AFB-TASK-001', 'submission_id': 'SUB-TEST', 'review_id': 'REV-TEST', 'changed_at': '2026-10-06', 'rationale': 'Synthetic fixture.', 'affected_link_ids': ['AFB-LINK-001']}]
        self.assertEqual(validator.validate(g), [])
        bad = copy.deepcopy(g)
        bad['changes'][0]['submission_id'] = 'MISSING'
        self.assertIn('change lacks accepting review', validator.validate(bad))

    def test_duplicate_id(self):
        self.graph['extracts'].append(copy.deepcopy(self.graph['extracts'][0]))
        self.assertTrue(any('duplicate extract_id' in e for e in validator.validate(self.graph)))
