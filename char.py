# This is a basic version of the char class
import dice
from lib import reader


class Character():
    def __init__(self,
                 player_class: str,
                 life: int = 60,
                 strength: int = 10 + dice.dice_d(3, 3),
                 inventory: list = [],
                 description: str = ''
                 ) -> None:
        self.player_class = player_class
        self.name = input('Enter a name: \n')
        self.life = life
        self.initial_life = self.life
        self.inventory = inventory
        self.strength = strength
        self.description = description

    def stats(self):
        print('''--> Name: "{}" Class: "*{}*"
              \nLife: [{}/{}] Strength: [{}]\n'''.format(self.name,
              self.player_class, self.life,
              self.initial_life, self.strength))

    def print_inventory(self):
        print('--> Inventory: {}\n'.format(self.inventory))

    def print_description(self):
        print('--> {}\n'.format(self.description))

    def take_hit(self, value):
        self.life -= value
        if(self.life > 0):
            print('Hit! You have {}/{} health left.'
                  .format(self.life, self.inital_life))
        else:
            print('You have been wounded fatally. Game over...')


def char_selector():
    char_selection = ''
    while char_selection.upper() not in ['A', 'B', 'C']:
        char_selection = input('''--> Select a character: \n
        A) The Adventurer \n
        B) The Mechanic \n
        C) The Zookeeper \n
        ''')

        if (char_selection.upper() == 'A'):
            return Character('Coach', 60, 60, [], reader.parse('./txt/char_related.txt', '{CCC0}'))
        elif (char_selection.upper() == 'B'):
            return Character('Mechanic', 50, 40, ['Multitool'], reader.parse('./txt/char_related.txt', '{CCM0}'))
        elif (char_selection.upper() == 'C'):
            return Character('Zookeeper', 40, 30, ['Mouse'], reader.parse('./txt/char_related.txt', '{CCZ0}'))
