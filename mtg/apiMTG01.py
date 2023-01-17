#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # This will not change regardless of the lookup we do

def main():
    """Runtime code"""

    # create resp, which is our request object
    resp = requests.get(f"{API}sets") # this f string reads API + "sets"


    # the .json() method will dump a JSON string into a Python data structure.
    # this is easier than using urllib.request library
    print( resp.json() )

if __name__ == "__main__":
    main()

