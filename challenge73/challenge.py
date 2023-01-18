#!/usr/bin/env python3

def main():
    """Challenge shrunk from many lines w/ if-elif to a few"""
    usr_name = input("Please enter your name:\n>").title()  
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    animals = [ 'Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep',]
    description = [ 'creative, resilient, gentle, mild-mannered, and shy.','sharp, smart, curious, and mischievious.','hardworking, resourceful, courageous, and talented.','loyal, honest, cautious, and kind.','symbol of wealth, honesty, and practicality.','artistic, sociable, industrious, charming, and intelligent.','strong, thorough, determined, loyal, and reliable.','courageous, enthusiastic, confident, charismatic, and a leader.','vigilant, witty, quick-minded, and ingenious.','talented, powerful, lucky, and successful.','wise, like to work alone, and determined.','animated, active, and energetic.',]
    print(f"{usr_name} your zodiac sign is {animals[usr_date % 12]}, you are {description[usr_date % 12]}")

if __name__ == "__main__":
    main()
