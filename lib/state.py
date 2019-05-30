
node = {
    room_id: '', # roomid
    visited: false # bool
}

room = {
    initial_description: '', #string
    connectorA: '',
    connectorB: '',
    connectorC: '',

}



state = {
    'visited_rooms': []
}


def room_reducer(state, id):
    state['visited_rooms'].append(id)
