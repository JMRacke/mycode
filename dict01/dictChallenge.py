#!/usr/etc/env python3

def main():

    marvelchars= {
    "Starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

    "Mystique":
        {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

    "Hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
    }
    
    another = True;
    while another:
        choice = input(" Which character do you want to know about? (Starlord, Mystique, Hulk) ")
        character = marvelchars.get(choice.title())
        choice2 = input(" What statistic do you want to know about? (real name, powers, archenemy) ")
        stats = character.get(choice2.lower())

        print(f"{choice.title()}'s {choice2.lower()} is: {stats.title()}")

        another = eval(input("Try another character/stat? (True/False) "))

main()
