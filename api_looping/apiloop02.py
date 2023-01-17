#!/usr/bin/env python3

import requests
import json

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(f"{pokeapi['name']}'s moves are: ")
    for move in pokeapi['moves']:
        print(f"{move['move']['name']}, ",end="")

if __name__ == "__main__":
    main()

