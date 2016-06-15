import falcon
import json
import uuid

from unit import Unit

class ServerClass:
    max_id = 0
    units = {}

class CreateAuthTokenResource:
    def on_get(self, req, resp):
        """Gets a new auth token"""
        resp.body = json.dumps({'token': str(uuid.uuid4())})


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
        y = 0
        while s.units.get((0, y)):
            y += 1
        s.units[(0, y)] = Unit(0, y, req_json['token'])


class GetGridResource:
    def on_post(self, req, resp):
        req_json = json.loads(req.stream.read().decode('utf-8'))
        ret = []
        for x in range(req_json['screen'][0][0], req_json['screen'][1][0]):
            for y in range(req_json['screen'][0][1], req_json['screen'][0][1]):
                #if s.units.get((x, y)):
                    ret.append((x, y))
        resp.body = json.dumps({'soldiers': ret})
    
    def on_get(self, req, resp):
        resp.body = json.dumps({'soldiers': list(s.units.keys())})

s = ServerClass()
api = falcon.API()
api.add_route('/unit/move', MoveUnitResource())
api.add_route('/unit/create', CreateUnitResource())
api.add_route('/grid', GetGridResource())
api.add_route('/token/get', CreateAuthTokenResource())
