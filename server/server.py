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
    s.units[max_id] = Unit(0, 0, max_id)
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
            s.units[id].y += 1
        elif direction == 1:
            s.units[id].x += 1
        elif direction == 2:
            s.units[id].y -= 1
        elif direction == 3:
            s.units[id].x -= 1
        resp.status = falcon.HTTP_200

class CreateUnitResource:
    def on_get(self, req, resp):
        s.max_id = add_unit(s.max_id)

class GetGridResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({'units': {str(id): (units[id].x, units[id].y) for id in s.units}})

api = falcon.API()
s = ServerClass()
api.add_route('/unit/move', MoveUnitResource())
api.add_route('/unit/create', CreateUnitResource())
api.add_route('/grid', GetGridResource())
