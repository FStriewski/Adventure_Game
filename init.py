# This is the root file that starts the game
import dice
import char

character = char.character

print('Create a new character: ')

character['name'] = input('Enter a name: ')
character['life'] = 60
character['strength'] = 10 + dice.dice_d(3,3)

print('Your chars name is {} with {} life and {} strength'.format(character['name'],
                                                                  character['life'],
                                                                  character['strength']))




#dice.dice_d6()
