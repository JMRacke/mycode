#!/usr/bin/env python3
import os

questions = {"1":{"question": "How many Grand Theft Auto games have been release?",
                  "options": {
                    "a":"12",
                    "b":"5",
                    "c":"15",
                    "d":"9"
                  },
                  "correct":"c"},
             "2":{"question": "In what year was the classic game 'Lemmings' release?",
                  "options": {
                    "a":"1991",
                    "b":"1995",
                    "c":"1988",
                    "d":"2001"
                  },
                  "correct":"a"},
             "3":{"question": "What color is the enemy seeking turtle shell in 'Super Mario Kart'?",
                  "options": {
                    "a":"yellow",
                    "b":"red",
                    "c":"green",
                    "d":"purple"
                  },
                  "correct":"b"},
             "4":{"question": "In what year was Nintendo founded?",
                  "options": {
                    "a":"1979",
                    "b":"1988",
                    "c":"1965",
                    "d":"1889"
                  },
                  "correct":"d"}
            }
def main():
    print(f"Welcome to video game trivia!")
    while True:
        userName = input("What is your name? ")
        if len(userName) > 25:
            userName = userName[0,24]
            break
        elif userName:
            break    

    playerscores = ""
    
    try:
        with open('scores.txt', 'r') as scores:
            playerscores = scores.readlines()
    except:
        with open('scores.txt', 'w') as scores:
            scores.close()
    
    for line in playerscores:
        print(line)
        
    playGame = True;

    while playGame:
        print(f"You'll be asked some Video Game trivia and at the end be given a score!\n\nGood luck!")
        score = 0
        round = 0
        for key, value in questions.items():
            query = value.get("question")
            print(f"\nQuestion {key}: {query}?")
            for option, answer in value.get("options").items():
                print(f"{option.upper()}- {answer}")

            userAnswer = input(f"Pick a letter: ")

            if userAnswer.lower() == value.get("correct"):
                print(f"That is correct! Great Job!")
                score += 100
            else:
                print(f"Sorry, the correct answer was: {value.get('correct')}.\n")
            round += 1
        
        
        print(f"\nGame Over! Your score was: {score}")
        if score == round * 100:
            print(f"Congratulations on a perfect game!")
        elif score < round * 100 and score > 0:
            print(f"You got some right! Better luck next time!")
        else:
            print(f"You can't win 'em all. You'll do better next time!\n")

        userInput = input("Would you like to play again? (Y/N) ")
        os.system('clear')
        if userInput.upper() == 'N' or userInput.upper() == 'NO':
            playGame = False;
            print("Goodbye!")

main()