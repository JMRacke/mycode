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
    # This guy swaps his final die to a 6
    def cheat(self):
        self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):
    # with loaded dice, they all tip one higher than they should
    def cheat(self):
        i = 0
        while i < len(self.dice):
            if self.dice[i] < 6:
                self.dice[i] += 1
            i += 1

class Cheat_Mulligan(Player):
    # If the total from roll is < 9 the cheater will roll again
    def cheat(self):
        if sum(self.dice) <= 9:
            self.roll()

class Cheat_Additional(Player):
    # Roll an additional die
    def cheat(self):
        self.dice.append(randint(1,6))
        self.dice.sort(reverse=True)
        self.dice = self.dice[0:3]

class Cheat_Weighted(Player):
    # First die is weighted so it can't be < 3
    def cheat(self):
        if self.dice[0] < 3:
            self.dice[0] = 3

class Cheat_Saboteur(Player):
    # This cheater stealthfully swaps out any high rolling dice for low
    # ones for their opponent
    def cheat(self,player):
        player.dice = [randint(1,3) for i in range(3)]

def main():
    """Runs only if this module is directly run"""
    player1 = Cheat_Saboteur()
    player2 = Player()
    # roll dice and show what it would be if they dont cheat
    player2.roll() 
    print(player2.dice)

    # execute their cheat method to manipulate the di(c)e
    player1.cheat(player2)
    print(player2.dice)

if __name__ == "__main__":
    main()

