# This is the root file that starts the game
import char
from lib import reader
from monster import Monster
# create an instance of the Character class:

state = {
    'visited_rooms' : []
}

reader.read('./txt/story_line.txt', '{SL01}')

state['visited_rooms'].append('1')

print(len(state['visited_rooms']))

# character = char.char_selector()
# character.stats()
# character.print_description()
# character.print_inventory()
