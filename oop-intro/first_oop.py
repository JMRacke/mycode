#!/usr/bin/python3
"""RZFeeser | Alta3 Research"""
from random import randint

class Player:
    NUM = 0
    # Constructor for player
    def __init__(self):
        self.dice = []

    # function to roll dice and add to list of player's dice
    def roll(self):
        self.dice = []
        for _ in range(3):
            self.dice.append(randint(1,6))
    
    # returns the list of dice
    def get_dice(self):
        return self.dice

def main():
    """Called at run time"""

    # Create each player object from the Player class
    player1 = Player()
    player2 = Player()

    # player objects can use their method "roll"
    player1.roll()
    player2.roll()

    # the f-string is simply a "fill in the {} with the value inside"
    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    # determine which player won
    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw!")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == "__main__":
    main()
