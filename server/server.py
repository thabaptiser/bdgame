import falcon
import json
from collections import namedtuple

Unit = namedtuple('Unit', ['x', 'y'])
unit = Unit(0,0)

class MoveUnitResource:
    def on_post(self, req, resp):
        """Handles post requests"""
        req_json = json.loads(req.stream.read())
        direction = req_json['direction']
        if direction == 0:
            unit.x += 1
        elif direction == 1:
            unit.y += 1
        elif direction == 2:
            unit.x -= 1
        elif direction == 3:
            unit.y -= 1
        unit = req_json['unit_id']
        resp.status = HTTP_200

class GetGridResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({'units': [(unit.x, unit.y)]})

api = falcon.API()
api.add_route('/unit/move', MoveUnitResource())
api.add_route('/grid', GetGridResource())
