# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    # def __str__(self):
    #     return f'Player: {self.name} is {self.room}'

    