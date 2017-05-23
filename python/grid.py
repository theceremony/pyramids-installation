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
        self.neoPixelrings = []
        for x in range(width):
            self.pixels.append([])
            for y in range(height):
                self.pixels[x].append(pixel(x,y))

    def getPixel(self,x,y):
        return self.pixels[x][y]

    def getCenter(self):
        return [self.width / 2, self.height /2]

    def insertPixlRing(self,pixelRing,x,y):
        self.neoPixelrings.append(pixelRing)
        self.getPixel(x,y).setNeoPixelAlias(pixelRing.chainIndex + 0)
        pixelRing.setPixelActual(pixelRing.chainIndex + 0, x,y)
        self.getPixel(x-1,y+1).setNeoPixelAlias(pixelRing.chainIndex + 1)
        pixelRing.setPixelActual(pixelRing.chainIndex + 1, x-1,y+1)
        self.getPixel(x-2,y+2).setNeoPixelAlias(pixelRing.chainIndex + 2)
        pixelRing.setPixelActual(pixelRing.chainIndex + 2, x-2,y+2)
        self.getPixel(x-1,y+3).setNeoPixelAlias(pixelRing.chainIndex + 3)
        pixelRing.setPixelActual(pixelRing.chainIndex + 3, x-1,y+3)
        self.getPixel(x,y+4).setNeoPixelAlias(pixelRing.chainIndex + 4)
        pixelRing.setPixelActual(pixelRing.chainIndex + 4, x,y+4)
        self.getPixel(x+1,y+3).setNeoPixelAlias(pixelRing.chainIndex + 5)
        pixelRing.setPixelActual(pixelRing.chainIndex + 5, x+1,y+3)
        self.getPixel(x+2,y+2).setNeoPixelAlias(pixelRing.chainIndex + 6)
        pixelRing.setPixelActual(pixelRing.chainIndex + 6, x+2,y+2)
        self.getPixel(x+1,y+1).setNeoPixelAlias(pixelRing.chainIndex + 7)
        pixelRing.setPixelActual(pixelRing.chainIndex + 7, x+1,y+1)

class neoPixelRing:
    def __init__(self,pixelAmount,chainIndex):
        self.pixelAmount = pixelAmount
        self.chainIndex = chainIndex
        self.pixelMask = [None] * 8
    def setPixelActual(self,pixel,x,y):
        self.pixelMask[pixel] = [x,y]


def create_led_grid(width,height):
    return grid(width,height)
