#!/usr/bin/env python3

import requests
import shutil

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    # Saves the url from the dictionary to a string
    link_url=pokeapi['sprites']['front_default']
    # Uses the creature's name to create a .png file name string
    fileurl = f"{pokeapi['name'].title()}.png"

    # Uses request to get the image
    imgpayload = requests.get(link_url, stream=True)

    # Determines if it successfully got the img based on the request status code
    if imgpayload.status_code == 200:
        # Opens the .png file name in write-binary mode
        with open(fileurl,'wb') as wfile:
            # Writes the raw binary image data to the file
            shutil.copyfileobj(imgpayload.raw,wfile)
        print("Success!")
    else:
        # Prints if something went wrong w/ the get
        print("Something went wrong!")


if __name__ == "__main__":
    main()

