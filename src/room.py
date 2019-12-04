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

    def getItemsInRoom(self):
        return self.items

    def addItemToRoom(self, item):
        self.items.append(item)

    def removeItemFromRoom(self, item):
        self.items.remove(item)