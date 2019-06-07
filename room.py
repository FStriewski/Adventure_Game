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
        self.description = reader.parse(self.PATH, ''.join((room_id, 'D')))
        self.visited = 'false'
        self.room_id = room_id
        self.connectors = None  # Connectors(room_id)
        self.choices = Choices(room_id).choices

    def init_room(self):
        self.set_visited()
        print(self.name)
        print(self.description)

    def set_visited(self):
        self.visited = 'true'

    def exhaust_choice(self, id):
        for choice in self.choices:
            if choice['id'] == id:
                choice['exhausted'] = 'true'

    def get_choices(self):
        gen = (choice for choice in self.choices if choice['exhausted'] != 'true')
        sel_list = []
        selection = ''

        for choice in gen:
            sel_list.append(choice['id'])
            print(choice['id'] + '    ' + choice['descriptor'])
        while selection.upper() not in sel_list:
            selection = input('Select: ')
            self.exhaust_choice(selection)
        return None


def stage_loader(room_id):
    # state.push(room_id) - use for count and blocking revisits
    stage = Room(room_id)
    stage.init_room()
    stage.get_choices()
