#!/usr/bin/env python3

import requests
import json

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    gamesIn = 0
    for game in pokeapi['game_indices']:
        gamesIn += 1
    print(f"This pokemon has appeared in {gamesIn} Pokemon games")

if __name__ == "__main__":
    main()

