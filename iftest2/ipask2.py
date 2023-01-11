#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") # prompt user for input

# If user sets to IP of gateway
if ipchk == "192.168.70.1":
    print(f"Looks like the IP address of the Gateway was set: {ipchk} This is not recommended.") # indented
elif ipchk: # If not NoneType and len() not 0
    print(f"Looks like the IP address was set: {ipchk}") # indented
else: # if data was not provided
    print(f"You did not provide input.") # indented

