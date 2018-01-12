import gradient
import grid
import pygame
import sys

from cmath import sqrt
import math

grid_width = 200
grid_height = 200
grid_drawing_mulitplier = 2

g = grid.create_led_grid(grid_width,grid_height)

np = grid.neoPixelRing(8,0)
np2 = grid.neoPixelRing(8,1)
np3 = grid.neoPixelRing(8,2)

g.insertPixelRing(np,7,2)
g.insertPixelRing(np2,2,8)
g.insertPixelRing(np3,11,8)
center = g.getCenter()

outGradient = gradient.linear_gradient("#11aaff","#222222",10)
outGradient2 = gradient.polylinear_gradient(["#000000","#ff0000","#11aaff","#000000"],10)

pygame.init()
background_colour = (255,255,255)
(width, height) = (grid_width * grid_drawing_mulitplier, grid_height * grid_drawing_mulitplier)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()


def plotCircle(x0,y0,radius):
    x = radius
    y = 0
    err = 0
    width = 1
    height = 1
    while x >= y:

        pygame.draw.rect(screen,(111,0,0),(x0 + x , y0 + y, width, height))
        pygame.draw.rect(screen,(111,0,0),(x0 + y, y0 + x, width, height))
        pygame.draw.rect(screen,(111,0,0),(x0 - y, y0 + x, width, height))
        pygame.draw.rect(screen,(111,0,0),(x0 - x, y0 + y, width, height))
        pygame.draw.rect(screen,(111,0,0),(x0 - x, y0 - y, width, height))
        pygame.draw.rect(screen,(111,0,0),(x0 - y, y0 - x, width, height))
        pygame.draw.rect(screen,(111,0,0),(x0 + y, y0 - x, width, height))
        pygame.draw.rect(screen,(111,0,0),(x0 + x, y0 - y, width, height))
        pygame.display.flip()
        y +=1
        if err <= 0:
            err += 2 * y + 1
        if err > 0:
            x -= 1
            err -= 2 * x + 1


if __name__ == '__main__':

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # screen.fill(background_colour)

        for x in range(grid_width):
            for y in range(grid_height):

                d1 = math.sqrt((x - grid_width/2) ** 2 + (y - grid_height/2) ** 2)
                d1 = int(math.floor(float(d1) / (math.sqrt(2) * grid_width/2) * 10))
                # print(d1)
                if d1 > len(outGradient2['r'])-1:
                    d1 = len(outGradient2['r'])-1
                pygame.draw.rect(screen, (outGradient2['r'][d1], outGradient2['g'][d1], outGradient2['b'][d1]), (x * grid_drawing_mulitplier, y * grid_drawing_mulitplier, grid_drawing_mulitplier, grid_drawing_mulitplier))
        pygame.display.flip()
