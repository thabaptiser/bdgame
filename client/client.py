import curses
from curses import wrapper
import json
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import urllib.request

offset = [0,0]   
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
# Clear screen
stdscr.clear()
curses.curs_set(2)

yLimit = curses.LINES - 1
xLimit = curses.COLS - 1
directions = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]

def main(stdscr):
    stdscr.move(yLimit//2,xLimit//2)       
    while True:
        # get direction to move soldier
        key = stdscr.getch() 
        if key == ord('q'):
            exit(stdscr)
        elif key == ord('c'):
            createSoldier()
            soldier = receiveSoldier()
        elif key in directions:
            moveCursor(stdscr,key)
        elif key == ord('s'):
            key = stdscr.getch()
            if key in directions:
                moveSoldier(stdscr,key)
        stdscr.refresh()

def extra():
    move = {"direction":keyDir(key)}
    sendData(move)
    # receive information to update display
    response = receiveData()
    soldier.moveSoldier(stdscr, response["units"][0][0], response["units"][0][1])
    stdscr.refresh()
    url = "http://52.34.125.56:8080/unit/move"
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)

def moveCursor(stdscr,key):
    cursorPos = stdscr.getyx()
    if key == KEY_DOWN:
        stdscr.move(cursorPos[0]+1,cursorPos[1])
    elif key == KEY_UP:
        stdscr.move(cursorPos[0]-1,cursorPos[1])
    elif key == KEY_LEFT:
        stdscr.move(cursorPos[0],cursorPos[1]-1)
    elif key == KEY_RIGHT:
        stdscr.move(cursorPos[0],cursorPos[1]+1)
    stdscr.refresh()

def receiveSoldier():
    url = "http://52.34.125.56:8080/grid"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return json.loads(response.read().decode("utf-8"))
    
def createSoldier():
    url = "http://52.34.125.56:8080/unit/create"
   # data = json.dumps().encode('utf-8')
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)

def moveSoldier(stdscr,key):
    stdscr.addch(self.y+(yLimit//2), self.x+(xLimit//2), " ")
    self.x = x - offset[0]
    self.y = offset[1] - y
    stdscr.addch(self.y + (yLimit//2),self.x + (xLimit//2),'#')
  
def keyDir(key):
    if key == KEY_UP:
        return 0
    elif key == KEY_RIGHT:
        return 1
    elif key == KEY_DOWN:
        return 2
    elif key == KEY_LEFT:
        return 3

def exit(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main(stdscr))


