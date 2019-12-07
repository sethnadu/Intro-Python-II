class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, player, item):
        player.inventory.append(item)
        player.current_room.removeItemFromRoom(item)

    def on_drop(self, player, item):
        player.removeItemFromInventory(item)
        player.current_room.addItemToRoom(item)

class Weapon(Item):
    def __init__(self, name, description, minDamage, maxDamage):
        super().__init__(name, description)
        self.minDamage = minDamage
        self.maxDamage = maxDamage

class Food(Item):
    def __init__(self, name, description, energy):
        super().__init__(name, description)
        self.energy = energy

class Bed(Item):
    def __init__(self, name, description, uses):
        super().__init__(name, description)
        self.uses = uses