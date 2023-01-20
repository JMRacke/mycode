#1/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
import requests
import random
import html


app = Flask(__name__)
CORRECT_ANSWER = ""

@app.route("/correct")
def correct():
    return render_template("correct.html") 

@app.route("/incorrect")
def incorrect():
    return render_template("wrong.html") 

@app.route("/trivia")
def trivia():
    global CORRECT_ANSWER
    url= f"https://opentdb.com/api.php?amount=10"
    data = requests.get(url).json()
    pydata = data['results']
    qdict = pydata[3]
    question = html.unescape(qdict['question']) # question to send
    CORRECT_ANSWER = qdict['correct_answer']
    answers = [qdict['correct_answer']]
    answers.extend(qdict['incorrect_answers'])
    letters = 'ABCD'
    options = {}
    opts = []
    for i in range(4):
        if len(answers) > 1:
            rand = random.randint(0,(len(answers)-1))
        else:
            rand = 0
        if len(answers) > 0:
            options[letters[i]] = html.unescape(answers.pop(rand))
    for let in options:
        opts.append(options.get(let))
    
    correct = qdict['correct_answer']
    
    return render_template("trivia.html",question = question,opts = opts)

@app.route("/submit",methods=["POST"])
def submit():
    global CORRECT_ANSWER
    print(request.form.get("answer"))
    print(CORRECT_ANSWER)
    if request.form.get("answer") == CORRECT_ANSWER:
        return redirect(url_for("correct"))
    else:
        return redirect(url_for("incorrect"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)