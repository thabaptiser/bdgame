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

class ServerClass():
    max_id = 0
    units = {}

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
        def on_get(self, req, resp):
            max_id = add_unit(self.max_id)

    class GetGridResource:
        def on_get(self, req, resp):
            resp.body = json.dumps({'units': {str(id): (unit.x, unit.y) for unit in units.values()}})

api = falcon.API()
s = ServerClass()
api.add_route('/unit/move', s.MoveUnitResource())
api.add_route('/unit/create', s.CreateUnitResource())
api.add_route('/grid', s.GetGridResource())
