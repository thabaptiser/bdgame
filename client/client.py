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
            start = cursor.position()
            end = cursor.position()
            cursor.select(start)
            grid.debug("hello")
            while key is not ord('s'):
                key = stdscr.getch()
                if key in directions:
                    if key == KEY_RIGHT:
                        end[0] += 1
                    elif key == KEY_LEFT:
                        end[0] -= 1
                    elif key == KEY_UP:
                        end[1] -= 1
                    elif key == KEY_DOWN:
                        end[1] += 1
                stdscr.clear()
                grid.debug(str(cursor.sel_bool))
                cursor.display()
                grid.display()
            cursor.deselect()
            x_r = sorted((start[0], end[0]))
            y_r = sorted((start[1], end[1]))
            sel_soldiers = []
            for x in range(x_r[0], x_r[1]):
                for y in range(y_r[0], y_r[1]):
                    if (x,y) in grid.grid['soldiers']:
                        sel_soldiers.append((x,y))
        elif key == ord('m'):
            dest = utils.normalize_coords(cursor.position())
            move_soldiers(dest, sel_soldiers)
        elif key == ord('d'):
            raise Exception(grid.request())
        stdscr.clear()
        cursor.display()
        grid.display()

def exit(stdscr):
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    sys.exit(0)

curses.wrapper(main)


