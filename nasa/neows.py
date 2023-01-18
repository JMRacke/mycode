#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/mycode/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = input("Please enter a start date int the format YYYY-MM-DD:")
    startdate = "start_date=" + startdate.strip("\n")

    ## the value below is not being used in this
    ## version of the script
    enddate = input("Enter an end date if you would like (same format) or just press enter")
    if len(enddate.strip("\n")) == 12:
        enddate = "&end_date=" + enddate.strip("\n")
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + f"{enddate if len(enddate)>12 else ''}"  + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

