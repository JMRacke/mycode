#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
from rooms import rooms
from Player import Player


# start the player in the Hall


# Create a player
PLAYER_1 = Player()
CURRENT_ROOM = 'Lobby'

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print(f'''
    RPG Game
    ========
    Commands:
      go <direction> - You go that direction
      get <item> - You pick up that item
      help - Displays these commands
      exit - Quits program
      inventory - Display items in inventory
      {'inspect - search for anything out of place' if CURRENT_ROOM == 'Study' else ''}
      {'push - push a button' if CURRENT_ROOM == 'Study' else ''}
    --------
    Objective:
     Survive the haunted mansion.
     Find the [diamond] and a way to escape!
     Beware of monsters! 
    ''')

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    # print('You are in the ' + currentRoom)
    # Description of room is displayed
    print(rooms[CURRENT_ROOM]['description'])
    # print what the player is carrying
    # print('Inventory:', player1.inventory)
    # # check if there's an item in the room, if so print it
    # if "items" in rooms[currentRoom]:
    #     for item in rooms[currentRoom]['items']:
    #         print(f"You see a {item}.")
    print("---------------------------")
    print(f"You've taken {PLAYER_1.steps} {'steps' if PLAYER_1.steps != 1 else 'step'} so far.")
    print("---------------------------")

def main():
    # Shows what the user can do
    global CURRENT_ROOM, PLAYER_1
    showInstructions()
    
    CURRENT_ROOM = 'Lobby'
    # breaking this while loop means the game is over
    while True:
        if rooms == None:
            break
        showStatus()

        ## If a player enters a room with a monster
        if 'items' in rooms[CURRENT_ROOM] and 'monster' in rooms[CURRENT_ROOM]['items']:
            if 'cleaver' in PLAYER_1.inventory:
               rooms[CURRENT_ROOM]['items'].pop(rooms[CURRENT_ROOM]['items'].index('monster'))
               print("There is a monster in the room that immediately lunges at you.")
               print("You deftly roll away from it's attack and counter with a blow")
               print("from the meat cleaver. The monster knocks you away as you do but")
               print("its wound is fatal. The cleaver broke in the process.")
               print("---------------------------")
               PLAYER_1.inventory.pop(PLAYER_1.inventory.index('cleaver'))
            elif 'potion' in PLAYER_1.inventory:
                print("As you enter the room, a giant monster leaps across and") 
                print("knocks you back into the previous room. Luckily you had a")
                print("potion to heal you wounds. You won't get past that way without")
                print("some way of defeating it.")
                print("---------------------------")
                PLAYER_1.inventory.pop(PLAYER_1.inventory.index('potion'))
                CURRENT_ROOM = "Hall_02"
                PLAYER_1.steps += 1
                continue
            else: 
                print("A monster leaps from across the room and eats you! .... GAME OVER")
                break

        ## Define how a player can win
        if CURRENT_ROOM == 'Garden' and 'key' in PLAYER_1.inventory and 'potion' in PLAYER_1.inventory:
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
            if userInput[1] in rooms[CURRENT_ROOM]:
                #set the current room to the new room
                CURRENT_ROOM = rooms[CURRENT_ROOM][userInput[1]]
                PLAYER_1.steps += 1
            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')
        elif userInput[0] == 'get' :
            # make two checks:
            # 1. if the current room contains an item
            # 2. if the item in the room matches the item the player wishes to get
            if "items" in rooms[CURRENT_ROOM] and userInput[1] in rooms[CURRENT_ROOM]['items']:
                #add the item to their inventory
                PLAYER_1.inventory.append(userInput[1])
                #display a helpful message
                print(userInput[1] + ' got!')
                #delete the item key:value pair from the room's dictionary
                rooms[CURRENT_ROOM]['items'].pop(rooms[CURRENT_ROOM]['items'].index(userInput[1]))
            # if there's no item in the room or the item doesn't match
            else:
                #tell them they can't get it
                print('Can\'t get ' + userInput[1] + '!')
        elif userInput[0] == 'help':
            showInstructions()
        elif userInput[0] == 'inventory':
            print(PLAYER_1.inventory)
        elif userInput[0] == 'exit':
            print("Exiting the game.")
            exit()
        else:
            print("I don't know what you mean.")
        


if __name__ == "__main__":
    main()