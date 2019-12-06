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

    def checkEnemies(self, enemies, player, player_death_room, enemy_death_room):
        for enemy in enemies:
            while player.current_room == enemy.current_room:
                print(f"{enemy.name} is in the room!")
                print('')
                battle = input("Do you fight, or run (fight, run)[i, q]?: ")
                print('********************************************')
                print('')
                if battle == 'fight':
                    for item in player.inventory:
                        if isinstance(item, Weapon):
                            weapons = []
                            weapons.append(item)
                            if len(weapons) == 1:
                                print(f"You attack the {enemy.name} with {weapons[0].name}")
                                if enemy.health != 0 and enemy.health > 0 or player.health != 0 and enemy.health > 0:
                                    player.attack(weapons[0], enemy)
                                else:
                                    if enemy.health == 0 or enemy.health < 0:
                                        print('')
                                        print(f"{player.name} has defeated {enemy.name}")
                                        print('')
                                        enemy.current_room = enemy_death_room
                                        player.current_room.items.append(enemy.inventory[0])
                                        print(enemy.inventory[0])
                                    elif player.health == 0 or player.health < 0:
                                        print("")
                                        print(f"{player.name} was defeated by {enemy.name}")
                                        print("")
                                        player.current_room = player_death_room
                            elif len(weapons) > 1:
                                print("Available weapons:")
                                for weapon in weapons:
                                    print(weapon.name)
                                pick = input("Which weapon do you wish to attack with?")    
                            else: 
                                print("You don't have a weapon!")