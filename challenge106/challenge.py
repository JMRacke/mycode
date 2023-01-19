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

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/trivlogin",methods=["POST"])
def trivlogin():
    return redirect(url_for("trivia",name=request.form.get("nm")))

@app.route("/correct")
def correct():
    return render_template("correct.html") 

@app.route("/incorrect")
def incorrect():
    return render_template("wrong.html") 

@app.route("/trivia")
def trivia():
    url= f"https://opentdb.com/api.php?amount=10&category={random.randint(1,31)}&difficulty=medium&type=multiple"
    data = requests.get(url).json()
    pydata = data['results']
    qdict = pydata.pop(random.randint(0,(len(pydata)-1)))
    question = html.unescape(qdict['question']) # question to send
    answers = [qdict['correct_answer']]
    answers.extend(qdict['incorrect_answers'])
    letters = 'ABCD'
    options = {}
    opts = []
    for i in range(4):
        rand = random.randint(0,(len(answers)-1))
        options[letters[i]] = html.unescape(answers.pop(rand))
    for let in options:
        opts.append(options.get(let))
    opt1 = opts[0]
    opt2 = opts[1]
    opt3 = opts[2]
    opt4 = opts[3]
    correct = qdict['correct_answer']
    
    return render_template("trivia.html",name = request.args.get('name'),question = question,opt1 = opt1,opt2=opt2,opt3=opt3,opt4=opt4,correct=qdict['correct_answer'])

@app.route("/submit",methods=["POST"])
def submit():
    print(request.form.get("choice"))
    print(request.form.get("correct"))
    if request.form.get("choice") == request.form.get("correct"):
        return redirect(url_for("correct"))
    else:
        return redirect(url_for("incorrect"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)