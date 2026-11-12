"""Exercise the two-attempt rules without a text interface."""

import unittest

from dataman.logic import AnswerChecker
from dataman.store import MemoryStore


class AnswerCheckerTests(unittest.TestCase):
    def setUp(self):
        self.store = MemoryStore()
        self.checker = AnswerChecker(self.store, "test-session", "P1")

    def attempt_history(self):
        """Read each try number, submitted answer, and outcome in order."""
        return [
            (row["try_number"], row["submitted_answer"], row["correct"])
            for row in self.store.get_attempts("test-session", "P1")
        ]

    def test_correct_first_answer_ends_problem(self):
        result = self.checker.submit_answer(56)
        self.assertEqual(result["outcome"], "correct")
        self.assertIsNone(self.checker.next_try_number())
        self.assertEqual(self.attempt_history(), [(1, 56, True)])
        self.assertEqual(self.checker.submit_answer(54)["outcome"], "closed")
        self.assertEqual(len(self.attempt_history()), 1)

    def test_wrong_then_correct_preserves_both_tries(self):
        first = self.checker.submit_answer(54)
        self.assertEqual(first["outcome"], "retry")
        self.assertNotIn("answer", first)
        self.assertEqual(self.checker.next_try_number(), 2)
        self.assertEqual(self.checker.problem_text(), "7 x 8")

        second = self.checker.submit_answer(56)
        self.assertEqual(second["outcome"], "correct")
        self.assertIsNone(self.checker.next_try_number())
        self.assertEqual(self.attempt_history(), [(1, 54, False), (2, 56, True)])

    def test_two_misses_reveal_and_block_third_submission(self):
        first = self.checker.submit_answer(54)
        self.assertNotIn("answer", first)

        second = self.checker.submit_answer(55)
        self.assertEqual(second["outcome"], "reveal")
        self.assertEqual(second["answer"], 56)
        self.assertIsNone(self.checker.next_try_number())
        self.assertEqual(self.checker.submit_answer(56)["outcome"], "closed")
        self.assertEqual(self.attempt_history(), [(1, 54, False), (2, 55, False)])

    def test_new_checker_uses_saved_history_for_the_same_session(self):
        self.checker.submit_answer(54)
        reopened = AnswerChecker(self.store, "test-session", "P1")
        other_session = AnswerChecker(self.store, "other-session", "P1")

        self.assertEqual(reopened.next_try_number(), 2)
        self.assertEqual(other_session.next_try_number(), 1)
        self.assertEqual(reopened.submit_answer(56)["outcome"], "correct")
        self.assertEqual(self.attempt_history(), [(1, 54, False), (2, 56, True)])

    def test_fresh_store_does_not_resume_an_old_session(self):
        self.checker.submit_answer(54)
        restarted = AnswerChecker(MemoryStore(), "test-session", "P1")
        self.assertEqual(restarted.next_try_number(), 1)


if __name__ == "__main__":
    unittest.main()
