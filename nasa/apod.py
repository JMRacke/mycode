#!/usr/bin/python3
import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## Grab API key from file
    with open("/home/student/mycode/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove whitespace and \n from the file read and 
    ## save as string in format used for API
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## Call API with our key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode the JSON to a Python data structure (dict)
    apod = json.loads(apodread.decode("utf-8"))

    ## Display our pythonic data
    print("\n\nConverted Python Data")
    print(apod)
    print()
    print(apod['title'] + "\n")
    print(apod['date'] + "\n")
    print(apod['explanation'] + "\n")
    print(apod["url"])

if __name__ == "__main__":
    main()

