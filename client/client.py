import curses
from curses import wrapper
import json
import urllib.request

def main(stdscr):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    # Clear screen
    stdscr.clear()
    curses.curs_set(2)
    while True:
        cursorPos = stdscr.getyx()
        key = stdscr.getch()
        
        
        newDirection = {"direction":keyDir(key)}
        params = json.dumps(newDirection).encode('utf8')
        req = urllib.request.Request
#        if key in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 'q']:
#           if key == q:
#                exit(stdscr)
#            elif key == KEY_LEFT:
#                stdscr.move(
#        stdscr.refresh()

def displaySoldier(stdsc,y,x):
    stdscr.addch(y,x,'#')

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


