import pygame as pg
import sys
from entities import Snake, Colli_Object
import random
import time
class Game:
    def __init__(self):
        pg.init()
        self.DIMENSIONS = [500,500]
        self.paused = False
        self.screen = pg.display.set_mode(self.DIMENSIONS)
        self.Snake = Snake(self.DIMENSIONS, self)
        self.FPS = 7
        self.SCALE = self.Snake.size*2
        
        self.BX_WIDTH = self.DIMENSIONS[0]
        self.BX_HEIGHT = (self.Snake.size*2)
        self.BY_WIDTH = self.BX_HEIGHT
        self.BY_HEIGHT = self.BX_HEIGHT
        self.clock = pg.time.Clock()
        pg.display.set_caption('snake game')
        
        self.font = pg.font.SysFont('Verdana', 20)
        self.fpsText = self.font.render(str(round(self.clock.get_fps())), True, (0,0,0))
        self.scoreText = self.font.render(str(self.Snake.length-1), True, 'red')
        
        self.x_keys_pressed = [False, False]
        self.y_keys_pressed = [False, False]
        self.collision_objects = []
        self.food = []

    def endGame(self):
        self.Snake = Snake(self.DIMENSIONS, self)
        self.FPS = 7
        #time.sleep(0.5)
    
    def speedUp(self):
        if (self.Snake.length-1) % 2 == 0 and 2 <= self.Snake.length:
            self.FPS += 1

    def checkCollisions(self):
        for ob in self.collision_objects:
            if self.Snake.snake.colliderect(ob.object):
                self.endGame()
        #check if food was eaten
        if self.Snake.snake.colliderect(self.food[0]):
            self.Snake.eat()
            self.food.clear()
            self.speedUp()
        #check if snake collided with self
        for seg in self.Snake.body[2:]:
            if self.Snake.snake.colliderect(seg.object):
                self.endGame()

    def spawnFood(self):
        if len(self.food) == 0:
            pos_x = random.randrange((self.SCALE*2), (self.DIMENSIONS[1] - self.SCALE*2),10)
            pos_y = random.randrange((self.SCALE*2), (self.DIMENSIONS[1] - self.SCALE*2),10)
            food_rect = pg.Rect(pos_x, pos_y, 10, 10)
            self.food.append(food_rect)
            #print([pos_x, pos_y])

    def renderFood(self):
        pg.draw.rect(self.screen, 'yellow', self.food[0])


    def createBorders(self):
        left_ver_border = [0,self.BY_HEIGHT]
        right_ver_border = [(self.BX_WIDTH - self.BX_HEIGHT), self.BX_HEIGHT]

        top_hor_border = [0, 0]
        bott_hor_border = [0, (self.DIMENSIONS[1] - self.BX_HEIGHT)]

        top = Colli_Object([self.DIMENSIONS[0], self.BX_HEIGHT], top_hor_border, self.screen, 'grey')
        bottom = Colli_Object([self.DIMENSIONS[0], self.BX_HEIGHT], bott_hor_border, self.screen, 'grey')
        #left = pg.Rect(left_ver_border[0], left_ver_border[1], self.BX_HEIGHT, (self.DIMENSIONS[0] - (self.BX_HEIGHT) * 2))
        left = Colli_Object([self.BX_HEIGHT, (self.DIMENSIONS[0] - (self.BX_HEIGHT) * 2)], [left_ver_border[0], left_ver_border[1]], self.screen, 'grey')
        #right = pg.Rect(right_ver_border[0], right_ver_border[1], self.BX_HEIGHT, (self.DIMENSIONS[0] - (self.BX_HEIGHT) * 2))
        right = Colli_Object([self.BX_HEIGHT, (self.DIMENSIONS[0] - (self.BX_HEIGHT) * 2)], [right_ver_border[0], right_ver_border[1]], self.screen, 'grey')
        self.collision_objects.append(top)
        self.collision_objects.append(bottom)
        self.collision_objects.append(left)
        self.collision_objects.append(right)
        #pg.draw.rect(self.screen, 'red', left)
        
        #pg.draw.rect(self.screen, 'red', right)

    def renderBorder(self):
        for b in self.collision_objects:
            b.render()

    def renderFPStext(self):
        self.fpsText = self.font.render(str(round(self.clock.get_fps(),2)), True, (127,127,127))
        self.screen.blit(self.fpsText, (0,0))
        self.scoreText = self.font.render(str(self.Snake.length-1), True, 'red')
        self.screen.blit(self.scoreText, (self.DIMENSIONS[0] - self.SCALE*3, self.SCALE))


    def processInput(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            # KEYDOWN PRESSES
            if event.type == pg.KEYDOWN:
                # y axis
                if event.key == pg.K_UP:
                    self.y_keys_pressed[0] = True
                if event.key == pg.K_DOWN:
                    self.y_keys_pressed[1] = True
                # x axis
                if event.key == pg.K_LEFT:
                    self.x_keys_pressed[0] = True
                if event.key == pg.K_RIGHT:
                    self.x_keys_pressed[1] = True
                if event.key == pg.K_SPACE:
                    self.paused = not self.paused
            if event.type == pg.KEYUP:
                # y axis
                if event.key == pg.K_UP:
                    self.y_keys_pressed[0] = False
                if event.key == pg.K_DOWN:
                    self.y_keys_pressed[1] = False
                # x axis
                if event.key == pg.K_LEFT:
                    self.x_keys_pressed[0] = False
                if event.key == pg.K_RIGHT:
                    self.x_keys_pressed[1] = False
                
    def run(self):
        running = True
        while running:
            #check input
            self.processInput()
            if not self.paused:
                self.screen.fill('black')
                self.spawnFood()
                self.renderFood()
                self.Snake.move()
                self.checkCollisions()
                self.Snake.getDirection(self.y_keys_pressed, self.x_keys_pressed)

                #Render here
                
                self.renderBorder()
                self.renderFPStext()
                
                self.Snake.render()
            
            
            pg.display.flip()
            self.clock.tick(self.FPS)

g = Game()
g.createBorders()
g.run()


