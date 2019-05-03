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
        self.life = life
        self.strength = strength
        self.inventory = inventory
        self.description = '''You are an adventurer with no specific
        traits but better stats.'''
        self.name = input('Enter a name: \n')

    def stats(self):
        print('''--> Name: "{}" Class: "*{}*"
              \nLife: [{}] Strength: [{}]\n'''.format(self.name,
              self.type,
              self.life, self.strength))

    def print_inventory(self):
        print('--> Inventory: {}\n'.format(self.inventory))

    def print_description(self):
        print('--> {}\n'.format(self.description))


class Mechanic(Character):
    def __init__(self):
        super().__init__()
        self.type = 'Mechanic'
        self.inventory = ['Hammer']
        self.life = 50
        self.strength = self.strength - 2
        self.description = '''You are good with fixing things,
        especially with your favorite tool, the handy hammer(TM).'''


class Zookeeper(Character):
    def __init__(self):
        super().__init__()
        self.type = 'Zookeeper'
        self.inventory = ['Mouse']
        self.life = 40
        self.strength = self.strength - 3
        self.description = '''You work the Zooshop day and night only
        accompanied by your pet companion "Manny the Mouse".'''


def char_selector():
    char_selection = ''
    while char_selection.upper() not in ['A', 'B', 'C']:
        char_selection = input('''--> Select a character: \n
        A) The Adventurer \n
        B) The Mechanic \n
        C) The Zookeeper \n
        ''')

        if (char_selection.upper() == 'A'):
            return Character()
        elif (char_selection.upper() == 'B'):
            return Mechanic()
        elif (char_selection.upper() == 'C'):
            return Zookeeper()
