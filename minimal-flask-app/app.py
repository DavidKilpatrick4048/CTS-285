from secrets import token_hex

from flask import Flask, redirect, render_template, request, session, url_for

from business_logic import check_answer
from dataman.logic import AnswerChecker
from data_store import practice_store

app = Flask(__name__)
app.secret_key = token_hex(32)


def current_checker():
    if "practice_id" not in session:
        session["practice_id"] = token_hex(16)
    return AnswerChecker(practice_store, session["practice_id"], "P1")


@app.get("/")
def index():
    checker = current_checker()
    return render_template(
        "index.html",
        problem=checker.problem_text(),
        next_try=checker.next_try_number(),
        message=session.get("message"),
    )


@app.post("/answer")
def answer():
    checker = current_checker()
    if checker.next_try_number() is not None:
        submitted = request.form.get("answer", type=int)
        if submitted is None:
            session["message"] = "Enter a whole number."
        else:
            session["message"] = check_answer(checker, submitted)
    return redirect(url_for("index"), code=303)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)