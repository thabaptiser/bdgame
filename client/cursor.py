from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from grid import Grid

class Cursor:
    def __init__(self, stdscr):
        self.x = 0
        self.y = 0
        self.stdscr = stdscr

    def display(self):
        self.stdscr.addch(self.y, self.x, "+")

    def move_cursor(self, key):
        if key == KEY_DOWN:
            self.y += 1
        elif key == KEY_UP:
            self.y -= 1
        elif key == KEY_LEFT:
            self.x -= 1
        elif key == KEY_RIGHT:
            self.x += 1

