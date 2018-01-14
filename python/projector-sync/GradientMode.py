# -*- coding: utf-8 -*-

import Gradient
import pygame

class GradientMode:

    def __init__(self):
        self.isActive = False
        self.surface = None
        self.gradientWidth = 1000
        self.grad1 = Gradient.polylinear_gradient(
            ["#5522aa", "#ff0000", "#11aaff", "#0f0f00"], self.gradientWidth)
        self.grad2 = Gradient.polylinear_gradient(
            ["#ffff00", "#ffffff", "#11aaff", "#0000ff"], self.gradientWidth)

        self.grad1Alpha = 255
        self.grad2Alpha = 0
        self.way = 1


    def run(self):
        if self.surface is not None:
            mod = 0
            self.grad2Alpha += self.way
            if self.grad2Alpha > 255:
                self.way = -1;
            if self.grad2Alpha <= 0:
                self.way = 1
            surface1 = pygame.Surface(self.surface.get_size())
            surface1.set_alpha(self.grad1Alpha)

            surface2 = pygame.Surface(self.surface.get_size())
            surface2.set_alpha(self.grad2Alpha)

            for y in range(self.surface.get_height()):
                if mod >= len(self.grad1.get('g')):
                    mod = 0
                pygame.draw.rect(surface1,
                    (self.grad1.get('r')[mod],self.grad1.get('g')[mod],self.grad1.get('b')[mod]),
                    (0,y,self.surface.get_width(),2)
                )

                pygame.draw.rect(surface2,
                    (self.grad2.get('r')[mod],self.grad2.get('g')[mod],self.grad2.get('b')[mod]),
                    (0,y,self.surface.get_width(),2)
                )
                mod +=1
            self.surface.blit(surface1, (0, 0))
            self.surface.blit(surface2, (0, 0))
