#!/usr/bin/env python3
"""
    Video Game Trivia Game
    By: Joseph Racke
    Date: 01-11-23
    Files: mini_proj.py, questions.py
"""
import os # Allows to clear screen (on linux i did not write logic for other os)
import questions as q # imports the questions.py with the alias q

questions = q.questions # Stores the questions from the question module to a variable


def sortandprintlist():
    """
        This function will take in a list of strings in the format str,digit
        and split it, sort it, and print it
    """
    playerscores = ""

    try:
        with open('scores.txt', 'r', encoding="utf-8") as scores:
            playerscores = scores.readlines() # Reads all lines and stores as a list of strings
    except FileNotFoundError as err:
        print(f"Error: {err}\nCreating high score file...")
        with open('scores.txt', 'w', encoding="utf-8") as scores:
            scores.close()

    # Will only print out the high scores if it finds a list in the file
    # (prevents going through code if file blank)
    if isinstance(playerscores, list):
        print("The current top players are: \n")

        # Variables declared and initialized to a base value
        playerlist = []
        scorelist = []
        index = -1
        tempscore = 0
        playerlistsorted = []
        scorelistsorted = []

        # Grabs each line, strips off the \n, splits it by the csv and strips again when appending
        # to the lists (in case I missed whitespace surrounding). The digits it converts to an int
        # value to more easily sort
        for line in playerscores:
            line = line.strip()
            temp = line.split(',')
            playerlist.append(temp[0].strip())
            scorelist.append(int(temp[1].strip()))

        # Iterates through the list
        initialrange = len(playerlist) if len(playerlist) <= 10 else 10
        for _ in range(initialrange):
            for i in range(len(playerlist)): # iterates while any values remain in the list
                # determines the highest score and saves value and index to variables
                if scorelist[i] > tempscore:
                    index = i
                    tempscore = scorelist[i]

            # These append the highest score to the sorted list
            playerlistsorted.append(playerlist.pop(index))
            scorelistsorted.append(scorelist.pop(index))

            # resets for next loop
            index = -1
            tempscore = 0

        # Prints out the list
        i = 0
        for player in playerlistsorted:
            # the :20 adds up to 20 characters after the name so the scores show up aligned
            print(f"{str(i+1) + '. ':4}{player:21}{scorelistsorted[i]}")
            i += 1


def addscore(name,score): # Takes in two parameters a string and integer
    """Appends the user's score to the high score list"""
    with open('scores.txt', 'a',encoding="utf-8") as file:
        file.write(f"{name},{score}\n")


def main():
    """Main method"""
    print("Welcome to video game trivia!")

    sortandprintlist() # Calls the sort and print

    playgame = True
    username = input("\nWhat is your name? ") # Gets user's name
    input("Press Enter to start game")
    os.system('clear')

    while playgame: # Game continues while playGame is True

        print("You'll be asked some Video Game trivia and at the end be given a score!"
                + "\n\nGood luck!")
        score = 0
        currentround = 0

        # Iterates through each question
        for key, value in questions.items():

            # Formats the question and answers
            query = value.get("question")
            print(f"\nQuestion {key}: {query}")
            for option, answer in value.get("options").items():
                print(f"{option.upper()}- {answer}")

            useranswer = input("Pick a letter: ") # Gets user's guess

            # Logic to determine if what they input was correct or not
            if useranswer.lower() == value.get("correct"):
                print("That is correct! Great Job!")
                score += 100 # cumulates the score
            else:
                print(f"Sorry, the correct answer was: {value.get('correct')}.\n")
            currentround += 1 # increments the round

        # Once all questions are answered it displays the score
        print(f"\nGame Over! Your score was: {score}")

        # Determines if they got all the questions right (100 each question * number of questions)
        if score == currentround * 100:
            print("Congratulations on a perfect game!")
        elif score > 0:
            print("You got some right! Better luck next time!")
        else:
            print("You can't win 'em all. You'll do better next time!\n")

        addscore(username,score) # Saves their score to the file

        # Play again (Won't ask name but will jump right into game)
        userinput = input("Would you like to play again? (Y/N) ")
        os.system('clear')

        # If user says no (formatted for ease) then it will set playGame to false and say
        # goodbye, then the while loop will end
        if userinput.upper() == 'N' or userinput.upper() == 'NO':
            playgame = False

            print("Goodbye!")


# Only runs main method if file is executed directly
if __name__ == '__main__':
    main()
