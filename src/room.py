# Implement a class to hold room information. This should have name and
# description attributes.
# from item import Item
from item import Weapon
class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = list(items)
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None 

    def getItemsInRoom(self, player):
        for item in player.current_room.items:
            if isinstance(item, Weapon):
                print(f'{item.name}[{item.minDamage},{item.maxDamage}]: {item.description}')
            else:
                print(f'{item.name}: {item.description}')
        print('')
        add = input("Type 'Take' with item name to add to inventory, 'all' to add all items or 'exit' stop searching: ")
        print('********************************************')
        print('')
        if add is not '':
            player.addItemToInventory(add, player)
        else: 
            print("Invalid key!")


    def addItemToRoom(self, item):
        self.items.append(item)

    def removeItemFromRoom(self, item):
        self.items.remove(item)

    def continueOn(self, player):
        direction_array = ['n', 'e', 's', 'w']
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
            drop = input("Type 'Drop', 'Consume', or 'Sleep' followed by item name to drop it, consume it, or use to sleep. Type 'exit' to exit inventory: ")
            print('********************************************')
            print('')
            player.dropFromInventoryOrEat(drop, player)
        # Quit the Game
        elif direction == 'q':
            print(f"Thanks for playing {player.name}")
            quit()
        elif direction == '':
            print("Invalid key!")
        else: 
            print(f"Sorry, '{direction}' is not a valid direction")


    def checkEnemies(self, enemies, player, player_death_room, enemy_death_room):
        weapons = []
        for item in player.inventory:
            if isinstance(item, Weapon):
                weapons.append(item)
        for enemy in enemies:
            if player.current_room == enemy.current_room:
                print('')
                print(f"{enemy.name} is in the room!")
                print('')
                battle = input("Do you fight, or run (fight, run)[i, q]?: ")
                print('********************************************')
                print('')
                if battle == 'fight':
                    print("Available weapons:")
                    for weapon in weapons:
                        print(f"{weapon.name}:[{weapon.minDamage}, {weapon.maxDamage}]")    
                    print('')
                    pick = input("Which weapon do you wish to attack with?: ")
                    print('********************************************')
                    print('')
                    while player.current_room == enemy.current_room:
                        for weapon in weapons:
                            if pick == weapon.name:
                                print(f"{player.name} attacked the {enemy.name} with {weapon.name}:[{weapon.minDamage}, {weapon.maxDamage}]")
                                player.attackProgress(player, enemy, weapon, player_death_room, enemy_death_room)
                    if len(weapons) == 0: 
                        print("You don't have a weapon!")
                        print(f"{player.name} runs away!")
                        player.current_room.continueOn(player)
                elif battle == "run":
                    player.current_room.continueOn(player)