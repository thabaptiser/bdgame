class Unit():
    def __init__(self, x, y, token, id):
        self.x = x
        self.y = y
        self.token = token
        self.life = 2
        self.destination = (0, 0)
        self.id = id
        self.moving = False

    def check_auth(self, token):
        return True
        return self.token == token

    def move_to(self, direction, token):
        if not self.check_auth(token):
            return
        self.destination = direction
        self.moving = True

    def move(self):
        if self.x < self.destination[0]:
            direction = 1
        elif self.x > self.destination[0]:
            direction = 3
        elif self.y < self.destination[0]:
            direction = 0
        elif self.y > self.destination[0]:
            direction = 2

        if direction == 0:
            self.y += 1
            del s.units[(self.x, self.y)]
            s.units[(self.x, self.y + 1)] = self

        elif direction == 1:
            self.x += 1
            del s.units[(self.x, self.y)]
            s.units[(self.x + 1, self.y)] = self

        elif direction == 2:
            self.y -= 1
            del s.units[(self.x, self.y)]
            s.units[(self.x, self.y - 1)] = self

        elif direction == 3:
            self.x -= 1
            del s.units[(self.x, self.y)]
            s.units[(self.x - 1, self.y)] = self

        if self.x == destination[0] and self.y == destination[1]:
            self.moving = False
        print("moved to {destination}".format(destination=(self.x, self.y)))

    def attack(self, enemy, token):
        if not self.check_auth(token):
            return
        enemy.life -= 1

    @property
    def dead(self):
        return self.life < 1
