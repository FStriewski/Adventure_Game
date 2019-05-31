# Used to read text from files
import os
from time import sleep


def find_line(key, path):
    return [line for line in path if key in line]


def read(path, key):
    if (key.length != 6):
        print('ERROR: Malformed key')
        return None

    with open(path, 'r') as file:
        for line in find_line(key, file):
            text = line[6:]
            print(text)


def parse(path, key):
    with open(path, 'r') as file:
        for line in find_line(key, file):
            text = line[6:]
            return text


def timeout(s):
    sleep(s)


def clear():
    os.system('clear||cls')
    timeout(3)
