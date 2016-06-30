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
            data = self.request()
            self.grid = {}
            for i in range(0,len(data['soldiers'])):
                key = (data['soldiers'][i][0], data['soldiers'][i][1])
                self.grid[key] = data['soldiers'][i][2]
    
    @property
    def bottom_right(self):
        return (self.top_left[0] + self.x_limit, self.top_left[1] - self.y_limit)

    def request(self):
        url = "http://52.34.125.56:8080/grid"
        data = {'screen': (self.top_left, self.bottom_right)}
        return utils.request(url, data)

    def display(self, cur_key, sel_bool=False):
        for soldier in self.grid:
            new_coords = utils.normalize_coords(self.top_left, (soldier[0], soldier[1]))
            self.stdscr.addch(new_coords[1], new_coords[0], '#')
        if cur_key is ord('m'):
            if sel_bool:
                self.stdscr.addstr(self.y_limit-1, 0, "moving")
            else:
                self.stdscr.addstr(self.y_limit-1, 0, "no soldiers selected")
        elif cur_key is ord('s'):
            self.stdscr.addstr(self.y_limit-1, 0, "selecting")
        if sel_bool:
            self.stdscr.addstr(self.y_limit-1, 0, "soldier(s) selected")

    def debug(self, string):
        self.stdscr.addstr(25, 0, string)
