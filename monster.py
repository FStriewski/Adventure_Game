import dice


class Monster():
    def __init__(self):
        self.vitality = 20
        self.strength = 10
        self.inventory = []
        self.description = 'A generic monster'
        self.lost_fight = 'It takes a last breath and dies'
        self.won_fight = 'The last what you see of it are its evil eyes'

    def attack():
        print('The monster attacks')

    def take_hit():
        print('The monster takes a hit')

    def loot():
        print('You find nothing of interest')
