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
