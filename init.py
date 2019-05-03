# This is the root file that starts the game
import char
from lib import reader
# create an instance of the Character class:

reader.read('./txt/story_line.txt', 0)

character = char.char_selector()
# character.name = input('Enter a name: \n')
character.stats()
character.print_description()
character.print_inventory()
