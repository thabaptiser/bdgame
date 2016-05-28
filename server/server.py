import falcon
import json
import uuid

class Unit():
    def __init__(self, x, y, id, token):
        self.x = x
        self.y = y
        self.id = id
        self.token = token

    def check_auth(self, token):
        return self.token == token

    def move(self, direction, token):
        if not self.check_auth(token):
            return
        if direction == 0:
            s.units[i].y += 1
        elif direction == 1:
            s.units[i].x += 1
        elif direction == 2:
            s.units[i].y -= 1
        elif direction == 3:
            s.units[i].x -= 1

def add_unit(max_id, token):
    s.units[str(max_id)] = Unit(0, 0, max_id, token)
    return max_id + 1

class ServerClass:
    max_id = 0
    units = {}

class CreateAuthTokenResource:
    def on_get(self, req, resp):
        """gets a new auth token"""
        resp.body = json.dumps({'token':uuid.uuid4()})

class MoveUnitResource:
    def on_post(self, req, resp):
        """Handles post requests"""
        req_json = json.loads(req.stream.read().decode('utf-8'))
        direction = req_json['direction']
        token = req_json['token']
        for i in req_json['ids']:
            s.units[i].move(direction, token)
        resp.status = falcon.HTTP_200

class CreateUnitResource:
    def on_post(self, req, resp):
        req_json = json.loads(req.stream.read().decode('utf-8'))
        s.max_id = add_unit(s.max_id, req_json['token'])

class GetGridResource:
    def on_get(self, req, resp):
        resp.body = json.dumps({'units': {id: (s.units[id].x, s.units[id].y) for id in s.units}})

api = falcon.API()
s = ServerClass()
api.add_route('/unit/move', MoveUnitResource())
api.add_route('/unit/create', CreateUnitResource())
api.add_route('/grid', GetGridResource())
api.add_route('/token/get', CreateAuthTokenResource())
