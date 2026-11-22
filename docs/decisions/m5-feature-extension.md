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