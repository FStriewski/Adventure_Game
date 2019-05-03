# Used to read text from files
import os
from time import sleep


def read(path, key):
    with open(path, 'r') as file:
        print(file.readlines())


def timeout(s):
    sleep(s)


def clear():
    os.system('clear||cls')
    timeout(3)
