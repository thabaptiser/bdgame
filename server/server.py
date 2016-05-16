import falcon
import json
from collections import namedtuple
import random

units = {}

class Unit():
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id

def add_unit(max_id):
    units[max_id] = Unit(0, 0, max_id)
    return max_id + 1

#def get_num_at_end_of_branch(branch):
#    if branch % 2 == 0:
#        x = branch//2
#        return (x) * (x+1)
#    else:
#        x = branch//2
#        return (x) * (x+1) + (branch+1)//2

#def get_curve_position(x, y):
#    """
#    given an x and y, gives you the integer location on the space filling curve
#    """
#    ya = int(abs(y))
#    xa = int(abs(x))
#    horizontal = False
#    vertical = False
#    if xa >= ya:
#        vertical = True
#        if x > 0:
#            branch = 4*x-2
#            if y < 0:
#                if ya == x:
#                    vertical = False
#                    horizontal = True
#                branch += 1
#        else:
#            branch = 4*xa
#    elif ya > xa:
#        horizontal = True
#        if y > 0:
#            branch = 4*y-3
#        else:
#            branch = 4*ya-1
#    last_corner = get_num_at_end_of_branch(branch)
#    if horizontal and y > 0:
#        total_num = last_corner + x + y - 1
#    elif horizontal and y < 0:
#        total_num = last_corner + ya - x
#    elif vertical and x > 0:
#        total_num = last_corner + (x-y)
#    elif vertical and x < 0:
#        total_num = last_corner + xa + y
#    elif x == y == 0:
#        return 0
#    return total_num

def get_x_y_position(curve_pos):
    """
    gets your position given your position on the curve
    """
    

level_array = {}
def generate_map(x, y):
    for i in range(x):
        for j in range(y):
            z = random.randrange(0, 10)
            if any([level_array.get(get_curve_position(i+a, j+b)) for a in range(-1, 2) for b in range(-1, 2)]):
                if z <=5:
                    z = 1
            if z >= 3:
                z = 3
            level_array[get_curve_position(i, j)] = z
    print(level_array)
            #r.set(get_curve_position(i, j), z)
            
class MoveUnitResource:
    def on_post(self, req, resp):
        """Handles post requests"""
        req_json = json.loads(req.stream.read().decode('utf-8'))
        direction = req_json['direction']
        id = req_json['id']
        if direction == 0:
            units[id].y += 1
        elif direction == 1:
            units[id].x += 1
        elif direction == 2:
            units[id].y -= 1
        elif direction == 3:
            units[id].x -= 1
        resp.status = falcon.HTTP_200

class CreateUnitResource:
    max_id = 0
    def on_get(self, req, resp):
        self.max_id = add_unit(self.max_id)

class GetGridResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({'units': {str(id): (unit.x, unit.y) for unit in units.values()}})

api = falcon.API()
api.add_route('/unit/move', MoveUnitResource())
api.add_route('/unit/create', CreateUnitResource())
api.add_route('/grid', GetGridResource())
