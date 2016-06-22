import threading
import utils

class Grid:
    def __init__(self, stdscr, x_limit, y_limit):
        self.stdscr = stdscr
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.top_left = (-20, 20)
        threading.Thread(target=self.refresh, daemon=True).start()
        self.grid = {}

    def refresh(self):
        while True:
            self.grid = self.request()
    
    @property
    def bottom_right(self):
        return (self.top_left[0] + self.x_limit, self.top_left[1] - self.y_limit)

    def request(self):
        url = "http://52.34.125.56:8080/grid"
        data = {'screen': (self.top_left, self.bottom_right)}
        return utils.request(url, data)

    def display(self, cur_key, sel_bool):
        for soldier in self.grid['soldiers']:
            new_coords = utils.normalize_coords(self.top_left, (soldier[0], soldier[1]))
            self.stdscr.addch(new_coords[1], new_coords[0], '#')
        if cur_key:
            if cur_key is ord('m'):
                self.stdscr.addstr(self.y_limit-1, 0, "move")
            elif cur_key is ord('s'):
                self.stdscr.addstr(self.y_limit-1, 0, "select")
        if sel_bool:
            self.stdscr.addstr(self.y_limit-1, 0, "soldier(s) selected")

    def debug(self, string):
        self.stdscr.addstr(self.y_limit-1, 0, string)
