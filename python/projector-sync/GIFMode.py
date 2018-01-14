# -*- coding: utf-8 -*-

import os
import pygame
from GIFImage import GIFImage
from random import randint


imagePath = "img/pyramids gifs/disp/"

class GIFMode:


    def __init__(self):
        modes = pygame.display.list_modes()
        self.surface = pygame.Surface(modes[0])
        self.currentGIF = None
        self.nextGIF = None
        self.loadingNextGIF = False
        self.files = os.listdir(imagePath)


    def set_surface(self, surface):
        self.surface = surface

    def play_next_GIF(self):
        print('PLAY NEXT CALLED')
        self.currentGIF = self.nextGIF
        self.nextGIF = None

    def load_next_GIF(self):
        print('LOAD NEXT CALLED')
        self.loadingNextGIF = True
        self.nextGIF = GIFImage(self.choose_next_GIF())
        print(self.nextGIF.loaded)


    def choose_next_GIF(self):
        return (imagePath + self.files[randint(0, len(self.files)-1)])

    def render_current(self):
        pass

    def run(self):

        # Check to see if next gif is loaded ----------------------------------
        if self.nextGIF is None:
            self.load_next_GIF()
        elif self.loadingNextGIF is True:
            if self.nextGIF.loaded is True:
                self.nextGIF.pause()
                self.loadingNextGIF = False
        #----------------------------------------------------------------------

        if self.nextGIF != None and self.currentGIF == None:
            self.play_next_GIF()