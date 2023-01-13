#!/usr/bin/python3

import random

def main():
    """run time code"""

    player1_dice = []
    player2_dice = []

    for _ in range(3):
        player1_dice.append(random.randint(1,6))
        player2_dice.append(random.randint(1,6))

    print("Player 1 rolled",player1_dice)
    print("Player 2 rolled",player2_dice)

    if sum(player1_dice) == sum(player2_dice):
        print("Draw")
    elif sum(player1_dice) > sum(player2_dice):
        print("Player 1 wins")
    else:
        print("Player 2 wins")

if __name__ == "__main__":
    main()

