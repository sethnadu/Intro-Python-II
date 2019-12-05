# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, inventory):
        self.name = name
        self.current_room = room
        self.inventory = list(inventory)

    # def __str__(self):
    #     return f'Player: {self.name} is {self.room}'

    def move(self, direction):
        if getattr(self.current_room, f"{direction}_to") is None:
            print('')
            print("You can not go in that direction")
            print('')
        else: 
          self.current_room = getattr(self.current_room, f"{direction}_to")  

    def getInventoryAndDrop(self, player):
        item_names = []
        item_objects = []
        if len(self.inventory) > 0:
            for item in self.inventory:
                if item is not str(item):
                    print(f"{item.name}: {item.description}")
                    item_objects.append(item)
                    item_names.append(item.name)
        else: 
            print("You have no items in your Inventory!")
            print('')
        print('')
        drop = input("Type 'Drop' with item name to drop item in room, 'exit' to exit inventory: ")
        print('********************************************')
        print('')
        drop_split = drop.split()
        item_only = ' '
        drop_item = item_only.join(drop_split[1:])
        if drop_split[0] == "Drop" and drop_item in item_names:
            for item in item_objects:
                if item.name == drop_item:
                    print(item)
                    item.on_drop(player, item)
                print(f"{item.name} have been dropped to {player.current_room.name}!")
                print('-------------------------------------------')
                print('')
        elif drop == 'exit': 
            print("You have left your Inventory")

    def findItem(self, add, player, item_names, items_array):
        add_split = add.split()
        item_only = ' '
        add_item = item_only.join(add_split[1:])
        # Add All Items
        if add == 'all':
                for item in range(len(player.current_room.items)):
                    player.addItemToInventory(player.current_room.items[item])
                player.current_room.items.clear()
                print("Items have been added!")
                print('-------------------------------------------')
                print('')
        # Add specific item
        elif add_split[0] == "Take" and add_item in item_names:
            for item in items_array:
                if item.name == add_item:
                    item.on_take(player, item)
            print(f"{add_item} have been added!")
            print('-------------------------------------------')
            print('')
        # Drop Specific Item
        # elif add_split[0] == "Drop" and add_item in item_names:
        #     for item in items_array:
        #         if item.name == add_item:
        #             item.on_drop(player, item, add_item)
        #     print(f"{add_item} have been added!")
        #     print('-------------------------------------------')
        #     print('')
        # Add no items
        elif add == 'no':
            print(f"{player.name} stopped searching")
            print('-------------------------------------------')
            print('')
        else:
            print("Invalid key!")
            print('')



    def addItemToInventory(self, item):
        self.inventory.append(item)

    def removeItemFromInventory(self, item):
        self.inventory.remove(item)


    