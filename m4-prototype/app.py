"""Text interface for the Module 4 DataMan Answer Checker."""

from dataman.logic import AnswerChecker
from dataman.store import MemoryStore


def run_practice(checker):
    """Read answers and display the results returned by the checker."""
    print("DataMan Answer Checker")
    print(f"Problem: {checker.problem_text()}")

    try_number = checker.next_try_number()
    while try_number is not None:
        try:
            answer = int(input(f"Try {try_number} of {checker.MAX_TRIES}. Your answer: "))
        except ValueError:
            print("Enter a whole number.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nPractice ended.")
            return

        result = checker.submit_answer(answer)
        if result["outcome"] == "correct":
            print("Correct.")
        elif result["outcome"] == "retry":
            print("EEE - Incorrect. One try left.")
            print(f"Problem: {checker.problem_text()}")
        elif result["outcome"] == "reveal":
            print(f"EEE - Incorrect. The correct answer is {result['answer']}.")

        try_number = checker.next_try_number()

    print("Practice complete.")


def main():
    """Start a fresh practice session with one sample problem."""
    store = MemoryStore()
    checker = AnswerChecker(store, session_id="demo-session", problem_id="P1")
    run_practice(checker)


if __name__ == "__main__":
    main()
