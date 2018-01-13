# -*- coding: utf-8 -*-

import os
import pygame
from GIFImage import GIFImage

imagePath = "img/pyramids gifs/disp"

class GIFMode:

    def __init__(self):

        modes = pygame.display.list_modes()

        print(modes)

        self.surface = pygame.Surface((1024, 768))
        self.currentGIF = None
        self.files = os.listdir(imagePath)
        print(self.files)

    def set_surface(self, surface):
        self.surface = surface

    def play_next_GIF(self):
        pass

    def load_nex_GIF(self):
        pass

    def unload_last_GIF(self):
        pass

    def choose_next_GIF(self):
        pass

    def render_current(self):
        pass