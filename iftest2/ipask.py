#!/usr/bin/env python3

ipchk = input("Apply an IP address: ")

if ipchk: # if type != NoneType and string.len() != 0
    print(f"Looks like the IP address was set: {ipchk}") # indented
else: # If no data was input for ipchk
    print(f"You did not provide input.") # indented

# testing outputs for an empty input vs None value
ip = None
print(type(ip))
print(type(ipchk))