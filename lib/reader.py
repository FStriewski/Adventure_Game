# Used to read text from files


def read(path, key):
    with open(path, 'r') as file:
        print(file.readlines())
