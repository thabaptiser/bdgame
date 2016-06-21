import curses
import sys

import utils
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from curses import wrapper

from cursor import Cursor
from grid import Grid
from soldier import create_soldier, move_soldiers

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
    grid = Grid(stdscr, x_limit, y_limit)
    while True:
        key = stdscr.getch() 
        if key == ord('q'):
            exit(stdscr)
        elif key == ord('c'):
            create_soldier(token)
        elif key in directions:
            cursor.move_cursor(key)
        elif key == ord('s'):
            cursor.select()
            key = ord('m')
            while key is not ord('s') or key is not ord('q'):
                stdscr.clear()
                cursor.display()
                grid.display()
                key = stdscr.getch()
                if key in directions:
                    cursor.move_cursor(key)
            if key is ord('s'):
                cursor.deselect()
                x_r = sorted((cursor.select_coords[0], cursor.x))
                y_r = sorted((cursor.select_coords[1], cursor.y))
                sel_soldiers = []
                for x in range(x_r[0], x_r[1]):
                    for y in range(y_r[0], y_r[1]):
                        if (x,y) in grid.grid['soldiers']:
                            sel_soldiers.append((x,y))
                key = 0
            if key is ord('q'):
                exit(stdscr)
        elif key == ord('m'):
            if sel_soldiers:
                dest = utils.normalize_coords(cursor.position())
                move_soldiers(dest, sel_soldiers)
            else:
                stdscr.addstr(y_limit-1, 0, "no soldiers selected")
                key = 0
       # elif key == ord('d'):
        #    raise Exception(grid.request())
        stdscr.clear()
        cursor.display()
        grid.display(key)

def exit(stdscr):
    stdscr.clear()
    stdscr.addstr(y_limit//2, x_limit//2, "Are you sure you want to quit? (y or n)")
    key = stdscr.getch()
    if key == ord('y'):
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit(0)

curses.wrapper(main)


