import curses
from curses import wrapper
import json
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import urllib.request
import sys
from soldier import create_soldier, move_soldier

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
# Clear screen
stdscr.clear()
curses.curs_set(0)

yLimit = curses.LINES - 1
xLimit = curses.COLS - 1
directions = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]
offset = [0, 0]

def main(stdscr):
    cursor = Cursor(stdscr)
    url = "http://52.34.125.56:8080/token/get"
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    token = json.loads(response.read().decode("utf-8"))['token'] 
    while True:
        grid = get_grid()
        # get direction to move soldier
        key = stdscr.getch() 
        if key == ord('q'):
            exit(stdscr)
        elif key == ord('c'):
            create_soldier(token)
            grid = get_grid()
            display_grid(grid, stdscr)
        elif key in directions:
            cursor.remove(stdscr)
            cursor.move_cursor(stdscr, key)
            cursor.display(stdscr)
        elif key == ord('s'):
            key = stdscr.getch()
            if key in directions:
                move_soldier(stdscr, key)
                grid = get_grid()
                display_grid(grid, stdscr)


class Cursor:
    def __init__(self, stdscr):
        self.x = xLimit//2
        self.y = yLimit//2
        self.display(stdscr)

    def remove(self, stdscr):
        stdscr.addch(self.y, self.x, " ")
        stdscr.refresh()

    def display(self, stdscr):
        stdscr.addch(self.y, self.x, "+")
        stdscr.refresh()

    def move_cursor(self, stdscr, key):
        if key == KEY_DOWN:
            self.y += 1
        elif key == KEY_UP:
            self.y -= 1
        elif key == KEY_LEFT:
            self.x -= 1
        elif key == KEY_RIGHT:
            self.x += 1


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
 
def get_grid():
    url = "http://52.34.125.56:8080/grid"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return json.loads(response.read().decode("utf-8"))

def display_grid(grid, stdscr):
    for soldier in grid['soldiers']:
        new_coords = normalize_coords(soldier[0], soldier[1], )
        stdscr.addch(new_coords[0], new_coords[1], '#')
    stdscr.refresh()

def normalize_coords(x, y, offset_x, offset_y):
    

def key_dir(key):
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
    sys.exit(0)

curses.wrapper(main)


