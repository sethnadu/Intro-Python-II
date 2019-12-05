

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player, item):
        player.addItemToInventory(item)
        player.current_room.removeItemFromRoom(item)

    def on_drop(self, player, item):
        print(item)
        player.removeItemFromInventory(item)
        player.current_room.addItemToRoom(item)
