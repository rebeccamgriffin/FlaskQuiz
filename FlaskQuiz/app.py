import os
from flask import Flask, render_template, request
app = Flask(__name__)

quiz_host = os.environ.get('FLASK_HOST')
quiz_port = os.environ.get('FLASK_PORT')

questions = [
    {
        "id": "1",
        "question": "What is the Capital of Syria?",
        "answers": ["a) Beirut", "b) Damascus", "c) Baghdad"],
        "correct": "b) Damascus"
    },
    {
        "id": "2",
        "question": "What is the square root of Pi?",
        "answers": ["a) 1.7724", "b) 1.6487", "c) 1.7872"],
        "correct": "a) 1.7724"
    },
    {
        "id": "3",
        "question": "How many counties are there in England?",
        "answers": ["a) 52", "b) 48", "c) 45"],
        "correct": "b) 48"
    }
]


@app.route("/quiz", methods=['POST', 'GET'])
def quiz():
    if request.method == 'GET':
        return render_template("index.html", data=questions)
    else:
        result = 0
        total = 0
        for question in questions:
            if request.form[question.get('id')] == question.get('correct'):
                result += 1
            total += 1
        return render_template('results.html', total=total, result=result)


if __name__ == "__main__":
    app.run(host=quiz_host, port=quiz_port)
