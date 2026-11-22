# M5 Feature Decision — Recall the Next Stored Problem

I chose the GO behavior from Memory Bank evidence E-03. It recalls one stored
problem at a time. I will reuse the two-attempt checker from US-02 / FR-03.

For this version, GO becomes available after the current problem closes.
Finishing 7 × 8 and clicking GO should open 6 × 7 on Try 1 with a fresh answer
box. Finishing the last problem should end the set.

The Flask route will handle the button. The checker will decide when another
problem can be recalled. MemoryStore will keep the order of the two problems,
the current problem for each practice session, and the numbered attempts.

My question is whether the next problem starts on Try 1 while the first
problem's attempts are still saved under its own ID.

## Test results and decision

### Two-attempt rule (US-02 / FR-03)

I entered 54 for 7 × 8 and refreshed the page. It stayed on Try 2 and
kept the correct answer hidden. When I entered 55, the page revealed 56,
removed the answer box, and showed the GO button. There was no Try 3.

### GO to the next problem (Memory Bank E-03)

Clicking GO opened 6 × 7 on Try 1 with an empty answer box. The feedback
from 7 × 8 was gone. I entered 41 and got one retry. When I entered 42,
the page displayed “Correct.” and “Practice set complete.” The GO button
was gone after the last problem.

### What I fixed and kept

During testing, the page showed two answer boxes and no try number.
I fixed `templates/index.html` and tested again. The page then showed
the current try number and one answer box.

I kept the decision about when GO is available in `AnswerChecker`.
The Flask route uses that decision to advance to the next problem.
The store keeps attempts by session and problem ID, so the two misses
on 7 × 8 do not use up either try on 6 × 7.

This version uses two preset problems. I deferred editing custom problem
banks and saving progress after the server restarts.