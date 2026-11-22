# M5 Implementation Finding — Two-Attempt Answer Checker

## What I tested

US-02 / FR-03 gives the learner one retry after an incorrect answer. A second
incorrect answer should reveal the correct answer and end the problem.

## What the starter showed

On the 6 × 7 problem, the first wrong answer moved the learner to Try 2.
After the second wrong answer, the page revealed 42 and removed the answer
box, but it still displayed “Try: 3.” The template was adding one to the
attempt count even after the round had ended.

## What changed and what the test confirmed

I kept the two-attempt rule in the Module 4 `AnswerChecker`. The Flask page
now uses `next_try_number()` to decide when to show the try number and answer
box.

In a Flask test of the migrated 7 × 8 problem, entering 54 displayed
“Incorrect. You have one try left.” Refreshing the page kept it on Try 2.
Entering 55 then displayed “The correct answer is 56.” The round ended with
no answer box and no Try 3 label.
