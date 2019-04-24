# This is a basic version of the char class


class Character():
    def __init__(self, name, life, strength, inventory):
        self.name = name
        self.life = life
        self.strength = strength
        self.inventory = inventory
    def getvalues(self):
        print(self.name, self.strength)
