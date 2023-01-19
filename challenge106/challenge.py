#1/usr/bin/env python3

URL= "https://opentdb.com/api.php?amount=10&category=11&difficulty=medium&type=multiple"

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import requests
import random

app = Flask(__name__)
correct = ""

@app.route("/trivia")
def trivia():
    data = requests.get(URL).json()
    pydata = data['results']
    qdict = pydata.pop(random.randint(0,(len(pydata)-1)))
    question = qdict['question'] # question to send
    answers = [qdict['correct_answer']]
    answers.extend(qdict['incorrect_answers'])
    letters = 'ABCD'
    options = {}
    opts = []
    for i in range(4):
        rand = random.randint(0,(len(answers)-1))
        options[letters[i]] = answers.pop(rand)
    for let in options:
        opts.append(options.get(let))
    opt1 = opts[0]
    opt2 = opts[1]
    opt3 = opts[2]
    opt4 = opts[3]
    correct = qdict['correct_answer']
    
    return render_template("trivia.html",question = question,opt1 = opt1,opt2=opt2,opt3=opt3,opt4=opt4,correct=qdict['correct_answer'])

@app.route("/submit",methods=["POST"])
def submit():
    print(request.form.get("choice"))
    print(request.form.get("correct"))
    if request.form.get("choice") == request.form.get("correct"):
        return render_template("correct.html")
    else:
        return render_template("wrong.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)