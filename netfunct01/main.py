#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""
import crayons
import os

os.system('chmod u+x main.py')

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print(f'{crayons.red("Handshaking")}. .. ... connecting with {ip}') # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')
            # we'll learn to write code that sends cmds to device here
    return None

def devicereboot(deviceips): # takes in a list of IPs
    for ip in deviceips: # iterates through each IP and prints it
        print(f"Connecting to.. {crayons.yellow(ip)}")
    print(f"{crayons.green('REBOOTING NOW!')}") 

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], 
                 "10.2.0.1": ["interface eth1/1", "shutdown"], 
                 "10.3.0.1":["interface eth1/5", "no shutdown"]}

    print("Welcome to the {crayons.blue('Network') Device Command Pusher") # welcome message
    
    # Promopts user for IP addresses and splits into a list
    deviceips = input("Input IP address separated by spaces (eg. 1.1.1.1 0.0.0.0) ")
    deviceips = deviceips.strip().split(" ")
    devicereboot(deviceips) # function call passing in the list

    ## get data set
    print("\nData set found\n") # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

# call our main function
main()

