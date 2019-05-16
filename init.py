# This is the root file that starts the game
import char
from lib import reader
from monster import Monster, Ghoule
# create an instance of the Character class:

reader.read('./txt/story_line.txt', '{SL01}')

Ghoule.attack()

character = char.char_selector()
character.stats()
character.print_description()
character.print_inventory()
