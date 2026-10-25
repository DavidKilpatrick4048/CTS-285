# M4 Lab Evidence Record

## Answer Flow Lab
**Initial design decision tested:** Attempt/state representation

**Scenario that exposed the issue:** Wrong, then correct

### Consequence Observed
Keeping only the final correct result lost the details of the first incorrect attempt. The result could not distinguish success on the first try from success on the second try.

### Revision Made
I changed the comparison configuration to use separate attempt records with try numbers. This keeps each answer and its outcome so first-try success, second-try success, and two incorrect attempts remain distinguishable.

### What Changed After Revision
The revision preserved the first incorrect attempt and the second correct attempt separately. The outcome could now be identified as second-try success.

---

## Memory Bank & Curator Retrieval Lab
**Initial design decision tested:** Attempt/session/result storage

**Scenario that exposed the issue:** Curator retrieves prior learner results

### Consequence Observed
The original model kept the session/result, but the curator query could not identify which problems the learner missed. The review failed both problem identity preservation and later curator retrieval.

### Revision Made
I replaced final-score-only storage with attempt records containing problem_id, try_number, correct, and session_id.  These connect each answer outcome to its problem and learner session, keeping the information needed to retrieve missed problems.

### What Changed After Revision
The curator query returned P2 and P5 as the missed problems.  The problem identity and retrieval checks changed from FAIL to PASS, and all five review checks passed.

---

## Cross-Lab Finding
The tests made the problem of storage choices visible. A final result alone can lose attempt history.  In the Memory Bank lab, the query failed even though the session/result continued. Preserving data must include enough detail to answer the questions users will ask later.

## Revised / New Design Question
What information must my DataMan prototype keep for each attempt so it enforces the two-attempt rule and later distinguishes first-try success, second-try success and two incorrect attempts?
