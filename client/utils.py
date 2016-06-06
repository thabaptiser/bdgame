import json
import urllib.request

def key_dir(key):
    if key == KEY_UP:
        return 0
    elif key == KEY_RIGHT:
        return 1
    elif key == KEY_DOWN:
        return 2
    elif key == KEY_LEFT:
        return 3

def normalize_coords(top_left, position):
    return (position[0] - top_left[0] , top_left[1] - position[1])

def request(url, data=None):
    data = json.dumps(data).encode('utf-8') if data else None
    req = urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req).read().decode("utf-8")
    if len(response):
        return json.loads(response)

