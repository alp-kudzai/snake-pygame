import pygame as pg

SPEED = 10
class Snake:
    def __init__(self, dim, game):
        self.size = 10
        self.body = []
        self.game = game
        self.last_direction = 4
        self.pos = [(dim[0]/2), (dim[1]/2)]
        self.snake = pg.Rect(self.pos[0], self.pos[1], self.size, self.size)

    def getDirection(self, pressed_y, pressed_x):
        if pressed_x[0]:
            self.last_direction = 8
        if pressed_x[1]:
            self.last_direction = 4
        if pressed_y[0]:
            self.last_direction = 2
        if pressed_y[1]:
            self.last_direction = 1
    
    def move(self):
        match self.last_direction:
            case 8:
                self.pos[0] -= SPEED
            case 4:
                self.pos[0] += SPEED
            case 2:
                self.pos[1] -= SPEED
            case 1:
                self.pos[1] += SPEED

    def render(self):
        self.snake = pg.Rect(self.pos[0], self.pos[1], self.size, self.size)
        pg.draw.rect(self.game.screen, 'grey', self.snake)
