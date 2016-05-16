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

def main(stdscr):
   while True:
        # get direction to move soldier
        key = stdscr.getch()
        move = {"direction":keyDir(key)}
        sendData(move)
        # receive information to update display
        response = receiveData()
        displaySoldier(stdscr,response["units"][0][0], response["units"][0][1])
        stdscr.refresh()

def receiveData():
    url = "http://52.34.125.56:8080/grid"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return json.loads(response.read().decode("utf-8"))
    
def sendData(data):
    url = "http://52.34.125.56:8080/unit/move"
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)

def displaySoldier(stdscr,x,y):
    x = x - offset[0]
    y = offset[1] - y
    stdscr.addch(y + (yLimit//2),x + (xLimit//2),'#')

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

wrapper(main)


