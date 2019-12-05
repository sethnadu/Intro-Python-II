# Implement a class to hold room information. This should have name and
# description attributes.
# from item import Item

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = list(items)
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None 

    def getItemsInRoom(self, player, items_array, item_names):
        items_array = []
        item_names = []
        for item in player.current_room.items:
            print(f'{item.name}: {item.description}')
            items_array.append(item)
            item_names.append(item.name)
        print('')
        add = input("Type in the name of the item you would wish you to add, or 'all' for all the items, 'no' to move on: ")
        print('')
        player.findItem(add, player, item_names, items_array)


    def addItemToRoom(self, item):
        self.items.append(item)

    def removeItemFromRoom(self, item):
        self.items.remove(item)