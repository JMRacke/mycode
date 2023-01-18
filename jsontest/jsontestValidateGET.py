#!/usr/bin/python3

import requests
import json

GETURL = "http://validate.jsontest.com/"

def main():
    mydata = {"fruit":["apple","pear"],"vegetable":["carrot"]}

    jsonToValidate = f"json={ json.dumps(mydata).replace(' ', '') }"

    resp = requests.get(f"{GETURL}?{jsonToValidate}")

    respjson = resp.json()

    print(respjson)

    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()

