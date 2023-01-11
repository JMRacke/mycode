#!/usr/bin/env python3
import random # needed to use random function
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

def main():
    num = random.randint(1,100) # Gets a random number from 1(inclusive) to 100(inclusive)


    rounds,guess = 0 # Sets both variables

    while rounds < 5 and guess != num:
        guess = input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        # determines if guess's value contains only 0-9s, if not, it'll make the user input again.
        if guess.isdigit():
            guess= int(guess)
        else:
            continue # skips following lines and goes back to beginning of while loop


        if guess > num:
            print("Too high!")
            rounds += 1
        elif guess < num:
            print("Too low!")
            rounds += 1
        else:
            print("Correct!")

    print("Exiting program.")

if __name__ == "__main__":
    main()