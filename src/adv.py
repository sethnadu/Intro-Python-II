from room import Room
from player import Player
from item import Item


# Declare all Items
item = {
    "dagger": Item("Sting", "A magical Elvish knife or dagger"),
    "ring": Item("The One Ring", "The One Ring to rule them all, crafted by the Dark Lord Sauron in Mount Doom, found in Gollum's Cave"),
    "food": Item("Hobbit Hash", "Breakfast meal containing: potatoes, leeks, spinach, and cheese"),
    "drink": Item("Beer", "A favorite among Hobbits"),
    "pouch": Item("A Gold Pouch", "Filled with Gold!"),
    "book": Item("There and Back Again", "It's not finished yet!"),
    "pipe": Item("Pipe", "Used for smoking Gilly-weed or Tobacco"),
    "walking-stick": Item("Gandalf's Staff", "Gandalf must have left it here, or is close by...")
}

# Declare all the rooms

room = {
    'outside':  Room("Bag-End Entrance, Bilbo's House",
                    "The round door is cracked ajar to the north, sweet smells are wofting out",
                    [item["pipe"]]),

    'foyer':    Room("Kitchen", 
                    """Dim light filters in from the south. The source of the savory smells come from a wooden table. Small passages run north and east.""", 
                    [item["food"], item["drink"]]),

    'overlook': Room("Overlook", 
                    """ While under renovations, you can see out the side of the hill. Darkness falls below you, and you can see feint lights from the other dwellings in the distance. The small passageway you came from is the only way you can go.""",
                    [item["walking-stick"]]),

    'narrow':   Room("Hallway", 
                """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
                [item["pouch"]]),

    'treasure': Room("Treasure Chamber", 
                """You have entered into your treasure room. It is filled with items from your previous adventures. No other ways to continue through the house but back the way you came."""
                ,[item["dagger"], item["book"], item["ring"]]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']



# Declare all Players

player = Player("Bilbo Baggins", room['outside'], [])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction_array = ['n', 'e', 's', 'w']

# Start of Game
print('\n')
print("Welcome to the Hobbit Adventure Game \n")

start = None
# Directions to start the game
while start == None or not start == 'start':
    start = input("Type 'start' to Start Your Adventure: ")
    print('********************************************')
    print('')
    if start == "start":
        print('-------------------------------------------')
        print("Use the following keys to navigate: \n'n' for north, \n'e' for east, \n's' for south, \n'w' for west \n")
        print("You can quit the game anytime by typing 'q'")
        print('-------------------------------------------')
        print('')
    elif start == 'q':
        print("Goodbye!")
        quit()
    else:
        print('')
        print("Sorry, type 'start' to begin, or 'q' to quit")
        print('')
        direction = ''
else:  
    # MAIN 
    while True:
        print('')
        print(f"{player.current_room.name}:")
        print(player.current_room.description)
        print('')
        info = input("Would you like to continue on, or search around (search, continue)? ")
        print('********************************************')
        if info == "search" and len(player.current_room.items) > 0:
            print(f"{player.name} is searching...")
            print('')
            print(f"You found:")
            ####### Display Items in current room

            # MOVE TO item.py
            items_array = []
            item_names = []
            for item in player.current_room.items:
                print(f'{item.name}: {item.description}')
                items_array.append(item)
                item_names.append(item.name)
            print('')
            #Finish move

            ####### Decide to add to inventory or move on
            add = input("Type in the name of the item you would wish you to add, or 'all' for all the items, 'no' to move on: ")

            #Move to player.py
            if add == 'all':
                for item in range(len(player.current_room.items)):
                    player.addItemToInventory(player.current_room.items[item])
                player.current_room.items.clear()
                print("Items have been added!")
                print('-------------------------------------------')
                print('')
            elif add in item_names:
                for item in items_array:
                    if item.name == add:
                        player.addItemToInventory(add)
                        player.current_room.removeItemFromRoom(item)
                print(f"{add} have been added!")
                print('-------------------------------------------')
                print('')
                # player.current_room.removeItemFromRoom(add)
            elif add == 'no':
                print(f"{player.name} stopped searching")
                print('-------------------------------------------')
                print('')
            else:
                print("Invalid key!")
                print('')
            #Finish Move
        elif info == 'search' and len(player.current_room.items) < 1:
            print(f"{player.name} is searching...")
            print('')
            print(f"You found no items!")
        elif info == 'q':
            print('Goodbye!')
            quit()
        elif info == 'continue':
            ######### Navigate to different Rooms
            print("Moving on..")
            direction = input("What direction would you like to move (n/e/w/s)?  ")
            print('********************************************')
            print('')
            if direction in direction_array:
                player.move(direction)
            elif direction == 'q':
                print(f"Thanks for playing {player.name}")
                quit()
            else: 
                print(f"Sorry, '{direction}' is not a valid direction")
        else:
            print("Type in 'search', 'continue' or 'q' ")
            print('********************************************')
            print('')

