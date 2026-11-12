# DataMan Module 4 Text Prototype

This prototype tests **US-01 (immediate answer feedback)** and **US-02 (one retry after an incorrect answer)** with a single problem, 7 × 8. See the [Design Studio investigation record](evidence/m4-design-investigation-record.md) and [AI prompt log](prompts.md).

## Run it

From this folder, run the following with Python 3. On Windows, you can use `py` in place of `python3`. No packages need to be installed.

```sh
python3 app.py
python3 -m unittest discover -s tests -v
```

Run `app.py` again for each terminal example below.

## Design question and state

**What does DataMan need to remember to distinguish Try 1 from Try 2, decide when to allow a retry or reveal the answer, and know when a problem is finished?** The Studio review sharpened the question: can the checker recover the next try if the interface no longer holds the first result?

The store keeps each submitted answer and its correctness in a numbered attempt record linked to the session and problem. The checker reads that history to find the next try. No saved attempts means Try 1. A single miss means Try 2 with the answer still hidden. A correct attempt or two misses closes the problem.

| Layer | Responsibility |
| --- | --- |
| [Text interface](app.py) | Prompts for a whole number and displays the problem, try number, feedback, and completion. |
| [Business logic](dataman/logic.py) | Evaluates answers, records attempts, and decides whether to retry, reveal the answer, or finish. It can run without the terminal. |
| [Stubbed data](dataman/store.py) | Supplies a sample problem and stores attempts in memory through `get_problem`, `get_attempts`, and `save_attempt`. |

## Observed test results

| Input for 7 × 8 | Result observed in the terminal | Acceptance criteria exercised |
| --- | --- | --- |
| `56` | Displayed **Correct.** after submission and finished. | US-01 / FR-02: feedback without another action. |
| `54`, then `56` | First miss displayed **EEE - Incorrect. One try left.** The same problem appeared at Try 2 without revealing 56. The retry displayed **Correct.** and finished. | US-01 and US-02 / FR-02, FR-03, NFR-03: incorrect feedback, one retry, and consistent correct feedback. |
| `54`, then `55` | First miss offered the retry. Second miss displayed **EEE - Incorrect. The correct answer is 56.** The program finished without a Try 3 prompt. | US-02 / FR-03: reveal after the second miss and stop. |
| `abc`, then `54`, then `56` | Prompted for a whole number and remained on Try 1 until a number was entered. The retry then worked as above. | Prototype assumption: invalid input does not consume a try. |

All five [logic tests](tests/test_answer_checker.py) passed. They confirmed that both attempts were saved separately and that the checker itself refused a third submission. After recording `54` on Try 1, a new checker using the same store, session, and problem started at Try 2. A different session or a fresh store started at Try 1. This shows the next try comes from the saved attempt history.

## Decision and limits

The tests supported the Studio revision: keep attempt history outside the text interface and let shared logic decide what happens next. No further design revision was needed for the in-process slice.

The sample problem and session ID are fixtures. Exiting the process clears the in-memory history. To resume after exit, DataMan still needs durable storage and an answer to **Q-02**: how to match a returning learner to the right unfinished session. Feedback appeared on submission, but **Q-03** still needs a measurable response-time limit. Scoring, Memory Bank and curator retrieval, and Flask are outside this prototype.
