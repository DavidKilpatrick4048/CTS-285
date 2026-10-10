# DataMan Product Backlog

## Sources

This backlog uses these files from my repository:

- `docs/requirements.md`
- `docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`

## Priority Order

1. [US-01 Immediate answer feedback]
2. [US-02 Retry an incorrect answer]
3. [US-03 View end of set results]
4. [US-04 Use core practice across student devices]
5. [US-05 Resume interrupted practice]

## Stories

### US-01 — Immediate answer feedback
  
**Requirement ID:** FR-02, NFR-01, NFR-03 from `docs/requirements.md`.
  
**User Story:** As a learner, I want to know whether my submitted answer is correct immediately so that I can recognize success or a mistake while practicing.

**Acceptance Criteria:**

- Given a learner submits a correct answer to a practice problem, when the system evaluates that submission, then it presents a correctness indication identifying the answer as correct.
- Given a learner submits an incorrect answer, when the system evaluates that submission, then it presents a correctness indication identifying the answer as incorrect.
- Given a learner submits an answer, when the system evaluates it, then the correctness indication appears without requiring another learner action to request the result.
- Given equivalent correct or incorrect outcomes occur on different problems, when feedback is presented, then the indications communicate the same meaning throughout practice.

**Relative Effort:** Small — Evaluating an answer and indicating correctness is narrower than accumulating set results, checking multiple device environments, or preserving interrupted practice.

**Dependency / Constraint:** None for the answer-feedback behavior. The triage stakeholder requires it for the first usable release. NFR-01 requires immediate feedback, but Q-03 leaves the maximum acceptable response time unconfirmed; measurable timing acceptance still requires refinement. NFR-03 requires consistent correctness indications.

**Priority:** 1

**Readiness:** Move Forward

**Priority Rationale:** This is high-value, small-effort work and the stakeholder explicitly requires it for the first usable release. It also supports the answer-checking flow needed by US-02. 

---

### US-02 — Retry an incorrect answer

**Requirement ID:** FR-03, NFR-03 from `docs/requirements.md`.

**User Story:** As a learner, I want a second attempt after an incorrect answer and the correct answer if I am still wrong so that I can practice correcting my mistake and learn the solution.

**Acceptance Criteria:**

- Given a learner's first answer to a problem is incorrect, when the result is presented, then the learner can submit a second answer to that same problem before the correct answer is revealed.
- Given the learner's second answer is correct, when that submission is evaluated, then the system indicates that it is correct using the same correctness meaning as other correct answers.
- Given the learner's second answer is incorrect, when that submission is evaluated, then the system indicates that it is incorrect and reveals the correct answer to that problem.
- Given both permitted attempts were incorrect, when the correct answer has been revealed, then a third attempt is not offered for that presentation of the problem.

**Relative Effort:** Small — This adds a bounded two-attempt flow to US-01 and is smaller than set-level scorekeeping, device coverage, or interrupted-session preservation.

**Dependency / Constraint:** US-01's answer evaluation and correctness feedback. FR-03 establishes two attempts and correct-answer disclosure after the second incorrect attempt; NFR-03 requires consistent feedback.

**Priority:** 2

**Readiness:** Move Forward

**Priority Rationale:** Retry behavior has high learning value, small relative effort, and low uncertainty because FR-03 defines the two-attempt behavior. It follows US-01 because it depends on answer checking. 

---

### US-03 — View end-of-set results

**Requirement ID:** FR-04, NFR-03 from `docs/requirements.md`.

**User Story:** As a learner, I want to see how many problems I answered correctly compared with how many I attempted at the end of a practice set so that I can understand my results.

**Acceptance Criteria:**

- Given a completed set contains ten problems, eight answered correctly on the first attempt and two answered incorrectly on both attempts, when the set ends, then the system displays eight problems correct and ten problems attempted.
- Given a learner makes two attempts at the same problem, when the completed set's attempted-problem total is displayed, then that problem contributes one problem to the attempted total.
- Given a learner completes a practice set, when its results are presented, then the correct and attempted counts are distinguishable and refer to that completed set.
- Given results are presented for different completed sets, when the learner reads the counts, then the meanings of correct problems and attempted problems remain consistent.

**Relative Effort:** Medium — Accumulating results across distinct problems and handling retries adds more coordination than US-01 or US-02, but less than preserving learner state across interrupted sessions.

**Dependency / Constraint:** US-01 and US-02 provide the answer outcomes and attempt behavior. Before this story moves forward, clarify whether a problem solved on its second attempt counts toward the correct total; FR-04 does not explicitly settle that rule. NFR-03 requires consistent scoring.

**Priority:** 3

**Readiness:** Refine

**Priority Rationale:** Learner-visible results preserve an established DataMan behavior and provide value after feedback and retries are available. Medium effort and a dependency on those outcomes justify this position.

---

### US-04 — Use core practice across student devices

**Requirement ID:** NFR-02 from `docs/requirements.md`.

**User Story:** As a learner, I want to complete practice on a Chromebook, phone, tablet, or home computer so that I can use the device available to me at school or at home.

**Acceptance Criteria:**

- Given an agreed test environment from each of the four device categories, when a learner submits correct and incorrect answers, then the learner can enter each answer and read the corresponding correctness feedback in every category.
- Given a first incorrect answer in each agreed device environment, when the learner uses the permitted second attempt, then the learner can submit it and read the correct answer if the second attempt is also incorrect.
- Given a completed practice set in each agreed device environment, when results are presented, then the learner can read both the correct-problem and attempted-problem counts.

**Relative Effort:** Medium — Checking the core practice sequence across four device categories is broader than one feedback or retry behavior, but narrower than restoring interrupted practice for an identified learner.

**Dependency / Constraint:** US-01, US-02, and US-03 supply the core behaviors being checked. Q-01 must establish the specific supported devices, browsers, and access conditions before the acceptance environments can be finalized. Offline use remains an open question.

**Priority:** 4

**Readiness:** Refine

**Priority Rationale:** Device usability matters because E-05 identifies these device categories as part of learners' real access conditions. Its position follows the core behaviors it must support. Refinement has value now, but unknown support conditions prevent a defensible implementation commitment or final compatibility judgment. This makes the uncertainty visible without adding unsupported browser or offline promises.

---

### US-05 — Resume interrupted practice

**Requirement ID:** FR-01, NFR-02 from `docs/requirements.md`.

**User Story:** As a learner, I want my in-progress practice preserved when a session ends unexpectedly so that I can sign back in and continue without losing my work.

**Acceptance Criteria:**

- Given an identified learner is halway through a practice set, when the session ends unexpectedly without sign-out and the learner signs back in, then the interrupted practice state is able to resume.
- Given the learner completed problems before the interruption, when the learner resumes that practice set, then the completed work remains recorded and is not lost because the session ended.
- Given two identified learners have different in-progress practice states, when each signs back in, then each learner receives their own preserved state.
- Given the agreed supported environments cover Chromebooks, phones, tablets, and home computers, when an identified learner resumes interrupted practice within each environment, then that learner can continue the preserved practice in every device category.

**Relative Effort:** Large — Preserving and restoring learner-specific state through interruptions requires more coordination and uncertainty resolution than the feedback, retry, score, or core device-usability stories.

**Dependency / Constraint:** Q-02's identity/session approach is not ready. US-01 through US-03 establish the practice behavior and results to preserve; Q-01 and US-04 establish supported access conditions. FR-01 requires recovery after an unexpected end without sign-out and resumption when signing back in. The identity method must be agreed before these learner-specific acceptance scenarios can be finalized.

**Priority:** 5

**Readiness:** Defer

**Priority Rationale:** This has high stakeholder value, but the triage record identifies large effort, medium risk, and an unresolved identity/session dependency. Advancing it now could require rework once learner identification is decided.

---

## Open Questions Carried Forward

- **Q-01:** Which exact devices, browsers, and access conditions must be supported, including whether offline use is required? US-04 remains Refine until its test environments are agreed. US-05 also needs these conditions before its device-related acceptance scope can be finalized.
- **Q-02:** How will the system identify unique learners and associate them with preserved practice? Individual accounts are an assumption, not an agreed solution. US-05 stays Defer because the account/session approach is not ready.
- **Q-03:** What is the maximum acceptable answer-feedback response time? US-01 moves forward for its established answer-feedback behavior, as required by triage, but NFR-01's numerical timing acceptance cannot be finalized until this question is answered.
- **Q-04:** What do stakeholders mean by "modern" and "simple"? These terms may affect later usability and theme decisions for US-01 through US-04. They do not provide a testable acceptance condition or justify an additional feature.

## Revisions After Triage and Release Planning

- **US-01:** Kept Move Forward and ranked first because triage S1 requires immediate feedback for the first usable release. The response-time limit in Q-03 still needs clarification.
- **US-02:** Kept Move Forward and placed after US-01 because triage S5 depends on answer checking. The story preserves the two-attempt behavior in FR-03.
- **US-03:** Added learner scores from FR-04 and marked Refine. Whether a correct second attempt counts toward the correct total still needs clarification.
- **US-04:** Added device usability from NFR-02 and marked Refine because the supported devices and access conditions in Q-01 are not fully confirmed.
- **US-05:** Changed from Refine to Defer, following triage S2, because the identity/session approach is not ready.


