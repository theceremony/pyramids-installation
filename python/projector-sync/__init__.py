# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

from cmath import sqrt
import math


# //////////////////////////////////////////////////////////////////////////////
#grid_width = 200
#grid_height = 200
#grid_drawing_mulitplier = 2

#pygame.init()
#background_colour = (0,0,0)
#(width, height) = (grid_width * grid_drawing_mulitplier, grid_height * grid_drawing_mulitplier)

# //////////////////////////////////////////////////////////////////////////////


(width, height) = (640,480)

class App:

    def __init__(self):
        self.running = True
        self.screen = None
        self.fullscreen = False

    def on_toggleFullscreen(self):
        if self.fullscreen:
            self.fullscreen = False
            self.screen = pygame.display.set_mode((width, height), RESIZABLE)
        else:
            self.fullscreen = True
            self.screen = pygame.display.set_mode((width, height), FULLSCREEN)

    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    def on_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_f:
                self.on_toggleFullscreen()
            if event.key == pygame.K_q:
                self.running = False
                self.on_cleanup()
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() is False:
            self.running = False

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
# /////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':

    _app = App()
    _app.on_execute()