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

    def findItem(self, add, player, item_names, items_array):
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

    def getInventory(self):
        return self.inventory

    def addItemToInventory(self, item):
        self.inventory.append(item)

    def removeItemFromInventory(self, item):
        self.inventory.remove(item)



    