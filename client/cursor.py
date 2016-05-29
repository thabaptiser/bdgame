from grid import Grid

class Cursor:
    def __init__(self, stdscr):
        self.x = Grid.x_limit//2
        self.y = Grid.y_limit//2
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
d
