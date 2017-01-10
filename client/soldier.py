import utils

def create_soldier(token):
    url = utils.ip + "unit/create"
    utils.request(url, data={'token': token})

def move_soldiers(dest, sel_soldiers):
    url = utils.ip + "unit/move"
    utils.request(url, data={'destination': dest, 'soldiers': sel_soldiers})

