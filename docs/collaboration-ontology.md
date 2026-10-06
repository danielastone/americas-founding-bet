# Collaboration ontology v1

The canonical pilot is `collaboration/c001-pilot.json`. Arrays are related by stable IDs, not document titles or names. Existing CSV registers remain authoritative for sources and observations. Bibliographic alignment remains in metadata; no full BIBFRAME implementation is introduced.

| Record | Key and relations | Meaning |
|---|---|---|
| Test | test_id → parent_claim_id | Independently evaluated proposition; kinds: accounting, mechanism, legal, causal |
| Source reference | source_id → source register; inventory_id → P1 inventory | Reuses canonical identity without copying bibliographic metadata |
| Extract reference | extract_id → source_id, observation_id | Exact existing observation and its locator; does not duplicate amount or evidence state |
| Evidence link | link_id → test_id, extract_ids, review_id | Relation: supports, contradicts, qualifies; rationale and limitations required |
| Task | task_id → test_id, source_ids | Bounded gap, target, acceptable result, capture standard, stop rule |
| Submission | submission_id → task_id | Attributable contribution and durable issue/PR URL |
| Review | review_id → submission_id | Attributable decision with rationale |
| Change | change_id → task_id, submission_id, review_id, affected_link_ids | Incorporation audit trail; does not itself grant analytical admission |

Links start proposed with null review_id. A reviewed link requires an accepting review, an incorporated task and a matching change record. All of its extracts must reference valid existing observations. `legacy_reference` inspection means this migration references earlier work; it does not assert a new image check.

Origin groups describe known shared ancestry, not independent corroboration. Different group IDs do not prove independence; unknown ancestry remains null with a reason. A reproduction and its underlying report must not be counted twice. The pilot does not compute support counts or claim confidence.

Task state is workflow metadata. Observation evidence_state is analytical maturity. Test decision is a conclusion under an applicable gate. These three axes must never be substituted for each other. P1 supports an accounting composition test; P3 needs timing and mechanism evidence. Legal authority cannot establish implementation, and a descriptive association cannot establish causation without a counterfactual.

Unknown fields use null with an explanation. New source or observation records must first enter the existing authoritative registers. A task-level source reference may be a discovery lead, but an extract must point to an existing observation with an exact locator.
