from instructions import Instructions
import time
# Declare Instructions
instruct = Instructions()

class Intro():
    def __init__(self):
        pass

    def introText(self, player):
        start = input("Type 'start' to Start Your Adventure: ")
        print('********************************************')
        print('')
        instruct.getInfo(start)
        print('')
        print("In a hole in the ground there lived a hobbit...")
        print('')
        time.sleep(2)
        print("Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort. ")
        print('')
        time.sleep(3)
