import curses
import utils
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from grid import Grid

# cursor coordinates not normalized
class Cursor:
    def __init__(self, stdscr):
        self.x = 0
        self.y = 0
        self.stdscr = stdscr
        self.sel_bool = False
        self.select_coords = (0, 0)
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    def position(self):
        return [self.x, self.y]

    def display(self, grid):
        if self.sel_bool:
            x_r = sorted((self.x, self.select_coords[0]))
            y_r = sorted((self.y, self.select_coords[1]))
            for x in range(x_r[0], x_r[1]+1):
                for y in range(y_r[0], y_r[1]+1):
                    new_coords = utils.normalize_coords(grid.top_left, (x, y))
                    self.stdscr.addstr(new_coords[1], new_coords[0], " ", curses.color_pair(1))
        
        new_coords = utils.normalize_coords(grid.top_left, (self.x, self.y))
        self.stdscr.addch(new_coords[1], new_coords[0], "+")
    
    def move_cursor(self, key):
        if key == KEY_DOWN:
            self.y -= 1
        elif key == KEY_UP:
            self.y += 1
        elif key == KEY_LEFT:
            self.x -= 1
        elif key == KEY_RIGHT:
            self.x += 1
    
    # select using the cursor
    def select(self):
        self.sel_bool = True
        self.select_coords = (self.x, self.y)
    
    # deselect soldiers using the cursor
    def deselect(self):
        self.sel_bool = False
