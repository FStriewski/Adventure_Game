# Used to read text from files
import os
from time import sleep


def find_line(key, path):
    parsed_line = [line for line in path if key in line]
    if parsed_line != []:
        return parsed_line
    else:
        return 'Output Error: Key not found'


def read(path, id):
    key = '{{{}}}'.format(id)
    if (key.length != 4):
        print('ERROR: Malformed key')
        return None

    with open(path, 'r') as file:
        for line in find_line(key, file):
            text = line[6:]
            print(text)


def parse(path, id):
    key = '{{{}}}'.format(id)
    with open(path, 'r') as file:
        for line in find_line(key, file):
            text = line[6:]
            return text


def timeout(s):
    sleep(s)


def clear():
    os.system('clear||cls')
    timeout(3)
