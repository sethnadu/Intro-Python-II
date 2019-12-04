from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Bag-End Entrance, Bilbo's House",
                     "The round door is cracked ajar to the north, sweet smells are wofting out"),

    'foyer':    Room("Kitchen", """Dim light filters in from the south. The source of the savory smells come from a wooden table. Small passages run north and east."""),

    'overlook': Room("Overlook", """ While under renovations, you can see out the side of the hill. Darkness falls below you, and you can see feint lights from the other dwellings in the distance. The small passageway you came from is the only way you can go."""),

    'narrow':   Room("Hallway", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You have entered into your treasure room. It is filled with items from your previous adventures. No other ways to continue through the house but back the way you came."""),
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

player = {
    "bilbo": Player("Bilbo Baggins", room['outside'])
}

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
        print(f"Welcome {player['bilbo'].name}, to the {player['bilbo'].current_room.name}")
        print(player["bilbo"].current_room.description)
        print('')
    elif start == 'q':
        quit()
    else:
        print('')
        print("Sorry, type 'start' to begin, or 'q' to quit")
        print('')
        direction = ''
else:

    ###### Navigation through rooms
    while player['bilbo']:
        direction = input("Where would you look to move (n/e/w/s)?  ")
        print('********************************************')
        print('')
        # Outside navigation
        if player["bilbo"].current_room.name == room['outside'].name:
            if direction == "n":
                player['bilbo'].current_room = room['outside'].n_to
                print('')
                print(f"You have entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == 's' or direction == 'w' or direction == 'e':
                print('')
                print(f"{player['bilbo'].name} can not go that way! \n")
            elif direction == 'q': 
                exit()
            else:
                print("Sorry, Pick a direction to navigate!")
                direction = ''

        # Foyer navigation
        elif player["bilbo"].current_room.name == room['foyer'].name:
            if direction == "n":
                player['bilbo'].current_room = room['foyer'].n_to
                print('')
                print(f"You entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == "s":
                player['bilbo'].current_room = room['foyer'].s_to
                print('')
                print(f"You entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == "e":
                player['bilbo'].current_room = room['foyer'].e_to
                print('')
                print(f"You entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == 'w':
                print(f"{player['bilbo'].name} can not go that way! \n")
            elif direction == 'q': 
                exit()
            else:
                print('')
                print(f"Sorry, {direction} Pick a direction to navigate!")
                direction = ''

        # Narrow Navigation
        elif player["bilbo"].current_room.name == room['narrow'].name:
            if direction == "n":
                player['bilbo'].current_room = room['narrow'].n_to
                print('')
                print(f"You entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == "w":
                player['bilbo'].current_room = room['narrow'].w_to
                print('')
                print(f"You entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == "e" or direction == 's':
                print('')
                print(f"{player['bilbo'].name} can not go that way! \n")
            elif direction == 'q': 
                exit()
            else:
                print('')
                print(f"Sorry, {direction} Pick a direction to navigate!")
                direction = ''

        # Overlook Navigation
        elif player["bilbo"].current_room.name == room['overlook'].name:
            if direction == "n":
                print(' ')
                print(f"{player['bilbo'].name} will fall down the hill! \n")
            elif direction == "s":
                player['bilbo'].current_room = room['overlook'].s_to
                print('')
                print(f"You entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == "e" or direction == 'w':
                print('')
                print(f"{player['bilbo'].name} can not go that way! \n")
            elif direction == 'q': 
                exit()
            else:
                print('')
                print(f"Sorry, {direction} Pick a direction to navigate!")
                direction = ''

        # Treasure Navigation
        elif player["bilbo"].current_room.name == room['treasure'].name:
            if direction == "e" or direction == 'w' or direction == 'n':
                print('')
                print(f"{player['bilbo'].name} can not go that way! \n")
            elif direction == "s":
                player['bilbo'].current_room = room['treasure'].s_to
                print('')
                print(f"You entered the {player['bilbo'].current_room.name} \n")
                print(player['bilbo'].current_room.description, "\n")
            elif direction == 'q': 
                exit()
            else:
                print('')
                print(f"Sorry, {direction} Pick a direction to navigate!")
                direction = ''
    else: 
        quit()

