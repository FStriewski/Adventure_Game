state = {
    'visited_rooms': []
}


def room_reducer(state, id):
    state['visited_rooms'].append(id)
