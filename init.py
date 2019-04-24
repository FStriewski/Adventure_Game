# This is the root file that starts the game
import dice
import char


character = char.Character('', 0, 0, []  )


print('Create a new character: ')

character.name = input('Enter a name: ')
character.life = 60
character.strength = 10 + dice.dice_d(3,3)
# character.getvalues()
print('Your chars name is {} with {} life and {} strength'.format(character.name,
                                                                   character.life,
                                                                   character.strength))




#dice.dice_d6()
