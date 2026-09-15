# M2 Elicitation Decision Record

## Investigation Path
1. Who will use the system and in what setting?
   Evidence revealed: The primary learner is a student practicing independently, often with a teacher or parent nearby. Exact device and access conditions have not yet been confirmed.
2. What exactly do stakeholders mean by “students shouldn’t lose their work”?
   Evidence revealed: Teachers report that students may pause practice and return later. They want a learner’s saved practice state to remain available after leaving and returning to the application.
3. Which original DataMan behaviors are considered essential to preserve?
   Evidence revealed: Stakeholders identify immediate answer feedback, repeated practice after an incorrect response, and a clear way for learners to see progress as central to the original experience.

## Initial Position
**Supported evidence:**
The primary user is a student that may practice independently with a teacher or parent near. Users may need to pause and resume practice without losing data. Immediate Feedback, repeated practice after an incorrect response and visible progress are important.

**Remaining uncertainty:**
The device conditions, methods of identifying users, length of time work must be saved, feedback response time, meaning of "modern" and "simple" remains unknown.

**Likely functional requirement:**
The system must allow a user to resume their saved practice state after leaving and returning

**Likely non-functional requirement / quality constraint:**
Answer feedback must appear immediately after a user submits a response.  The maximum response time remains unconfirmed.

**Assumption or proposed solution I am not treating as confirmed:**
The system will require individual user accounts to preserve progress. This has not been confirmed.

**Why my initial position is defensible:**
Evidence 1 provides the user context
Evidence 2 the functional requirement of a pause and resume need
Evidence 3 feedback response time
The position is defensible because it can traced directly to collected evidence
Uninvestigated statements like modern, simple, and parents information needs

## Complication
Students may use DataMan on school Chromebooks, phones, tablets, and home computers. Some sessions may be interrupted before intentional sign-out.

**What this affects:**
It affects the pause and resume functionality.  It resolves the uncertainity about devices and access conditions.  "leaving and returning" must now account for sessions that end unexpectedly without signing out.   The various devices also bring up the question of cross-device continuity.

**What I revised, if anything:**
The system must preserve a user's in progress practice state when a sessions ends unexpectedly, without requiring the user to sign out and must allow the user to resume that state upon signing back in"

**Final decision and reasoning:**
Revise the functional requirement, Relying on an intentional sign off would not protect user work during interruptions.   I would need to ask further questions about exactly which devices are being used.

## Next Project Action
Use this evidence to update the DataMan Requirements Register and preserve any unresolved questions as open assumptions or follow-up items.
