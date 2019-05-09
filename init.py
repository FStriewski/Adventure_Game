# This is the root file that starts the game
import char
from lib import reader
from monster import Monster
# create an instance of the Character class:

reader.read('./txt/story_line.txt', '{SL01}')

# character = char.char_selector()
# character.stats()
# character.print_description()
# character.print_inventory()
current_monster = Monster()
current_monster.take_hit(4)
current_monster.take_hit(20)
