from lib import reader


class Monster():
    PATH = './txt/monster.txt'

    def __init__(self, life: int, strength: int, monster_id: str, inventory):
        self.life = life
        self.initial_life = self.life
        self.strength = strength
        self.monster_id = monster_id
        self.inventory = inventory

    def print_description(self):
        '''Description on encounter'''
        reader.parse(self.PATH, ''.join((self.monster_id, 'D')))

    def attack(self):
        '''Monster wins an attack'''
        reader.parse(self.PATH, ''.join((self.monster_id, 'H')))

    def loot(self):
        '''Player gets item after winning a fight'''
        print('You find nothing of interest')

    def take_hit(self, value):
        '''Palyer hits monster'''
        self.life -= value
        if (self.life > 0):
            reader.parse(self.PATH, ''.join((self.monster_id, 'T')))
            print('The monster takes a hit and has {}/{} health left.'
                  .format(self.life, self.initial_life))
        else:
            reader.parse(self.PATH, ''.join((self.monster_id, 'L')))
            self.loot()


# Beastary
Dog = Monster(6, 0, 'MD0', [])
Crows = Monster(5, 0, 'MC0', [])
Rat = Monster(7, 0, 'MR0', [])
Servents = Monster(7, 0, 'MS0', ['Golden Key'])
Cook = Monster(6, 0, 'MO0', [])
OldMan = Monster(8, 0, 'MM0', ['Silver Key'])
Final = Monster(10, 0, 'MF0', [])
