"""In-memory data layer for the Module 4 prototype."""


class MemoryStore:
    """Keep a sample problem and attempt records for one program run."""

    def __init__(self):
        self._problems = {"P1": {"prompt": "7 x 8", "answer": 56}}
        self._attempts = []

    def get_problem(self, problem_id):
        """Read one problem by ID."""
        return self._problems[problem_id].copy()

    def get_attempts(self, session_id, problem_id):
        """Return attempts for this session and problem in submission order."""
        return [
            attempt.copy()
            for attempt in self._attempts
            if attempt["session_id"] == session_id and attempt["problem_id"] == problem_id
        ]

    def save_attempt(self, attempt):
        """Store a copy of a numbered attempt."""
        self._attempts.append(attempt.copy())
