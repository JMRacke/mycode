#1/usr/bin/env python3
"""
    Trivia Game Challenge Part 2
    Joseph Racke
    01-20-2023

    Took the Trivia Game Challenge from 103 and:
    -Made a single function that handles both the GET of the questions and the POST
    of the answer submission
    -Made a single render template for the Answer result vice separate correct/incorrect
    -Added import for sessions to keep track of user and score
    -Created a login for the user

    Future TODOs
    - Change the game to have the user keep going until they get a question wrong
    - Tally their score and save it to a file
    - Display the high scores
    - Stylize the HTML
"""

# Required imports
from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
from flask import url_for
from flask import session
import requests
import random
import html


app = Flask(__name__) # server app
app.secret_key = "Hutch is the Best Python Instructor!" # Required for session to work
CORRECT_ANSWER = "" # Keeps the variable to be used for multiple function calls
# HTTP route for the user login
@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":
        session["user"] = request.form.get("user") # Store user input to their "user" name
        session["score"] = 0 # Sets their initial score to 0
        return redirect(url_for("trivia")) # Logs them in and redirects to the trivia page
    
    # If the method is a 'GET' it returns the login page
    return """
   <form action = "" method = "post">
      <p><input type = text name = user></p>
      <p><input type = submit value = Login></p>
   </form>"""

# Main route to be executed
# Handles both the GET to display trivia and the POST of the user's answer
@app.route("/trivia",methods = ["GET","POST"])
def trivia():
    global CORRECT_ANSWER
    if request.method == "GET":

        # Checks if the user is logged in
        if "user" in session:
            
            # API call to open trivia db for get 10 random questions
            url= f"https://opentdb.com/api.php?amount=10"
            data = requests.get(url).json()
            pydata = data['results']

            # Get a random question from the bank
            qdict = pydata[random.randint(0,8)]

            question = html.unescape(qdict['question']) # question to send

            CORRECT_ANSWER = qdict['correct_answer'] # correct answer
            answers = [qdict['correct_answer']]
            answers.extend(qdict['incorrect_answers']) # adds the incorrect 

            # Iterates through the answers and adds them to list and formats them
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

            # Render the page using the trivia template and passing the parameters            
            return render_template("trivia.html",question = question,
                                    opts = opts,user=session["user"],
                                    score = session["score"])
        
        # Returns this if user is not logged in
        return "You are not logged in <br><a href = '/login'></b>" + \
                    "click here to log in</b></a>"

    # if request.method is "POST"
    check_answer = False
    if request.form.get("answer") == CORRECT_ANSWER:
        check_answer = True
        session["score"] += 100

    return render_template("result.html",ans = check_answer,score=session["score"])


    

# Boots up the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)