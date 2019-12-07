from instructions import Instructions
from room import Room
from player import Main, Enemy
from item import Item, Weapon, Food, Bed
from intro import Intro
from gandalf import Gandalf
from dwarfs import Dwarfs
import time
import pygame

# Declare all Items
item = {
    # Weapons
    "sting": Weapon("Sting", "A magical Elvish knife or dagger", 13, 25),
    "stick": Weapon("Oak Stick", "A broken branch from an Oak Tree", 6, 12),
    "machete": Weapon("Hooked Machete", "A long machete with a sharp hook on the end", 7, 15),
    "rock": Weapon("Rock", "A large rock with a sharp end", 10, 30),
    "walking-stick": Weapon("Gandalf's Staff", "Gandalf must have left it here, or is close by...", 12, 35),
    "teeth": Weapon("Sharp Teeth", "Sharp teeth used as a weapon!", 5, 8),

    # Items
    "ring": Item("The One Ring", "The One Ring to rule them all, crafted by the Dark Lord Sauron in Mount Doom, found in Gollum's Cave"),
    "pouch": Item("A Gold Pouch", "Filled with Gold!"),
    "book": Item("There and Back Again", "It's not finished yet!"),
    "pipe": Item("Pipe", "Used for smoking Gilly-weed or Tobacco"),
    "gilly-weed": Item("Gilly-weed", "Used to relax, need a pipe to smoke it"),
    

    # Bed Gear
    "bed-gear": Bed("Bed Gear", "Can be used to sleep and heal some health", 5),

    # Food
    "food": Food("Hobbit Hash", "Breakfast meal containing potatoes, leeks, spinach, and cheese", 35),
    "drink": Food("Beer", "A favorite among Hobbits", 15),
}

# Declare all the rooms
room = {
    # Hell
    'dead': Room("Hell", "Enemies go here when they die", []),
    # Bag End House
    'outside':  Room("Bag-End Entrance, Bilbo's House",
                    "The round door of a house build into the ground is cracked ajar to the north, sweet smells are wofting out",
                    [item["pipe"]]),

    'foyer':    Room("Dining-Room", 
                    """Dim light filters in from the south. The source of the savory smells come from a wooden table. Small passages run north and east.""", 
                    [item["food"], item["drink"]]),

    'narrow':   Room("Hallway", 
                """The narrow passage bends here from west to north. The smell of earth and food permeates the air.""",
                [item["pouch"]]),

    'treasure': Room("Living Room", 
                """You have entered into your living room. It is filled with books, papers with a comfy chair and desk. No other ways to continue through the house but back the way you came."""
                ,[]),

    "bag-bedroom": Room("Bilbo's Bedroom", 'A very cozy bedroom, the bed looks comfortable! The only exit is the way you came.', [item["bed-gear"]]),

    'overlook': Room("Overlook", 
                    """ While under renovations, you can see out the side of the hill. Darkness falls below you, and you can see feint lights from the other dwellings in the distance. The small passageway you came from is the only way you can go.""",
                    [item["walking-stick"]]),

}


# Link rooms together
# Bag End
room['outside'].n_to = room['narrow']
room['narrow'].s_to = room['outside']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['narrow'].w_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['foyer'].n_to = room['bag-bedroom']
room['bag-bedroom'].s_to = room['foyer']

# Declare all Players
player = Main("Bilbo Baggins", room['outside'], [item["gilly-weed"], item["stick"]], 100, 100)
orc = Enemy("Uruk Hai", room['dead'], [item["machete"]], 45, 45)
gollum = Enemy("Gollum", room['dead'], [item["rock"], item["ring"]], 75, 75)
rat = Enemy("Rat", room['foyer'], [item['teeth']], 20, 20)

# Declare Character Classes
gandalf = Gandalf()
dwarfs = Dwarfs()


enemies = [
    orc,
    gollum,
    rat
]

intro = Intro()

########################## Start of Game ##########################
pygame.mixer.init()
pygame.mixer.music.load("src/Sounds/shire.mp3")
pygame.mixer.music.play(loops=-1)
print('\n')
print("Welcome to the Hobbit Adventure Game \n")

start = None
direction = ''
##### Directions to start the game #####

intro.introText(player)
    ######################## MAIN ########################
print('')
# Check if enemy is in room, run or attack
player.current_room.checkEnemies(enemies, player, room["outside"], room["dead"])
print(f"{player.current_room.name}:")
time.sleep(1)
print(player.current_room.description)
time.sleep(2)
print('')
input('Type any key to continue..')
print('********************************************')
print('')
gandalf.greetingGandalfAtBagEnd(player, room['narrow'])
while True:
    print('')
    # Check if enemy is in room, run or attack
    player.current_room.checkEnemies(enemies, player, room["outside"], room["dead"])
    if len(room['foyer'].items) == 0:
        dwarfs.greetDwarfsAtBag(player, room['treasure'], item[''])
    
    print(f"{player.current_room.name}:")
    time.sleep(1)
    print(player.current_room.description)
    time.sleep(2)
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
        drop = input("Type 'Drop', 'Consume', or 'Sleep' followed by item name to drop it, consume it, or use to sleep. Type 'exit' to exit inventory: ")
        print('********************************************')
        print('')
        player.dropFromInventoryOrEat(drop, player)
    # Navigation
    elif info == 'continue':
        player.current_room.continueOn(player)
else:
    print("Type in 'search', 'continue', 'q' for quit, 'i' for inventory ")
    print('********************************************')
    print('')

