#!/usr/bin/python3
"""RZFeeser | Alta3 Research"""
from random import randint

class Player:
    
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = []
        for _ in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice

class Cheat_Swapper(Player):
    def cheat(self):
        self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

class Cheat_Mulligan(Player):
    def cheat(self):
        if sum(self.dice) <= 9:
            self.roll()

class Cheat_Additional(Player):
    # Roll an additional die
    def cheat(self):
        self.dice.append(randint(1,6))
        self.dice.sort(reverse=True)
        self.dice = self.dice[0:3]

def main():
    """Runs only if this module is directly run"""
    player1 = Cheat_Additional()

    player1.roll()
    
    print(player1.dice)

    player1.cheat()
    print(player1.dice)

if __name__ == "__main__":
    main()

