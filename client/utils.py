import json
import urllib.request

from curses import KEY_UP, KEY_RIGHT, KEY_DOWN, KEY_LEFT

def normalize_coords(top_left, position):
    return (position[0] - top_left[0] , top_left[1] - position[1])

def request(url, data=None):
    data = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req).read().decode("utf-8")
    if len(response):
        return json.loads(response)

