#!/usr/bin/env python3

# Save user input to variable
hostname = input("What value should we set for hostname? ")

# If the hostname is mtg this is the exepected value so it prints the following lines
if hostname.lower() == "mtg":
    print(f"The hostname was found to be {hostname.lower()}.")
    print(f"hostname matches expected config")

# Exit console print so the user knows the program exited properly without error
print(f"Exiting the script")
