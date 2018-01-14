# -*- coding: utf-8 -*-

import os
import pygame
from GIFImage import GIFImage
from random import randint


imagePath = "img/pyramids gifs/disp/"

class GIFMode:

    def __init__(self):

        self.surface = None
        self.currentGIF = None
        self.nextGIF = None
        self.loadingNextGIF = False
        self.files = os.listdir(imagePath)
        self.isActive = True
        self.playTime = 200
        self.currentTime = 0

    def set_surface(self, surface):
        self.surface = surface

    def play_next_GIF(self):
        print('PLAY NEXT CALLED')
        self.currentGIF = self.nextGIF
        self.currentGIF.play()
        self.nextGIF = None

    def load_next_GIF(self):
        print('LOAD NEXT CALLED')
        self.loadingNextGIF = True
        self.nextGIF = GIFImage(self.choose_next_GIF())
        modes = pygame.display.list_modes()
        self.nextGIF.scale_image(modes[0])
        print(self.nextGIF.loaded)

    def choose_next_GIF(self):
        return (imagePath + self.files[randint(0, len(self.files) - 1)])

    def render_current(self):
        if self.currentGIF is not None:
            #print('I like to render')
            self.currentGIF.render(self.surface, (0, 0))
            self.currentTime += 1

    def run(self):
        if self.isActive is True:
            # Check to see if next gif is loaded ----------------------------------
            if self.nextGIF is None:
                self.load_next_GIF()
            elif self.loadingNextGIF is True:
                if self.nextGIF.loaded is True:
                    self.nextGIF.pause()
                    self.loadingNextGIF = False
            #----------------------------------------------------------------------
            if self.nextGIF is not None and self.currentGIF is None:
                self.play_next_GIF()
            #----------------------------------------------------------------------
            self.render_current()
            #----------------------------------------------------------------------

            if self.currentTime >= self.playTime:
                self.currentGIF = None
                self.currentTime = 0