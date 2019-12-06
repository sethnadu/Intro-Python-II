# Write a class to hold player information, e.g. what room they are in
# currently.
import random
from room import Room

class Player:
    def __init__(self, name, room, inventory, health):
        self.name = name
        self.current_room = room
        self.inventory = list(inventory)
        self.health = health


    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is None:
            print('')
            print("You can not go in that direction")
            print('')
        else: 
          self.current_room = getattr(self.current_room, f"{direction}_to")  

    def getInventory(self, player):
        print('')
        print("Inventory:")
        print('')
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(f"{item.name}: {item.description}")
        else: 
            print("You have no items in your Inventory!")
            print('')

    def dropFromInventory(self, drop, player):
        drop_split = drop.split()
        item_only = ' '
        drop_item = item_only.join(drop_split[1:])
        if drop is not '':
            if drop_split[0] == "Drop":
                for item in self.inventory:
                    if item.name == drop_item:
                        item.on_drop(player, item)
                print(f"{drop_item} have been dropped to {player.current_room.name}!")
                print('-------------------------------------------')
                print('')
            elif drop == 'exit': 
                print("You have left your Inventory")
        else:
            print("Invalid Key!")

    def addItemToInventory(self, add, player):
        add_split = add.split()
        item_only = ' '
        add_item = item_only.join(add_split[1:])
        # Add All Items/ Remove all from current room
        if add == 'all':
                for item in range(len(player.current_room.items)):
                    self.inventory.append(player.current_room.items[item])
                player.current_room.items.clear()
                print("Items have been added!")
                print('-------------------------------------------')
                print('')
        # Add specific item/ Remove from current room
        elif add_split[0] == "Take":
            for item in player.current_room.items:
                if item.name == add_item:
                    item.on_take(player, item)
            print(f"{add_item} have been added!")
            print('-------------------------------------------')
            print('')
        # Exit Search
        elif add == 'exit':
            print(f"{player.name} stopped searching")
            print('-------------------------------------------')
            print('')
        else:
            print("Invalid key!")
            print('')

    def removeItemFromInventory(self, item):
        self.inventory.remove(item)

    def attack(self, weapon, enemy):
        damageEnemy = random.randint(weapon.minDamage, weapon.maxDamage)
        damagePlayer = random.randint(weapon.minDamage, weapon.maxDamage)
        healthLeftEnemy = enemy.health - damageEnemy
        print(f"{enemy.name} was hit with {damageEnemy} damage")
        if healthLeftEnemy < 0 or healthLeftEnemy == 0:
            print(f"{enemy.name} has 0 health left")
            enemy.health = healthLeftEnemy
        else:
            print(f"{enemy.name} has {healthLeftEnemy} health left")
            enemy.health = healthLeftEnemy
        
        print('')
        print(f"{enemy.name} attacks {self.name}")
        healthLeftPlayer = self.health - damagePlayer
        if healthLeftPlayer < 0 or healthLeftPlayer == 0:
            print(f"{self.name} has 0 health left")
            enemy.health = healthLeftEnemy
        else:
            print(f"{self.name} was hit with {damagePlayer} damage")
            print(f"{self.name} has {healthLeftPlayer} left")
            self.health = healthLeftPlayer




class Enemy(Player):
    def __init__(self, name, current_room, inventory, health):
        super().__init__(name, current_room, inventory, health)
        
        
            
class Main(Player):
    def __init__(self, name, current_room, inventory, health):
        super().__init__(name, current_room, inventory, health)    