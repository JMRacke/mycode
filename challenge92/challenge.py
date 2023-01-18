#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    lat = resp['iss_position']['latitude']
    lon = resp['iss_position']['longitude']
    coords = (lat,lon)
    location = rg.search(coords,verbose=False)
    city = location[0]['name']
    area = location[0]['cc']
    print("CURRENT LOCATION OF THE ISS:")
    print(f"Lon: {lon}")
    print(f"Lat: {lat}")
    print(f"City/Country: {city},{area}")

if __name__ == "__main__":
    main()

