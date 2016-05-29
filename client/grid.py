import json
import urllib.request

class Grid:
    def __init__(self, stdscr, x_limit, y_limit, directions):
        self.stdscr = stdscr
        self.x_Limit = x_limit
        self.y_Limit = y_limit
        self.directions = directions

    def request(self):
        url = "http://52.34.125.56:8080/grid"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        return json.loads(response.read().decode("utf-8"))

    def display(self):
        grid = self.request()
        for soldier in grid['soldiers']:
            new_coords = normalize_coords(soldier[0], soldier[1], )
            stdscr.addch(new_coords[0], new_coords[1], '#')
        stdscr.refresh()


