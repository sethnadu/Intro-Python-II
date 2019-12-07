# Write a class to hold player information, e.g. what room they are in
# currently.
import random
import time
from room import Room
from item import Weapon, Food, Bed


class Player:
    def __init__(self, name, room, inventory, health, maxHealth):
        self.name = name
        self.current_room = room
        self.inventory = list(inventory)
        self.health = health
        self.maxHealth = maxHealth

    # Navigate directions
    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is None:
            print('')
            print("You can not go in that direction")
            print('')
        else: 
          self.current_room = getattr(self.current_room, f"{direction}_to")  

    # Check Inventory
    def getInventory(self, player):
        print('')
        print(f"{player.name}'s health: {player.health}/{player.maxHealth}")
        print('')
        print("Inventory:")
        print('')
        if len(self.inventory) > 0:
            for item in self.inventory:
                if isinstance(item, Weapon):
                    print(f"{item.name}[{item.minDamage}, {item.maxDamage}]: {item.description}")
                elif isinstance(item, Bed):
                    print(f"{item.name}[{item.uses}]: {item.description}")
                else:
                    print(f"{item.name}: {item.description}")
        else:   
            print("You have no items in your Inventory!")
            print('')
        
    # Drop or Consume items in Inventory
    def dropFromInventoryOrEat(self, drop, player):
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
            elif drop_split[0] == "Consume":
                for item in self.inventory:
                    if item.name == drop_item and isinstance(item, Food):
                        if player.health > player.maxHealth or player.health == player.maxHealth:
                            print('')
                            print(f"{player.name} is not hungry or thirsty")
                            print('')
                        else:
                            player.health = player.health + item.energy
                            print('')
                            print(f"{player.name}'s health went up by {item.energy} points!")
                            print('')
                    elif item.name == drop_item and not isinstance(item, Food):
                        print("You can not consume that.")
            elif drop_split[0] == 'Sleep':
                for item in self.inventory:
                    if item.name == drop_item and isinstance(item, Bed):
                        if item.uses > 0:
                            print("You have layed out your bed gear")
                            item.uses = item.uses - 1
                            if player.health < player.maxHealth:
                                sleepHeal = random.randint(10, player.health // 2)
                                player.health = player.health + sleepHeal
                                print('')
                                print(f"Your sleep has made you feel better, your health went up {sleepHeal} points")
                                print(f'{item.name} has {item.uses} left.')
                                print('')
                            else:
                                print("You are not tired!")
                        elif item.uses == 0:
                            print("There are no more uses left!")
                            time.sleep(1)
                            print("...")
                            time.sleep(2)
            elif drop == 'exit': 
                print("You have left your Inventory")
        else:
            print("Invalid Key!")

    # Add item to inventory
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

    #  Remove item from inventory
    def removeItemFromInventory(self, item):
        self.inventory.remove(item)

    # Progress of Attacking
    def attackProgress(self, player, enemy, weapons, player_death_room, enemy_death_room):
        if enemy.health > 0 and player.health > 0:
            player.attack(weapons, enemy)
            print('')
            input("Type any key to attack!")
            print('********************************************')
            print('')
        else:
            if enemy.health == 0 or enemy.health < 0:
                print('')
                print(f"{player.name} has defeated {enemy.name}")
                print(f"{enemy.name} may have dropped items!")
                print('')
                enemy.current_room = enemy_death_room
                for inv in enemy.inventory:
                    player.current_room.items.append(inv)
            elif player.health == 0 or player.health < 0:
                print("")
                print(f"{player.name} was defeated by {enemy.name}")
                print("")
                player.current_room = player_death_room

    # Attack Action
    def attack(self, weapon, enemy):
        damageEnemy = random.randint(weapon.minDamage, weapon.maxDamage)
        damagePlayer = random.randint(weapon.minDamage, weapon.maxDamage)
        healthLeftEnemy = enemy.health - damageEnemy
        print(f"{enemy.name} was hit with {damageEnemy} damage")
        if healthLeftEnemy < 0 or healthLeftEnemy == 0:
            print(f"{enemy.name} is almost dead")
            enemy.health = healthLeftEnemy
        else:
            print(f"{enemy.name} has {healthLeftEnemy} health left")
            enemy.health = healthLeftEnemy
        
        print('')
        print(f"{enemy.name} attacks {self.name} with {enemy.inventory[0].name}:[{enemy.inventory[0].minDamage}, {enemy.inventory[0].maxDamage}]")
        healthLeftPlayer = self.health - damagePlayer
        if healthLeftPlayer < 0 or healthLeftPlayer == 0:
            print(f"{self.name} has is almost dead")
            self.health = healthLeftPlayer
        else:
            print(f"{self.name} was hit with {damagePlayer} damage")
            print(f"{self.name} has {healthLeftPlayer} left")
            self.health = healthLeftPlayer




class Enemy(Player):
    def __init__(self, name, current_room, inventory, health, maxHealth):
        super().__init__(name, current_room, inventory, health, maxHealth)
        
        
            
class Main(Player):
    def __init__(self, name, current_room, inventory, health, maxHealth):
        super().__init__(name, current_room, inventory, health, maxHealth)    