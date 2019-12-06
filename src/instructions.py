class Instructions:
    def __init__(self):
        pass

    def getInfo(self, start):
        if start == "start":
            print('-------------------------------------------')
            print("Use the following keys to navigate: \n'n' for north, \n'e' for east, \n's' for south, \n'w' for west \n")
            print("You can quit the game anytime by typing 'q'")
            print("Check your inventory by typing 'i'")
            print('-------------------------------------------')
            print('')
        elif start == 'q':
            print("Goodbye!")
            quit()
        else:
            print('')
            print("Sorry, type 'start' to begin, or 'q' to quit")
            print('')