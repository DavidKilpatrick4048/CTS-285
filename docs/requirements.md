# DataMan Requirements Register

## Project Context

The DataMan modernization project works to bring the original 1977 DataMan math quiz toy experience into a modern application while preserving the behaviors that made it effective for learning. The primary users are students practicing math independently, often in settings where a teacher or parent is nearby but not directly operating the device. The project must determine how to modernize the interface without losing the immediate-feedback, repeat-practice, and progress-tracking experience that defined the original toy.

## Evidence Notes

- **E-01 — Source:** DataMan manual(Answer Checker)
  **Evidence:** When a user enters a problem and an answer, DataMan flashes its display to confirm a correct answer. For an incorrect answer, it displays "EEE" with a blinking-light pattern and gives the user a second try before revealing the correct answer.

- **E-02 — Source:** DataMan manual(Answer Checker)
  **Evidence:** After every ten problems, DataMan displays two numbers: the number of correct answers and the number of problems attempted. This is kept as a running score.

- **E-03 — Source:** DataMan manual (Memory Bank) 
  **Evidence:** A parent, teacher or friend can store up to ten custom problems in DataMan's memory. Pressing GO recalls them one at a time, gives the learner two tries per problem, and reports the number of correct answers compared with the number of attempted problems at the end.

- **E-04 — Source:** Elicitation  
  **Evidence:** Teachers report that students may pause practice and return later, and they want a learner's saved practice state to remain available after leaving and returning.

- **E-05 — Source:** Elicitation  
  **Evidence:** Students may use DataMan on school Chromebooks, phones, tablets, and home computers, and some sessions are interrupted before an intentional sign-out.

## Functional Requirements

### FR-01
**Requirement:** The system must preserve a learner's in-progress practice state when a session ends unexpectedly, without requiring the user to sign out, and must allow the user to resume that state when signing back in.  
**Source/Rationale:** E-04 establishes the need for learners to leave and return without losing their saved practice state. E-05 establishes that some sessions may end unexpectedly.

### FR-02
**Requirement:** The system must indicate to the learner whether a submitted answer is correct immediately after submission.
**Source/Rationale:** E-01 establishes that the original Answer Checker provides immediate visual feedback after an answer is submitted.

### FR-03
**Requirement:** The system must give a learner a second attempt at a problem after an incorrect answer, and must reveal the correct answer if the second attempt is incorrect.
**Source/Rationale:** E-01 establishes the Answer Checker's two-attempt behavior and the revealing of the correct answer after the second incorrect attempt.

### FR-04
**Requirement:** The system must track and display, at the end of a set of problems, the number of problems answered correctly versus the number attempted.  
**Source/Rationale:** E-02 and E-03 note the device's scorekeeping in both Answer Checker and Memory Bank

## Non-Functional Requirements

### NFR-01
**Requirement:** The system must provide answer feedback without an unnecessary delay after the learner submits an answer. The maximum acceptable response time remains to be confirmed.
**Source/Rationale:** E-01 establishes that the original Answer Checker provides feedback immediately after an answer is submitted. A measurable maximum response time has not yet been established.

### NFR-02
**Requirement:** The system must remain usable across the range of devices students are known to use, including Chromebooks, phones, tablets and home computers.  
**Source/Rationale:** E-05 identifies the range of devices students may use to access the modernized DataMan system.

### NFR-03
**Requirement:** The system must present correctness feedback and score information consistently during the learner's practice experience.
**Source/Rationale:** E-01 establishes the need for correctness feedback, while E-02 and E-03 establish score reporting as part of the original DataMan.

## Open Questions / Assumptions

- **Q-01:** Exact devices and access conditions (like browser support, offline use) are not confirmed yet.
- **Q-02:** Will individual user accounts be able to identify unique users, and preserve progress is assumed.
- **Q-03:** The maximum acceptable feedback response time has not been confirmed.
- **Q-04:** Stakeholder's use of the terms "modern" and "simple" has not been clarified.
