import math
from colour import Color

class pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def setPixelColor(self,color):
        self.color = color
    def setNeoPixelAlias(self,alias):
        self.pixelAlias = alias


class grid:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.pixels = []
        for x in range(width):
            self.pixels.append([])
            for y in range(height):
                self.pixels[x].append(pixel(x,y))

    def getPixel(self,x,y):
        return self.pixels[x][y]

    # def insertPixlRing(self,pixelRing,x,y):


class neoPixelRing:
    def __init__(self,pixelAmount,chainIndex):
        self.pixelAmount = pixelAmount
        self.chainIndex = chainIndex


def create_led_grid(width,height):
    return grid(width,height)
