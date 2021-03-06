# -*- coding: utf-8 -*-
import os
import pygame
from pygame.locals import *
from GIFMode import GIFMode
from GradientMode import GradientMode

from Grid import *
from LEDController import NEOPixel


(width, height) = (640, 480)

class App:

    def __init__(self):
        self.running = True
        self.screen = None
        self.fullscreen = False
        self.lifted = None
        self.image_library = {}
        self.cat_pos_x = 0
        self.cat_pos_y = 0
        self.gif = None

        self.GIFMode = None
        self.GradientMode = None
        self.NeoPixel = NEOPixel()

    def get_image(self, path):
        image = self.image_library.get(path)
        if image is None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            self.image_library[path] = image.convert()
        return image

    def on_setScreenSize(self):
        if self.fullscreen:
            modes = pygame.display.list_modes()
            self.screen = pygame.display.set_mode(
                modes[0], FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
            )
        else:
            self.screen = pygame.display.set_mode((width, height), RESIZABLE)

        self.GIFmode.surface = self.screen
        self.GradientMode.surface = self.screen
        self.NeoPixel.surface = self.screen

    def on_toggleFullscreen(self):
        if self.fullscreen:
            self.fullscreen = False
        else:
            self.fullscreen = True

        self.on_setScreenSize()

    def on_init(self):
        pygame.init()
        self.GIFmode = GIFMode()
        self.GIFmode.isActive = True
        self.GradientMode = GradientMode()
        self.GradientMode.isActive = False
        self.on_setScreenSize()
        pygame.mouse.set_visible(False)

    def toggle_modes(self):
        if self.GIFmode.isActive is True:
            self.GIFmode.isActive = False
            self.GradientMode.isActive = True
        else:
            self.GIFmode.isActive = True
            self.GradientMode.isActive = False

    def on_event(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                self.toggle_modes()
            if event.key == pygame.K_f:
                self.on_toggleFullscreen()
            if event.key == pygame.K_q:
                self.running = False
                #self.on_cleanup()
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        self.GIFmode.run()
        self.GradientMode.run()
        self.NeoPixel.run()

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