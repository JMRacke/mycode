
rooms = {   
    "Hall" : {
          "description" : "The hallway is barren. There are doors to the south, east, and west.",
          "south" : "Kitchen",
          "east" : "Dining Room",
          "west" : "Den"
        },
    "Den" : {
          "description" : "",
          "east" : "Hall",
          "items" : ["key"]
        },
    "Kitchen" : {
          "description" : "The kitchen smells rancid. To the north is a door way. In the corner you see a grotesque beast!",
          "north" : "Hall",
          "items" : ["monster"]
        },
    "Dining Room" : {
        "description": "",
        "west" : "Hall",
        "south" : "Garden",
        "items" : ["potion"]
        },
    "Garden" : {
        "description" : "The gardens are filled with flora from all over the world. To the north is a doorway.",
        "north" : "Dining Room"
        }
 }

rooms["Den"]["description"] = "The den smells of mahogany. There are books on build in shelves in the wall, and an ornate desk in the center." +  \
                                f"{'On the desk is a key.' if 'key' in rooms['Den']['items'] else ''} To the east is a doorway."
rooms["Dining Room"]["description"] = "Dust covers the place settings on the table. It looks as", \
                                      "though the owners were expecting company.", \
                                      f"{'In the middle of the table, there is a potion.' if 'potion' in rooms['Dining Room']['items'] else ''}", \
                                      "To the west and south are doorways"