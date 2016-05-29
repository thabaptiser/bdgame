import curses
import json
import sys
import urllib.request

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from curses import wrapper

from cursor import Cursor
from grid import Grid
from soldier import create_soldier, move_soldier

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.clear()
curses.curs_set(0)
yLimit = curses.LINES - 1
xLimit = curses.COLS - 1
directions = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]

def main(stdscr):
    cursor = Cursor(stdscr)
    url = "http://52.34.125.56:8080/token/get"
    data = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    token = json.loads(response.read().decode("utf-8"))['token'] 
    grid = Grid(stdscr)
    while True:
        key = stdscr.getch() 
        if key == ord('q'):
            exit(stdscr)
        elif key == ord('c'):
            create_soldier(token)
            grid.display()
        elif key in directions:
            cursor.remove(stdscr)
            cursor.move_cursor(stdscr, key)
            cursor.display(stdscr)
        elif key == ord('s'):
            key = stdscr.getch()
            if key in directions:
                move_soldier(stdscr, key)
                grid.display()

def exit(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    sys.exit(0)


def normalize_coords(x, y, offset_x, offset_y):


curses.wrapper(main)


