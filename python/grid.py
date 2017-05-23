import math
from cmath import sqrt
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
        # self.pixels = []
        self.neoPixelrings = []
        # for x in range(width):
        #     self.pixels.append([])
        #     for y in range(height):
        #         self.pixels[x].append(pixel(x,y))

    # def getPixel(self,x,y):
    #     return self.pixels[x][y]

    def getCenter(self):
        return [self.width / 2, self.height /2]

    def insertPixlRing(self,pixelRing,x,y):
        self.neoPixelrings.append(pixelRing)
        # self.getPixel(x,y).setNeoPixelAlias(pixelRing.chainOffset + 0)
        pixelRing.setPixelActual(0, x,y)
        # self.getPixel(x-1,y+1).setNeoPixelAlias(pixelRing.chainOffset + 1)
        pixelRing.setPixelActual(1, x-1, y+1)
        # self.getPixel(x-2,y+2).setNeoPixelAlias(pixelRing.chainOffset + 2)
        pixelRing.setPixelActual(2, x-2,y+2)
        # self.getPixel(x-1,y+3).setNeoPixelAlias(pixelRing.chainOffset + 3)
        pixelRing.setPixelActual(3, x-1,y+3)
        # self.getPixel(x,y+4).setNeoPixelAlias(pixelRing.chainOffset + 4)
        pixelRing.setPixelActual(4, x,y+4)
        # self.getPixel(x+1,y+3).setNeoPixelAlias(pixelRing.chainOffset + 5)
        pixelRing.setPixelActual(5, x+1,y+3)
        # self.getPixel(x+2,y+2).setNeoPixelAlias(pixelRing.chainOffset + 6)
        pixelRing.setPixelActual(6, x+2,y+2)
        # self.getPixel(x+1,y+1).setNeoPixelAlias(pixelRing.chainOffset + 7)
        pixelRing.setPixelActual(7, x+1,y+1)

class neoPixelRing:
    def __init__(self,pixelAmount,chainOffset):
        self.pixelAmount = pixelAmount
        self.chainOffset = chainOffset
        self.pixelMask = [None] * pixelAmount

    def setPixelActual(self,pixel,x,y):
        self.pixelMask[pixel] = [x,y]

    def getActualPixelDistance(self,pixel,x,y):
        a = self.pixelMask[pixel][0] - x
        b = self.pixelMask[pixel][1] - y
        v = (a*a) - (b*b);
        d = abs(sqrt(v))
        return d

    def getPixelChainPosition(self,pixel):
        return pixel + (self.chainOffset * self.pixelAmount)

def create_led_grid(width,height):
    return grid(width,height)
