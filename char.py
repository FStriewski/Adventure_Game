# This is a basic version of the char class
import dice


class Character():
    def __init__(self,
                 name: str = '',
                 life: int = 60,
                 strength: int = 10 + dice.dice_d(3, 3),
                 inventory: list = [],
                 ) -> None:
        self.type = 'Adventurer'
        self.name = name
        self.life = life
        self.strength = strength
        self.inventory = inventory

    def stats(self):
        print('Name: "{}" Class: "{}" \nLife: [{}] Strength: [{}]'.format(
              self.name,
              self.type,
              self.life,
              self.strength))

    def print_inventory(self):
        print()


class Mechanic(Character):
    def __init__(self):
        super().__init__()
        self.type = 'Mechanic'
        self.inventory = ['Hammer']


