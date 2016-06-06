import utils

def create_soldier(token):
    url = "http://52.34.125.56:8080/unit/create"
    utils.request(url, data={'token': token})

def move_soldier(token, stdscr, key):
    move = {"direction": utils.key_dir(key)}
    url = "http://52.34.125.56:8080/unit/move"
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)

