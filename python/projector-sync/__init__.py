# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

from cmath import sqrt
import math


grid_width = 200
grid_height = 200
grid_drawing_mulitplier = 2

pygame.init()

pygame.init()

background_colour = (0,0,0)
(width, height) = (grid_width * grid_drawing_mulitplier, grid_height * grid_drawing_mulitplier)
# Screen Size ----------------------------------------------------------

# ----------------------------------------------------------------------



if __name__ == '__main__':
    screen = pygame.display.set_mode((width, height),RESIZABLE)
    pygame.display.set_caption('Secret Sessions.....shhhhhhhh')
    screen.fill(background_colour)
    pygame.display.flip()

    running = True
    fullscreen = False
    while running:

        screen.fill(background_colour)
        # UPDATE ---------------------------------------------------------------
        #pygame.display.update()



        # EVENTS ---------------------------------------------------------------
        for event in pygame.event.get():

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_f:
                    print("F")
                    if fullscreen: fullscreen = False
                    else: fullscreen = True

                    if fullscreen:
                        screen = pygame.display.set_mode((width, height),FULLSCREEN)
                    else:
                       screen = pygame.display.set_mode((width, height),RESIZABLE)


                if event.key == pygame.K_q:
                    running = False;

            if event.type == pygame.QUIT:
                running = False