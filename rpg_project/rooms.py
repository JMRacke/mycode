
rooms = {   
    "Lobby" : {
          "description" : "You enter are in a grand lobby.\nThe door to the south has locked you in.\nThere are doors to the east north and west",
          "east" : "Bar",
          "west" : "Hall_01",
          "north" : "Hall_02"
        },
    "Hall_01" : {
          "description" : "The hallway is barren. There are doors to the east and west.",
          "east" : "Lobby",
          "west" : "Kitchen"
        },
    "Bar" : {
          "description" : "You are standing in a bar.\nBehind the bar on the wall you see dozens of bottles of various liquors.\nYou notice a bottle of [potion] among them.\nTo the west is a door.",
          "west" : "Lobby",
          "items" : ["potion"]
        },
    "Kitchen" : {
          "description" : "The kitchen smells rancid. To the north and east are doors.\nStuck in a butcher block, you see a big meat [cleaver].",
          "north" : "Pantry",
          "east" : "Hall_01",
          "items" : ["cleaver"]
        },
    "Pantry" : {
          "description" : "The shelves in this pantry are stocked with expired food.\nIt looks like it has been here for ages.",
          "south" : "Kitchen",
        },
    "Hall_02" : {
          "description" : "The hallway stretches north toward a large room. To the south is the lobby.",
          "south" : "Lobby",
          "north" : "Main Room"
        },
    "Main Room" : {
        "description": "This must be the main entertaining room of the house. In the corner is a dusty grand piano. There are couches everywhere for guests to sit at. There are doorways in all directions.",
        "west" : "Hall_03",
        "south" : "Hall_02",
        "north" : "Hall_04",
        "east" : "Hall_05",
        "items" : ["monster"]
        },
    "Garden" : {
        "description" : "The gardens are filled with flora from all over the world. To the north is a doorway.",
        "north" : "Dining Room"
        }
 }


