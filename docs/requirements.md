# DataMan Requirements Register

## Project Context

The DataMan modernization project works to bring the original 1977 DataMan math quiz toy experience into a modern application while preserving the behavoirs that made it effective for learning. The primary users are students practicing math independently, often in settings where a teacher or parent is nearby but not directly operating the device. The project must resolve how to modernize the interface without losing the immediate-feedback, repeat-practice, and progress-tracking experience that defined the original toy.

## Evidence Notes

- **E-01 — Source:** DataMan manual(Answer Checker)
  **Evidence:** When a user enters a problem and an answer, DataMan flashes its display to confirm a correct answer; on incorrect answers it displays "EEE" with a blinking-light pattern and gives the user a second try before revealing the correct answer.

- **E-02 — Source:** Dataman manual(Answer Checker)
  **Evidence:** After every ten problems, DataMan displays two numbers, one is the count of right answers and the second is count of problems tried. This is kept as a running score.

- **E-03 — Source:** DataMan manual (Memory Bank) 
  **Evidence:** A parent, teacher or friend can store up to ten custom problems in DataMan's memory. Pressing GO recalls them one at a time, gives two tries per problem, and at the end reports correct answers vs tried answer score

- **E-04 — Source:** Elicitation  
  **Evidence:** Teachers report that students may pause practice and return later, and they want a learner's save practice state to remain available after leaving and then returning

- **E-05 — Source:** Elicitation  
  **Evidence:** Students may use DataMan on school Chromebooks, tablets, and home computers, and some sessions are interrupted before an intential sign-out.

## Functional Requirements

Write at least four functional requirements. Each requirement should describe a capability or behavior the system must provide.

### FR-01
**Requirement:** The system must preserve a user's in-progress practice state when a session ends unexpectedly, without requiring the user to sign out, and must allow the user to resume that state when signing back in.  
**Source/Rationale:** Directly supported by E-04, stake holders want a saved state to persist across leaving and returning

### FR-02
**Requirement:** The system must indicate to the leaner whether a submitted answer is correct immediately after submission.
**Source/Rationale:** The original answer checker confrims a correct answer with an immediate visual signal

### FR-03
**Requirement:** The system must give a learner a second attempt at a problem after an incorrect answer, and must reveal the correct answer if the second attempt
**Source/Rationale:** The manual states the behavior for Answer Checker's two-try-then-reveal.

### FR-04
**Requirement:** The system must track and display, at the end of a set of problems, the number of problems answered correctly versus the number attempted.  
**Source/Rationale:** E-02 and E-03 note the devices score keeping in both Answer Checker and Memory Bank

## Non-Functional Requirements

### NFR-01
**Requirement:** The system must display answer feedback without a noticable delay after submission.  
**Source/Rationale:** E-01 the original device's flash response to a submitted answer

### NFR-02
**Requirement:** The system must remain usable across the range of devices students are known to use, including Chromebooks, phones, tablets and home computers.  
**Source/Rationale:** E-05 confirmed the actual range of devices in use.

### NFR-03
**Requirement:** The system must retain a user's save practice state reliably enough to survive a session ending suddenly, without proper signout.
**Source/Rationale:** E-05  concluded that relying on intentional sign out would not protect work during interruptions.

### NFR-04
**Requirement:** The system must report accurately, and reflect the number of correct answers against the number of attempted answers.
**Source/Rationale:** The original device's feedback was noted in the manual, and must be present in the modernized version.

## Open Questions / Assumptions

Do not turn an unsupported idea into a confirmed requirement. Record unresolved items here until evidence supports a decision.

- **Q-01:** Exact devices and access conditions (like browser support, offline use) are not confirmed yet
- **Q-02:** Will individual user accounts be able to identify unique users, and preserve progress is assumed
- **Q-03:** The maximum acceptable feedback response time has not been confirmed
- **Q-04:** Stakeholder use of the terms "modern" and "simple" has not been clarified.
