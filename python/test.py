import gradient
import grid
import pygame
import sys

from cmath import sqrt

if __name__ == '__main__':
    # print (gradient.linear_gradient("#0f0f0f","#000000"))

    grid_width = 14
    grid_height = 14
    grid_drawing_mulitplier = 31

    g = grid.create_led_grid(grid_width,grid_height)

    np = grid.neoPixelRing(8,0)
    np2 = grid.neoPixelRing(8,1)
    np3 = grid.neoPixelRing(8,2)

    g.insertPixelRing(np,7,2)
    g.insertPixelRing(np2,2,8)
    g.insertPixelRing(np3,11,8)
    center = g.getCenter()

    gradient = gradient.linear_gradient("#003300","#11aaff")
    # gradient2 = gradient.polylinear_gradient(["#003300","#11aaff","#003300"],8)

    # print(np3.pixelMask   )

    print(gradient)
    pygame.init()
    background_colour = (255,255,255)
    (width, height) = (grid_width * grid_drawing_mulitplier, grid_height * grid_drawing_mulitplier)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Tutorial 1')
    screen.fill(background_colour)
    pygame.display.flip()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(background_colour)
        # pygame.draw.rect(screen, (60, 60, 100), (20, 20, 40, 40))

        for x in range(grid_width):
            for y in range(grid_height):
                a = x - (grid_width/2)
                b = y - (grid_height/2)
                v = (a*a) - (b*b);
                d = int(abs(sqrt(v)))
                pygame.draw.rect(screen, (gradient['r'][d], gradient['g'][d], gradient['b'][d]), (x * grid_drawing_mulitplier, y * grid_drawing_mulitplier, grid_drawing_mulitplier, grid_drawing_mulitplier))
        pygame.display.flip()
