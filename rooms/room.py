# Room definition
from lib import reader


class Choices():
    PATH = './txt/rooms.txt'

    def __init__(self, room_id):

        self.room_id = room_id
        self.choices = [
            {
             'id': 'A',
             'descriptor': self.reader_lookup('A'),
             'description': self.reader_lookup('X'),
             'exhausted': 'false',
             },
            {
             'id': 'B',
             'descriptor': self.reader_lookup('B'),
             'description': self.reader_lookup('Y'),
             'exhausted': 'false',
            },
            {
             'id': 'C',
             'descriptor': self.reader_lookup('C'),
             'description': self.reader_lookup('Z'),
             'exhausted': 'false',

            }
        ]

    def reader_lookup(self, id):
        return reader.parse(self.PATH, ''.join((self.room_id, id)))


class Room():
    PATH = './txt/rooms.txt'

    def __init__(self, room_id):
        self.name = reader.parse(self.PATH, ''.join((room_id, 'N')))
        self.description = reader.parse(self.PATH, ''.join((room_id, 'N')))
        self.visited = 'false'
        self.room_id = room_id
        self.connectors = []  # Connectors(room_id)
        # is static, doesn't update state
        self.choices = Choices(room_id).choices

    def set_visited(self):
        self.visited = 'true'

    def exhaust(self, id):
        for choice in self.choices:
            if choice['id'] == id:
                choice['exhausted'] = 'true'

    def get_choices(self):
        gen = (choice for choice in self.choices if choice['exhausted'] != 'true')
        selection = ''

        for choice in gen:
            print(choice['id'] + '    ' + choice['descriptor'])
# needs to exclude exhausted items of gen instead static list
        while selection.upper() not in ['A', 'B', 'C']:
            selection = input('Select: ')
            self.exhaust(selection)

#        for choice in self.choices:
#            print(choice['exhausted'])
# reader.read(self.PATH, 'KEY')
        # user pick choice - choices.exhaust(id)


class Lobby(Room):
    def __init__(self):
        self.name = 'Lobby'
        self.description = 'First Lobby'
        self.id = 'X01'


class Lobby_2(Room):
    def __init__(self):
        self.name = 'Lobby2'
        self.description = 'Second Lobby'
        self.id = 'X02'
