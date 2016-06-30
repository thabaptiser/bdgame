
class Unit():
    def __init__(self, x, y, token, id):
        self.x = x
        self.y = y
        self.token = token
        self.life = 2
        self.dest = (0,0)
        self.id = id
        self.moving = False

    def check_auth(self, token):
        return self.token == token

    def move_to(self, direction, token):
        if not self.check_auth(token):
            return
        self.dest = direction
        
    def move(self):
        if self.x < dest[0]:
            direction = 1
        elif self.x > dest[0]:
            direction = 3
        elif self.y < dest[0]:
            direction = 0
        elif self.y > dest[0]:
            direction = 2

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

        if self.x == direction[0] and self.y == direction[1]:
            self.moving = False

    def attack(self, enemy, token):
        if not self.check_auth(token):
            return
        enemy.life -= 1

    @property
    def dead(self):
        return self.life < 1
