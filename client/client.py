import curses
import sys

import utils
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from curses import wrapper

from cursor import Cursor
from grid import Grid
from soldier import create_soldier, move_soldiers

import signal
import sys

def signal_handler(signal, frame):
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Initialize screen and keyboard
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.clear()
curses.curs_set(0)
y_limit = curses.LINES - 1
x_limit = curses.COLS - 1
directions = [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]

# open debug file
debug_file = open("debug.out", "a")

def main(stdscr):
    cursor = Cursor(stdscr)
    url = utils.ip + "token/get"
    token = utils.request(url)['token']
    grid = Grid(stdscr, x_limit, y_limit, cursor)
 
    sel_bool = False
    sel_soldiers = []
    
    while True:
        key = stdscr.getch()

        # quit game
        if key == ord('q'):
            exit(stdscr)
    
        # create soldier
        elif key == ord('c'):
            create_soldier(token)
        
        # move cursor
        elif key in directions:
            cursor.move_cursor(key)
        
        # select tiles
        elif key == ord('s') and not sel_bool:
            cursor.select()
            key = 0
            sel_bool = True
            sel_soldiers = []

        # finish selecting
        elif key is ord('s') and sel_bool:
            cursor.deselect()
            x_r = sorted((cursor.select_coords[0], cursor.x))
            y_r = sorted((cursor.select_coords[1], cursor.y))
            debug_file.write(str(x_r) + "\n" + str(y_r) + "\n")
            for x in range(x_r[0], x_r[1]+1):
                for y in range(y_r[0], y_r[1]+1):
                    if (x,y) in grid.grid:
                        debug_file.write("inserting")
                        sel_soldiers.append(grid.grid[(x,y)])
            sel_bool = False
        if key is ord('q'):
            exit(stdscr)
    
        # move soldiers (soldiers must be selected first)
        elif key == ord('m'):
            key = 69
            debug_file.write(str(sel_soldiers))
            if sel_soldiers:
                debug_file.write("moving soldiers\n")   
                move_soldiers(cursor.position(), sel_soldiers)
                sel_bool = False
        elif key == ord('d'):
            raise Exception(grid.request())
        
        grid.debug(str(key))
        grid.update(key, sel_bool)
        grid.display()

# exit the game
def exit(stdscr):
    stdscr.clear()
    stdscr.addstr(y_limit//2, x_limit//2 - 15, "Are you sure you want to quit? (y or n)")
    key = stdscr.getch()
    if key == ord('y'):
        curses.nocbreak()
        stdscr.keypad(False)
        curses.echo()
        curses.endwin()
        sys.exit(0)

# run the game
curses.wrapper(main)


