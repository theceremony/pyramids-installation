# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

import sys
import os

from cmath import sqrt
import math


(width, height) = (640,480)

class App:

    def __init__(self):
        self.running = True
        self.screen = None
        self.fullscreen = False
        self.lifted = None
        self.image_library = {}

    def get_image(self, path):
        image = self.image_library.get(path)
        if image is None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            print(canonicalized_path)
            image = pygame.image.load(canonicalized_path)
            self.image_library[path] = image.convert()
        return image

    def on_toggleFullscreen(self):
        if self.fullscreen:
            self.fullscreen = False
            self.screen = pygame.display.set_mode((width, height), RESIZABLE)
        else:
            self.fullscreen = True
            modes = pygame.display.list_modes()
            self.screen = pygame.display.set_mode(modes[0], FULLSCREEN)

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
        #pygame.display.blit(self.get_image('./img/lifted.png'),20,20)

        self.screen.blit(self.get_image('img/lifted.png'), (0, 0) )

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