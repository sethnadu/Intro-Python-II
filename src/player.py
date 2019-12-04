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


    def getInventory(self):
        return self.inventory

    def addItemToInventory(self, item):
        self.inventory.append(item)

    def removeItemFromInventory(self, item):
        self.inventory.remove(item)



    