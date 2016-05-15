import curses
from curses import wrapper
import json
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
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
#        key = stdscr.getch()
 #       if key == ord('q'):
  #          exit(stdscr)
        url = "http://52.34.125.56/grid"
        newDirection = {"direction":0}
        params = json.dumps(newDirection).encode('utf8')
        req = urllib.request.Request(url, data=params)
        response = urllib.request.urlopen(req)
#        print(response.read().decode('utf8'))
#        if key in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 'q']:
#           if key == q:
#                exit(stdscr)
#            elif key == KEY_LEFT:
#                stdscr.move(
        stdscr.refresh()

def request(url, dic):

def displaySoldier(stdscr,y,x):
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


