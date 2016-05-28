def create_soldier(token):
    url = "http://52.34.125.56:8080/unit/create"
    data = json.dumps({'token': token}).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)

def move_soldier(token, stdscr, key):
    stdscr.addch(self.y+(yLimit//2), self.x+(xLimit//2), " ")
    self.x = x - offset[0]
    self.y = offset[1] - y
    stdscr.addch(self.y + (yLimit//2),self.x + (xLimit//2),'#')
    move = {"direction":key_dir(key)}
    send_data(move)
    # receive information to update display
    response = receiveData()
    url = "http://52.34.125.56:8080/unit/move"
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
 
