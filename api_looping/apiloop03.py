#!/usr/bin/env python3

import requests
import json

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    gamesIn = len(pokeapi['game_indices'])
    print(f"This pokemon has appeared in {gamesIn} Pokemon games")

if __name__ == "__main__":
    main()

