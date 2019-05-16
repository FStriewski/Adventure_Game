import dice


class Monster():
    def __init__(self, life, strength, inventory):
        self.life = life
        self.initial_life = self.life
        self.strength = strength
        self.inventory = inventory
        self.description = 'A generic monster.'
        self.lost_fight = 'It takes a last breath and dies.'
        self.won_fight = 'The last what you see of it are its evil eyes.'

    def attack(self):
        print('The monster attacks')

    def loot(self):
        print('You find nothing of interest')

    def take_hit(self, value):
        self.life -= value
        if (self.life > 0):
            print('The monster takes a hit and has {}/{} health left.'
                  .format(self.life, self.initial_life))
        else:
            print(self.lost_fight)
            self.loot()


Ghoule = Monster(5, 5, [])
