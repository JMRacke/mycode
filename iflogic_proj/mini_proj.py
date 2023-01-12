#!/usr/bin/env python3
"""
    Video Game Trivia Game
    By: Joseph Racke
    Date: 01-11-23
    Files: mini_proj.py, questions.py
"""
import os # Allows to clear screen (on linux i did not write logic for other os)
import questions as q # imports the questions.py with the alias q

questions = q.questions # Stores the questions to a variable because I was too lazy to rewrite the code when I hid the questions in another file

# This function will take in a list of strings in the format str,digit and split it, sort it, and print it
def sortAndPrintList():
    playerscores = ""
    
    try:
        with open('scores.txt', 'r') as scores:
            playerscores = scores.readlines()
    except:
        with open('scores.txt', 'w') as scores:
            scores.close()

    if isinstance(playerscores, list): # Will only print out the high scores if it find a list in the file (prevents going through code if file blank)
        print(f"The current top players are: \n")

        # Variables declared and initialized to a base value
        playerList = []
        scoreList = []
        index = -1
        tempScore = 0
        playerListSorted = []
        scoreListSorted = []

        # Grabs each line, strips off the \n, splits it by the csv and strips again when appending to the lists (in case I missed whitespace surrounding). The digits it converts to an int value to more easily sort
        for line in playerscores:
            line = line.strip()
            temp = line.split(',')
            playerList.append(temp[0].strip())
            scoreList.append(int(temp[1].strip()))
        
        # Iterates through the list
        initialRange = len(playerList) if len(playerList) <= 10 else 10
        for j in range(initialRange):
            for i in range(len(playerList)): # iterates while any values remain in the list
                if scoreList[i] > tempScore: # determines the highest score and saves value and index to variables
                    index = i
                    tempScore = scoreList[i]
            
            # These append the highest score to the sorted list
            playerListSorted.append(playerList.pop(index))
            scoreListSorted.append(scoreList.pop(index))
            
            # resets for next loop
            index = -1
            tempScore = 0

        # Prints out the list
        for i in range(len(playerListSorted)):
            print(f"{str(i+1) + '. ':4}{playerListSorted[i]:16}     {scoreListSorted[i]}") # the :20 adds up to 20 characters after the name so the scores show up aligned

    
# Appends the user's score to the high score list
def addScore(name,score): # Takes in two parameters a string and integer
    with open('scores.txt', 'a') as file:
        file.write(f"{name},{score}\n")


def main(): # Main method
    print(f"Welcome to video game trivia!")

    sortAndPrintList() # Calls the sort and print   
        
    playGame = True;
    userName = input("\nWhat is your name? ") # Gets user's name
    input("Press Enter to start game") # Doesn't use this input, it just pauses here so you can see high scores before clearing and starting game
    os.system('clear')

    while playGame: # Game continues while playGame is True
        
        print(f"You'll be asked some Video Game trivia and at the end be given a score!\n\nGood luck!")
        score = 0
        round = 0

        # Iterates through each question
        for key, value in questions.items():

            # Formats the question and answers
            query = value.get("question")
            print(f"\nQuestion {key}: {query}?")
            for option, answer in value.get("options").items():
                print(f"{option.upper()}- {answer}")

            userAnswer = input(f"Pick a letter: ") # Gets user's guess

            # Logic to determine if what they input was correct or not
            if userAnswer.lower() == value.get("correct"):
                print(f"That is correct! Great Job!")
                score += 100 # cumulates the score
            else:
                print(f"Sorry, the correct answer was: {value.get('correct')}.\n")
            round += 1 # increments the round
        
        # Once all questions are answered it displays the score
        print(f"\nGame Over! Your score was: {score}")

        # Determines if they got all the questions right (100 each question times number of questions)
        if score == round * 100:
            print(f"Congratulations on a perfect game!")
        elif score < round * 100 and score > 0:
            print(f"You got some right! Better luck next time!")
        else:
            print(f"You can't win 'em all. You'll do better next time!\n")

        addScore(userName,score) # Saves their score to the file

        userInput = input("Would you like to play again? (Y/N) ") # Play again (Won't ask name but will jump right into game)
        os.system('clear')

        # If user says no (formatted for ease) then it will set playGame to false and say goodbye, then the while loop will end
        if userInput.upper() == 'N' or userInput.upper() == 'NO':
            playGame = False;
            
            print("Goodbye!")


# Only runs main method if file is executed directly
if __name__ == '__main__':
    main()