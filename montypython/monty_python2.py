#!/usr/bin/env python3

# Initialize variables
round = 0
answer = " "

while round < 3 and answer.title() != 'Brian': # Loops until rounds are met or the user answers correctly
    round += 1 # increment round
    print(f'Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ") # Get user input

    if answer.title() == 'Brian': # executes if correct
        print('Correct') # indent
    elif answer.lower() == 'shrubbery':
        print(f"You gave the super secret answer!")
        break
    elif round==3: # executes if rounds = 3
        print(f"Sorry, the answer was Brian.")
    else: # executes if incorrect answer
        print(f"Sorry! Try again!")