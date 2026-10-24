# M4 Investigation Brief

## Product Slice
US-01 Immediate answer feedback, US-02 Retry an incorrect answer

## Trace to Product Work
FR-02 requires feedback after an answer is submitted. FR-03 requires a second attempt after an incorrect answer and revealing the correct answer after a second incorrect attempt. US-02’s acceptance criteria also require keeping the same problem for the retry and not offering a third attempt. I need to investigate how the design will distinguish the two attempts and determine when the problem is finished.

## Initial Design Question
**Question type:** Data / State

What information must the system keep for the current problem to distinguish the first and second attempts, determine whether a retry is allowed, and know when the problem is finished?

## Why This Question Matters
Without defining this state, the program could lose track of attempts, reveal the correct answer after the first mistake, or allow a third attempt. Fixing these problems later could require changes to the answer-checking logic and how information about the current problem is stored.

## Planned Evidence
- Field or state table
- Acceptance-criteria trace

## Why This Evidence Is a Reasonable Starting Point
A state table can help identify what information must be kept for the current problem and how it changes after each answer. An acceptance-criteria trace can check first-attempt success, a retry after an incorrect answer, second-attempt success, and revealing the answer after a second mistake. Together, they can show whether the design tracks attempts correctly and prevents a third attempt.

## Studio Check
During the DataMan Design Studio, record whether the evidence actually answered the question, whether you needed different evidence, and what new question emerged.
