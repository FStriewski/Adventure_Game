# Room definition


class Room():
    def __init__(self, name):
        self.name = name
        self.description = ''
        self.id = ''


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
