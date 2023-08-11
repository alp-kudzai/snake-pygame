import pygame as pg

SPEED = 10
class Colli_Object:
    def __init__(self, size, pos, screen, color):
        self.width = size[0]
        self.height = size[1]
        self.pos = pos
        self.screen = screen
        self.color = color
        self.object = pg.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def move(self, coords):
        self.pos[0] += coords[0]
        self.pos[1] += coords[1]
        self.object = pg.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def render(self):
        self.object = pg.Rect(self.pos[0], self.pos[1], self.width, self.height)
        pg.draw.rect(self.screen, self.color, self.object)

    def __repr__(self):
        return f'Current Pos: {self.pos}'



class Snake:
    def __init__(self, dim, game):
        self.size = 10
        self.game = game
        self.last_direction = 4
        self.pos = [(dim[0]//2), (dim[1]//2)]
        self.snake = pg.Rect(self.pos[0], self.pos[1], self.size, self.size)
        self.body = []
        self.body.append(self.snake)
        # self.body.append(Colli_Object([10,10], [self.pos[0] - 10, self.pos[1]], self.game.screen, 'grey'))
        # self.body.append(Colli_Object([10,10], [self.pos[0] - 20, self.pos[1]], self.game.screen, 'grey'))
        self.length = 1
        self.color = 'grey'
        self.path = []
        self.sizeLimit = 100

    def getDirection(self, pressed_y, pressed_x):
        if pressed_x[0] and self.last_direction != 4:
            self.last_direction = 8
        if pressed_x[1] and self.last_direction != 8:
            self.last_direction = 4
        if pressed_y[0] and self.last_direction != 1:
            self.last_direction = 2
        if pressed_y[1] and self.last_direction != 2:
            self.last_direction = 1

    def eat(self):
        size = self.size
        if self.length == 1:
            match self.last_direction:
                case 8:
                    newpos =  [(self.pos[0] + SPEED), self.pos[1]]
                case 4:
                    newpos =  [(self.pos[0] - SPEED), self.pos[1]]
                case 2:
                    newpos = [ self.pos[0], (self.pos[1] + SPEED)]
                case 1:
                    newpos = [ self.pos[0], (self.pos[1] - SPEED)]
        else:
            lastpos = self.body[-1].pos
            match self.last_direction:
                case 8:
                    newpos =  [(lastpos[0] + SPEED), lastpos[1]]
                case 4:
                    newpos =  [(lastpos[0] - SPEED), lastpos[1]]
                case 2:
                    newpos = [ lastpos[0], (lastpos[1] + SPEED)]
                case 1:
                    newpos = [ lastpos[0], (lastpos[1] - SPEED)]

        seg = Colli_Object([self.size, self.size], newpos, self.game.screen, self.color)
        self.body.append(seg)
        self.length += 1
        #print(self.body)

    def moveBody(self):
        path = self.path[::-1]
        for i, s in enumerate(self.body[1:]):
            s.pos = path[i]
        
        
    def move(self):
        last_pos = self.pos[:]
        match self.last_direction:
            case 8:
                self.pos[0] -= SPEED
            case 4:
                self.pos[0] += SPEED
            case 2:
                self.pos[1] -= SPEED
            case 1:
                self.pos[1] += SPEED
        if self.length > 1:
            self.moveBody()
        #print(self.path)
        trail = self.pos[:]
        self.path.append(trail)
        self.snake = pg.Rect(self.pos[0], self.pos[1], self.size, self.size)
        if len(self.path) >= self.sizeLimit:
            self.path.pop(0)

        
        # for s in self.body[1:]:
        #     temp = s.pos
        #     s.move(last_pos)
        #     last_pos = temp
    

    def render(self):
        self.snake = pg.Rect(self.pos[0], self.pos[1], self.size, self.size)
        pg.draw.rect(self.game.screen, self.color, self.snake)
        for seg in self.body[1:]:
            seg.render()
