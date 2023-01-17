#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()

        house = requests.get(got_dj['allegiances'][0])
        house_js = house.json()

        print(f"{got_dj['name']} of {house_js['name']}")
        books_list = []
        for book in got_dj['books']:
            bookget = requests.get(book)
            bookjs = bookget.json()
            books_list.append(bookjs['name'])
        print(f"They appeared in the following books\n{books_list}")

if __name__ == "__main__":
        main()

