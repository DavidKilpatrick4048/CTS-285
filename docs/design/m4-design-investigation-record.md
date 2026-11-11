# M4 Design Investigation Record

## Product Slice
US-01 - Immediate answer feedback; US-02 - Retry an incorrect answer

## Initial Question
What information must the system keep for the current problem to distinguish the first and second attempts, determine whether a retry is allowed, and know when the problem is finished?

## Planned Evidence
A field or state table and an acceptance-criteria trace.

## Evidence Actually Used
- Use-case boundary / actor-goal framing
- Behavior/state flow and two-attempt simulation
- Data-model/schema and Memory Bank constraint stress tests
- Interface/wireframe comparison and state audit
- Design complication and critique

## Findings
### Use-Case Boundary / Question Framing
Learner > Check a practice answer and get one more try if the first answer is wrong.  Question: What information must DataMan keep about each attempt so it can enforce the two-attempt rule and distinguish a correct first answer, a correct retry, and two incorrect answers?

### Behavior / State
What does DataMan need to remember to decide whether to allow a retry, finish the problem, or reveal the answer? It needs to know which problem is active, which attempt was submitted, and whether that answer was correct. A first miss keeps the problem open, while a second miss ends it and reveals the answer. A correct answer ends the problem on either try.

### Data / Persistence
A single learner answer stored on Problem would lose the first attempt when the learner retries. Separate attempt records keep both outcomes tied to the same problem and learner session, so DataMan can tell a successful retry from two misses.

### Memory Bank Constraint
The eleventh addition was rejected, and the set stayed at ten problems. The rule belongs in the shared logic that adds a problem to a set so the same limit applies in the text prototype and later in Flask.

**Constraint boundary selected:** both

### Interaction
Approach A showed why EEE alone can leave a learner unsure what to do next. Approach B made the attempt number visible, but showing the previous answer beside “Try 2 of 2” made it unclear which try that answer belonged to. After the first miss, I would show “Incorrect. One try left” and keep the same problem open. After the second miss, I would show the correct answer and a clear way to continue. The business logic should decide when retry or reveal is allowed. For later curator review, the attempts should stay linked to the learner’s session and problem.

## Layer Boundary Notes
**Business behavior that should remain outside the interface:**
The business logic should check the answer, record the try number and outcome, and decide whether to allow a retry, finish the problem, or reveal the correct answer. The text interface and Flask can both use that result to display feedback.

**Data that can be stubbed now:**
For my feedback and retry slice, I can keep sample problems, one test learner session, and its numbered attempt records in memory. The business logic can read problems and save attempts through a small data layer. Later, persistent storage can replace the lists without changing the answer checking or retry rules.

## New Complication
**Response:** Revise state boundary

The behavior test showed that the first miss allows a retry and the second miss reveals the answer. The Memory Bank query could identify P2 and P5 only after attempts were tied to their problems and sessions. I would record the first miss when it happens so closing the screen does not erase the evidence needed for a retry or later review.

## Build-Readiness Decision
**Disposition:** Revise

**Design decision:**
Revise US-01 and US-02 so the business logic reads and records each numbered attempt through a data layer. The interface displays the retry or reveal decision returned by that logic. The text prototype can use in-memory storage during one run. Resuming after the program closes requires persistent storage and a way to locate the correct unfinished session.

## Revision From Initial Thinking
I started by asking how to tell the two tries apart during practice. The close-after-Try-1 case showed why the screen cannot be the only place that remembers the first miss. When the same session is reopened, the saved first miss should put the learner on Try 2 with the answer still hidden.

## Tradeoff Accepted
Separate attempt records take a little more work, but they preserve the difference between a correct first answer, a correct retry, and two misses. An in-memory data layer lets me test the shared rules before adding persistent storage.

## Unresolved Uncertainty
Q-02 still needs an agreed way to match a returning learner to the correct unfinished session. The maximum feedback delay in Q-03 and the rules for curator access to learner history also remain open.

## Next Question
How will DataMan find the correct unfinished session for a returning learner so they can resume the same problem at Try 2 with the answer still hidden?

## Three-Layer Prototype Bridge
Text interface: Show the problem, and current try number, accept the learners answer, and display feedback and the next action returned
Business Logic: check the answer and record each numbered attempt through the data layer. After the first miss, keep the same problem open and allow one retry. Finish after a correct answer, or reveal the answer and finish after the second miss. If memory bank is added, enforce the 10-problem limit.
Stubbed data layer: Keep sample problems, a test session and separate attempt records in memeory. Link each attempt to its problem and session. Provide simple functions to read and save records so persistent storage can replace the memory version later.

## Trace Back to Product Work
US-01 > FR-02, NFR-01, NFR-03: Give consistent correct or incorrect feedback after submission without requiring another action. The maximum acceptable response time is still open under Q-03.

US-02 > FR-03, NFR-03: After the first miss, keep the same problem open for a retry and hide the answer. Give correct feedback if the retry succeeds. After the second miss, reveal the correct answer and prevent a third attempt.
