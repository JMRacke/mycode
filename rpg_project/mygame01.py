#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
from rooms import rooms
from Player import Player


# start the player in the Hall


# Create a player
player1 = Player()


def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go <direction> - You go that direction
      get <item> - You pick up that item
      help - Displays these commands
      exit - Quits program
      inventory - Display items in inventory
    --------
    Objective:
      Escape the house with they key and potion
      Beware of monsters!
    ''')

def showStatus(currentRoom):
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # Description of room is displayed
    print(rooms[currentRoom]['description'])
    # print what the player is carrying
    # print('Inventory:', player1.inventory)
    # # check if there's an item in the room, if so print it
    # if "items" in rooms[currentRoom]:
    #     for item in rooms[currentRoom]['items']:
    #         print(f"You see a {item}.")
    print("---------------------------")

def main():
    # Shows what the user can do
    showInstructions()
    currentRoom = 'Hall'
    # breaking this while loop means the game is over
    while True:
        if rooms == None:
            break
        showStatus(currentRoom)

        ## If a player enters a room with a monster
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print("A monster has got you... GAME OVER!")
            break

        ## Define how a player can win
        if currentRoom == 'Garden' and 'key' in player1.inventory and 'potion' in player1.inventory:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break


        # the player MUST type something in
        # otherwise input will keep asking
        userInput = ''
        while userInput == '':  
            userInput = input('>')

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]          
        userInput = userInput.lower().split(" ", 1)

        #if they type 'go' first
        if userInput[0] == 'go':
            #check that they are allowed wherever they want to go
            if userInput[1] in rooms[currentRoom]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom][userInput[1]]
                player1.steps += 1
            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')
        elif userInput[0] == 'get' :
            # make two checks:
            # 1. if the current room contains an item
            # 2. if the item in the room matches the item the player wishes to get
            if "items" in rooms[currentRoom] and userInput[1] in rooms[currentRoom]['items']:
                #add the item to their inventory
                player1.inventory.append(userInput[1])
                #display a helpful message
                print(userInput[1] + ' got!')
                #delete the item key:value pair from the room's dictionary
                rooms[currentRoom]['items'].pop(rooms[currentRoom]['items'].index(userInput[1]))
            # if there's no item in the room or the item doesn't match
            else:
                #tell them they can't get it
                print('Can\'t get ' + userInput[1] + '!')
        elif userInput[0] == 'help':
            showInstructions()
        elif userInput[0] == 'inventory':
            print(player1.inventory)
        elif userInput[0] == 'exit':
            print("Exiting the game.")
            exit()
        else:
            print("I don't know what you mean.")
        


if __name__ == "__main__":
    main()