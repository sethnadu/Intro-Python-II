from instructions import Instructions
from room import Room
from player import Main, Enemy
from item import Item, Weapon


# Declare all Items
item = {
    "sting": Weapon("Sting", "A magical Elvish knife or dagger", 10, 25),
    "stick": Weapon("Oak Stick", "A broken branch from an Oak Tree", 6, 12),
    "machete": Weapon("Hooked Machete", "A long machete with a sharp hook on the end", 7, 10),
    "ring": Item("The One Ring", "The One Ring to rule them all, crafted by the Dark Lord Sauron in Mount Doom, found in Gollum's Cave"),
    "food": Item("Hobbit Hash", "Breakfast meal containing potatoes, leeks, spinach, and cheese"),
    "drink": Item("Beer", "A favorite among Hobbits"),
    "pouch": Item("A Gold Pouch", "Filled with Gold!"),
    "book": Item("There and Back Again", "It's not finished yet!"),
    "pipe": Item("Pipe", "Used for smoking Gilly-weed or Tobacco"),
    "walking-stick": Weapon("Gandalf's Staff", "Gandalf must have left it here, or is close by...", 10, 18),
    "gilly-weed": Item("Gilly-weed", "Used to relax, need a pipe to smoke it")
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
                ,[item["sting"], item["book"], item["ring"]]),
    'dead': Room("Hell", "Enemies go here when they die", [])
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
player = Main("Bilbo Baggins", room['outside'], [item["gilly-weed"], item["stick"]], 100)
orc = Enemy("Uruk Hai", room['foyer'], [item["machete"]], 45)

enemies = [
    orc
]




# Declare Instructions
instruct = Instructions()


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




########################## Start of Game ##########################
print('\n')
print("Welcome to the Hobbit Adventure Game \n")

start = None
direction = ''
direction_array = ['n', 'e', 's', 'w']
##### Directions to start the game #####
while start == None or not start == 'start':
    start = input("Type 'start' to Start Your Adventure: ")
    print('********************************************')
    print('')
    instruct.getInfo(start)
    print('')
    print(f'Welcome {player.name}!')
    print('')
else:  
    ######################## MAIN ########################
    while True:
        print('')
        player.current_room.checkEnemies(enemies, player, room["outside"], room["dead"])
        print(f"{player.current_room.name}:")
        print(player.current_room.description)
        print('')
        info = input("Would you like to continue on or search around (search, continue) [i, q] ?: ")
        print('********************************************')
        # Display Items in current room and to Add to Inventory/Remove from room 
        if info == "search" and len(player.current_room.items) > 0:
            print(f"{player.name} is searching...")
            print('')
            print(f"You found:")
            player.current_room.getItemsInRoom(player)
        # Display No Item is no items are found in room
        elif info == 'search' and len(player.current_room.items) < 1:
            print(f"{player.name} is searching...")
            print('')
            print(f"You found no items!")
        # Quit the game
        elif info == 'q':
            print('Goodbye!')
            quit()
        # Check inventory
        elif info == 'i':
            player.getInventory(player)
            print('')
            drop = input("Type 'Drop' with item name to drop item in room, 'exit' to exit inventory: ")
            print('********************************************')
            print('')
            player.dropFromInventory(drop, player)
        # Navigation
        elif info == 'continue':
            print("Moving on..")
            direction = input("What direction would you like to move (n/e/w/s) [q/i]?: ")
            print('********************************************')
            print('')
            # Navigate to different Rooms
            if direction in direction_array:
                player.move(direction)
            # Check Inventory
            elif direction == 'i':
                player.getInventory(player)
                print('')
                drop = input("Type 'Drop' with item name to drop item in room, 'exit' to exit inventory: ")
                print('********************************************')
                print('')
                player.dropFromInventory(drop, player)
            # Quit the Game
            elif direction == 'q':
                print(f"Thanks for playing {player.name}")
                quit()
            elif direction == '':
                print("Invalid key!")
            else: 
                print(f"Sorry, '{direction}' is not a valid direction")
    else:
        print("Type in 'search', 'continue', 'q' for quit, 'i' for inventory ")
        print('********************************************')
        print('')

