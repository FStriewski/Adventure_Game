# This is the root file that starts the game
import char

# create an instance of the Character class:
character = char.Mechanic()


print('Create a new character: ')

character.name = input('Enter a name: ')
character.stats()
