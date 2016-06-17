import falcon
import json
import uuid
import time
from unit import Unit
import threading
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

class ServerClass:
    def __init__(self):
        max_id = 0
        units = {}
        threading.Thread(target=self.refresh).start()

    def refresh(self):
        while True:
            for u in s.units:
                if s.units[u].dead:
                    del s.units[u]
            time.sleep(0.1)

class CreateAuthTokenResource:
    def on_get(self, req, resp):
        """Gets a new auth token"""
        resp.body = json.dumps({'token': str(uuid.uuid4())})


class MoveUnitResource:
    def on_post(self, req, resp):
        """Handles post requests"""
        req_json = json.loads(req.stream.read().decode('utf-8'))
        dest = req_json['destination']
        token = req_json['token']
        mid_x = sum([s[0] for s in req_json['soldiers']])/len(req_json['soldiers'])
        mid_y = sum([s[1] for s in req_json['soldiers']])/len(req_json['soldiers'])
        if mid_x < dest[0]:
            direction = 1
        elif mid_x > dest[0]:
            direction = 3
        elif mid_y < dest[0]:
            direction = 0
        elif mid_y > dest[0]:
            direction = 2
        for i in req_json['soldiers']:
            s.units[i].move(direction, token)
        resp.status = falcon.HTTP_200

class AttackMoveUnitResource:
    def on_post(self, req, resp):
        """Handles post requests"""
        req_json = json.loads(req.stream.read().decode('utf-8'))
        dest = req_json['destination']
        token = req_json['token']
        mid_x = sum([s[0] for s in req_json['soldiers']])/len(req_json['soldiers'])
        mid_y = sum([s[1] for s in req_json['soldiers']])/len(req_json['soldiers'])
        if mid_x < dest[0]:
            direction = 1
        elif mid_x > dest[0]:
            direction = 3
        elif mid_y < dest[0]:
            direction = 0
        elif mid_y > dest[0]:
            direction = 2
        for i in req_json['soldiers']:
            attacked = False
            for d in directions:
                if s.units[(i[0]+d[0], i[1]+d[1])] and s.units[(i[0]+d[0], i[1]+d[1])].token != token:
                    s.units[i].attack(s.units[(i[0]+d[0], i[1]+d[1])])
                    attacked = True
                    break
            if not attacked:
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
        x_r = sorted((req_json['screen'][0][0], req_json['screen'][1][0]))
        y_r = sorted((req_json['screen'][0][1], req_json['screen'][1][1]))
        for x in range(x_r[0], x_r[1]):
            for y in range(y_r[0], y_r[1]):
                if s.units.get((x, y)):
                    ret.append((x, y))
        resp.body = json.dumps({'soldiers': ret})
    
    def on_get(self, req, resp):
        resp.body = json.dumps({'soldiers': list(s.units.keys())})

s = ServerClass()
tick_time = 0.1
api = falcon.API()
api.add_route('/unit/move', MoveUnitResource())
api.add_route('/unit/create', CreateUnitResource())
api.add_route('/grid', GetGridResource())
api.add_route('/token/get', CreateAuthTokenResource())

