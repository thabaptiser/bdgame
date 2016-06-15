import utils

def create_soldier(token):
    url = "http://52.34.125.56:8080/unit/create"
    utils.request(url, data={'token': token})

def move_soldiers(dest, sel_soldiers):
    url = "http://52.34.125.56:8080/unit/move"
    utils.request(url, data=move)
    response = utils.request(url)

