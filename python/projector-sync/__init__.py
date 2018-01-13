# -*- coding: utf-8 -*-
import os
import pygame
from pygame.locals import *
from GIFImage import GIFImage

(width, height) = (1024,768)

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
            self.screen = pygame.display.set_mode(modes[0], FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF,8)
        else:
            self.screen = pygame.display.set_mode((width, height), RESIZABLE)

    def on_toggleFullscreen(self):
        if self.fullscreen:
            self.fullscreen = False
        else:
            self.fullscreen = True

        self.on_setScreenSize()

    def on_init(self):
        pygame.init()
        self.on_setScreenSize()
        pygame.mouse.set_visible(False)
        modes = pygame.display.list_modes()
        self.gif =  GIFImage("img/pyramids gifs/weird/colors.gif")
        self.gif.scale_image(modes[0])


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
        self.cat_pos_x += 4
        self.cat_pos_y += 1

    def on_render(self):
        pygame.display.flip()
        self.gif.render(self.screen, (0, 0))
        #self.gif2.render(self.screen, (250, 250))
        #self.screen.blit(self.get_image('img/lifted.png'), (0, 0) )
        #self.screen.blit(self.get_image('img/pyramids gifs/flowers/1.gif'), (self.cat_pos_x,self.cat_pos_y) )
        #self.screen.blit(self.get_image('img/cat2.jpg'), (self.cat_pos_x+ 200,self.cat_pos_y-200 ) )

        color = self.screen.get_at( (200,200) )

        print(color)

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