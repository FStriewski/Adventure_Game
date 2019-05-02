# This is the root file that starts the game
import char

# create an instance of the Character class:


def char_selector():
    char_selection = input('''--> Select a character: \n
      A) The Adventurer \n
      B) The Mechanic \n
      C) The Zookeeper \n
      ''')

    if (char_selection.upper() == 'A'):
        return char.Character()
    elif (char_selection.upper() == 'B'):
        return char.Mechanic()
    elif (char_selection.upper() == 'C'):
        return char.Zookeeper()
    else:
        print('Input must be A, B or C')
        char_selector()


character = char_selector()
character.name = input('Enter a name: \n')
character.stats()
character.print_description()
character.print_inventory()
