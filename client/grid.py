import threading
import utils

class Grid:
    def __init__(self, stdscr, x_limit, y_limit, cursor):
        self.stdscr = stdscr
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.top_left = (-20, 20)   # top left of screen for normalization
        threading.Thread(target=self.refresh, daemon=True).start()
        self.grid = {}
        self.cursor = cursor
        self.cur_key = 0
        self.sel_bool = False
        self.displaying = False

    # continually refresh the grid from the server
    def refresh(self):
        while True: 
            data = self.request()
            self.grid = {}
            for i in range(0,len(data['soldiers'])):
                key = (data['soldiers'][i][0], data['soldiers'][i][1])
                self.grid[key] = data['soldiers'][i][2]
            self.display()
                           
    @property
    def bottom_right(self):
        return (self.top_left[0] + self.x_limit, self.top_left[1] - self.y_limit)

    # update values from user
    def update(self, key, select_bool):
        self.cur_key = key
        self.sel_bool = select_bool

    # request grid from the server
    def request(self):
        url = utils.ip + "grid"
        data = {'screen': (self.top_left, self.bottom_right)}
        return utils.request(url, data)

    # display current actions to the screen
    def display(self):
        if self.displaying == False:
            self.displaying = True
        else:
            return

        self.stdscr.clear()

        for soldier in self.grid:
                new_coords = utils.normalize_coords(self.top_left, (soldier[0], soldier[1]))
                self.stdscr.addch(new_coords[1], new_coords[0], '#')
  
        self.cursor.display(self)

        if self.cur_key is ord('m'):
            if self.sel_bool:
                self.stdscr.addstr(self.y_limit-1, 0, "moving soldiers")
            else:
                self.stdscr.addstr(self.y_limit-1, 0, "no soldiers selected")
        elif self.cur_key is ord('s'):
            self.stdscr.addstr(self.y_limit-1, 0, "selecting")
        if self.sel_bool:
            self.stdscr.addstr(self.y_limit-1, 0, "soldier(s) selected")
        self.displaying = False   
     
    def debug(self, string):
        self.stdscr.addstr(25, 0, string)
