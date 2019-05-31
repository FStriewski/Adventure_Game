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
             'exhausted': 'false',
             },
            {
             'id': 'B',
             'descriptor': self.reader_lookup('B'),
             'exhausted': 'false',
            },
            {
             'id': 'C',
             'descriptor': self.reader_lookup('C'),
             'exhausted': 'false',

            }
        ]

    def reader_lookup(self, id):
        return reader.parse(self.PATH, ''.join((self.room_id, id)))

    def exhaust(self, id):
        self.id['exhausted'] = 'true'


class Room():
    PATH = './txt/rooms.txt'

    def __init__(self, room_id):
        self.name = reader.parse(self.PATH, ''.join((room_id, 'N')))
        self.description = reader.parse(self.PATH, ''.join((room_id, 'N')))
        self.visited = 'false'
        self.room_id = room_id
        self.connectors = []  # Connectors(room_id)
        self.choices = Choices(room_id).choices

    def set_visited(self):
        self.visited = 'true'

    def get_choices(self):
        # if 2/3 choices exhausted, reroute

        for choice in self.choices:
            print(choice['descriptor'])
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
