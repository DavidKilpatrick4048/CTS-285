def check_answer(checker, submitted):
    result = checker.submit_answer(submitted)
    action = result["outcome"]

    if action == "reveal":
        return f"The correct answer is {result['answer']}."

    messages = {
        "retry": "Incorrect. You have one try left.",
        "correct": "Correct.",
        "closed": "This round is complete.",
    }
    return messages[action]