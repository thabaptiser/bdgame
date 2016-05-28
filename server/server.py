import falcon
import json
import uuid

class Unit():
    def __init__(self, x, y, token):
        self.x = x
        self.y = y
        self.token = token

    def check_auth(self, token):
        return self.token == token

    def move(self, direction, token):
        if not self.check_auth(token):
            return
        
        if direction == 0:
            self.y += 1
            del s.units[(self.x, self.y)]
            s.units[(self.x, self.y+1)] = self
        
        elif direction == 1:
            self.x += 1
            del s.units[(self.x, self.y)]
            s.units[(self.x+1, self.y)] = self

        elif direction == 2:
            self.y -= 1
            del s.units[(self.x, self.y)]
            s.units[(self.x, self.y-1)] = self

        elif direction == 3:
            self.x -= 1
            del s.units[(self.x, self.y)]
            s.units[(self.x-1, self.y)] = self
 
def add_unit(max_id, token):
    s.units[(0, max_id)] = Unit(0, 0, token)
    return max_id + 1

class ServerClass:
    max_id = 0
    units = {}

class CreateAuthTokenResource:
    def on_get(self, req, resp):
        """Gets a new auth token"""
        resp.body = json.dumps({'token': uuid.uuid4()})


class MoveUnitResource:
    def on_post(self, req, resp):
        """Handles post requests"""
        req_json = json.loads(req.stream.read().decode('utf-8'))
        direction = req_json['direction']
        token = req_json['token']
        for i in req_json['positions']:
            s.units[i].move(direction, token)
        resp.status = falcon.HTTP_200


class CreateUnitResource:
    def on_post(self, req, resp):
        req_json = json.loads(req.stream.read().decode('utf-8'))
        s.max_id = add_unit(s.max_id, req_json['token'])


class GetGridResource:
    def on_post(self, req, resp):
        req_json = json.loads(req.stream.read().decode('utf-8'))
        ret = []
        for x in range(req_json['screen'][0][0], req_json['screen'][0][1]):
            for y in range(req_json['screen'][0][1], req_json['screen'][1][1]):
                ret.append(s.units[(x, y)])
        resp.body = json.dumps({'soldiers': ret})

api = falcon.API()
s = ServerClass()
api.add_route('/unit/move', MoveUnitResource())
api.add_route('/unit/create', CreateUnitResource())
api.add_route('/grid', GetGridResource())
api.add_route('/token/get', CreateAuthTokenResource())
