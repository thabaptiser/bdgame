class Cursor:
    def __init__(self, stdscr):
        self.x = xLimit//2
        self.y = yLimit//2
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
