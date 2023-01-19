#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import random
import html


URL= "https://opentdb.com/api.php?amount=10&category=11&difficulty=medium&type=multiple" 

def ask_question(question):
    answers = [question['correct_answer']]
    answers.extend(question['incorrect_answers'])
    letters = 'ABCD'
    options = {}
    print(html.unescape(question['question']))
    for i in range(4):
        rand = random.randint(0,(len(answers)-1))
        options[letters[i]] = answers.pop(rand)
    for let in options:
        print(let + ".",options.get(let))
    userAns = input("What is the correct answer (answer with letter)? ") 
    userAns = userAns[0]
    if options[userAns] == question['correct_answer']:
        print("That is correct!\n\n")
    else:
        print(f"WRONG!!! The correct answer was {question['correct_answer']}.\n\n")

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    pydata = data['results']

    while pydata:
        ask_question(pydata.pop(0))


if __name__ == "__main__":
    main()

