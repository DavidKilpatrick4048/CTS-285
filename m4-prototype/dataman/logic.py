"""Answer checking and retry rules shared by any interface."""


class AnswerChecker:
    """Check answers for one problem in a practice session."""

    MAX_TRIES = 2

    def __init__(self, store, session_id, problem_id):
        self.store = store
        self.session_id = session_id
        self.problem_id = problem_id

    def problem_text(self):
        """Return the problem prompt without the correct answer."""
        return self.store.get_problem(self.problem_id)["prompt"]

    def next_try_number(self):
        """Read attempt history to find the next try, or None if finished."""
        attempts = self.store.get_attempts(self.session_id, self.problem_id)
        if len(attempts) >= self.MAX_TRIES or (attempts and attempts[-1]["correct"]):
            return None
        return len(attempts) + 1

    def submit_answer(self, submitted_answer):
        """Record a whole-number answer and return the resulting action."""
        try_number = self.next_try_number()
        if try_number is None:
            return {"outcome": "closed"}

        correct_answer = self.store.get_problem(self.problem_id)["answer"]
        correct = submitted_answer == correct_answer
        self.store.save_attempt({
            "session_id": self.session_id,
            "problem_id": self.problem_id,
            "try_number": try_number,
            "submitted_answer": submitted_answer,
            "correct": correct,
        })

        if correct:
            return {"outcome": "correct", "try_number": try_number}
        if try_number == self.MAX_TRIES:
            return {"outcome": "reveal", "try_number": try_number, "answer": correct_answer}
        return {"outcome": "retry", "try_number": try_number}
