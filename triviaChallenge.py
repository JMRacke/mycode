#!/usr/bin/env python3
import html # Allows us to use the html library

# Bank of trivia questions
trivia = {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():
    incorrect_answer = trivia.get('incorrect_answers') # stores incorrect answers to list

    print(trivia.get("question"),'\n') # prints out the question from the trivia dictionary

    # Formats from html to unicode and prints each option
    print(f"A: {html.unescape(trivia.get('correct_answer'))}")
    print(f"B: {html.unescape(incorrect_answer[0])}")
    print(f"C: {html.unescape(incorrect_answer[1])}")
    print(f"D: {html.unescape(incorrect_answer[2])}")

    userInput = input("\nPick a choice: ") # Gets the user's answer


    if userInput.upper() == 'A':
        print("Correct!")
    else:
        print("WRONG!!!")

# Only runs main() if method is directly run
if __name__ == '__main__':
    main()