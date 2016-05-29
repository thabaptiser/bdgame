import curses
import sys

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
y_limit = curses.LINES - 1
x_limit = curses.COLS - 1
directions = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]

def main(stdscr):
    cursor = Cursor(stdscr)
    url = "http://52.34.125.56:8080/token/get"
    token = utils.request(url)['token']
    grid = Grid(stdscr, x_limit, y_limit, directions)
    while True:
        key = stdscr.getch() 
        if key == ord('q'):
            exit(stdscr)
        elif key == ord('c'):
            create_soldier(token)
        elif key in directions:
            cursor.move_cursor(key)
        elif key == ord('s'):
            key = stdscr.getch()
            if key in directions:
                move_soldier(stdscr, key)
        stdscr.clear()
        grid.display()
        cursor.display()
        stdscr.refresh()

def exit(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    sys.exit(0)

curses.wrapper(main)


