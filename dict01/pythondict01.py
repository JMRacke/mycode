#!/usr/bin/env python3
"""Understanding dictionaries
    {key: value, key: value, ...} """

def main():
    # Runtime Function

    ## Create a dictionary with 4 key:value pairs
    switch = {"hostname":"sw1", "ip": "10.0.1.1","version":"1.2","vendor":"cisco"}

    ## Display the entire dictionary
    print(switch)

    ## Prove that switch is indeed a dictionary
    print(type(switch))

    ## Display parts of the dictionary
    print( switch["hostname"] )  # Displays "sw1"
    print( switch["ip"] )        # Displays "10.0.1.1"

    ## Request a 'fake' key
    print( switch["lynx"] ) # This will cause the program to FAIL

    ## request a 'fake' key
    # print( switch["lynx"] )   # Be sure to comment out this line,
                                # or your program will CONTINUE to fail!
                                # if a KEY is requested that does not exist,
                                # an ERROR will be thrown!

    ## request a 'fake' key with .get() method
    print( "First test - .get()" )
    print( switch.get("lynx") ) # alternative to switch["lynx"]
    #print(switch.get("lynx", None)) # this is what is actually being run...
                                     # by default dict.get() returns "None"

    # if you want to customize what is returned when the key is not found
    print( "Second test - .get()" )
    print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

    print( "Third test - .get()" )
    print( switch.get("version") ) # alternative to switch['version']
                                   # this key exists, so it will return a value of "1.2"


# Will only call the function if the file is directly executed and not called by another file
if __name__ == "__main__":
    main()
