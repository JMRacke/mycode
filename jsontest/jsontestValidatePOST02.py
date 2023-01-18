#!/usr/bin/env python3

import requests

TIMEURL = "http://date.jsontest.com"
IPURL = "http://ip.jsontest.com"
VALIDURL = "http://validate.jsontest.com/"

def main():
    resp = requests.get(TIMEURL)

    time = resp.json()

    mytime = time["time"].replace(" ","").replace(":","-")
    

    resp = requests.get(IPURL)
    myip = resp.json()
    myip = myip["ip"]

    with open("myservers.txt", "r") as myfile:
        mysvrs = myfile.readlines()

    jsontotest = {}
    jsontotest["time"] = mytime
    jsontotest["ip"] = myip
    jsontotest["mysvrs"]= mysvrs
    print(jsontotest)

    mydata = {}
    mydata["json"] = str(jsontotest)

    resp = requests.post(VALIDURL, data=mydata)

    respjson = resp.json()

    print(respjson)

    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
