#!/usr/bin/python3

import requests

# define URL to use
IPURL = "http://ip.jsontest.com/"

def main():
    # use requests to send HTTP GET
    resp = requests.get(IPURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    print(respjson)

    print(f"The current WAN IP is --> {respjson['ip']}")

if __name__ == "__main__":
    main()
