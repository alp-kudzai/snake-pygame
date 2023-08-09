import pygame as pg
import sys
from entities import Snake

class Game:
    def __init__(self):
        pg.init()
        self.FPS = 10
        self.DIMENSIONS = [500,500]
        self.clock = pg.time.Clock()
        pg.display.set_caption('snake game')
        self.screen = pg.display.set_mode(self.DIMENSIONS)
        self.font = pg.font.SysFont('Verdana', 20)
        self.fpsText = self.font.render(str(round(self.clock.get_fps())), True, (0,0,0))
        self.Snake = Snake(self.DIMENSIONS, self)
        self.x_keys_pressed = [False, False]
        self.y_keys_pressed = [False, False]

    def renderFPStext(self):
        self.fpsText = self.font.render(str(round(self.clock.get_fps(),2)), True, (127,127,127))
        self.screen.blit(self.fpsText, (0,0))

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

            self.screen.fill('black')
            self.Snake.getDirection(self.y_keys_pressed, self.x_keys_pressed)
            self.Snake.move()

            #Render here
            self.renderFPStext()
            self.Snake.render()
            pg.display.flip()
            self.clock.tick(self.FPS)

Game().run()


