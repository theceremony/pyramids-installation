# -*- coding: utf-8 -*-
import gradient
import grid
import analogInput
import math
from neopixel import *

LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 2       # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


class standard:
    def __init__(self):
        self.analogInput = analogInput.AnalogInput()
        self.gradient = gradient.linear_gradient("#11aaff","#00ff00",7)
        self.gradient2 = gradient.polylinear_gradient(["#003300","#11aaff","#003300"],8)
        print(self.gradient2)
        #print(self.gradient)
        #print self.gradient['b']
        self.grid_14 = grid.create_led_grid(14,14)
        self.np_0 = grid.neoPixelRing(8,0)
        self.np_1 = grid.neoPixelRing(8,1)
        self.np_2 = grid.neoPixelRing(8,2)

        self.grid_14.insertPixelRing(self.np_0, 7, 0)
        self.grid_14.insertPixelRing(self.np_1, 0, 12)
        self.grid_14.insertPixelRing(self.np_2, 12, 12)

        self.strip = Adafruit_NeoPixel(self.grid_14.getTotalPixels(), LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        self.strip.begin()

    def update(self):
        self.analogInput.update()
        center = self.grid_14.getCenter()
        center_x = (self.analogInput.xPercent * 5) + center[0]
        center_y = (self.analogInput.yPercent * 5) + center[1]
        for ring in self.grid_14.neoPixelrings:
            for i in range(ring.pixelAmount):
                a = ring.getPixelChainPosition(i)
                d = int(math.floor(ring.getActualPixelDistance(i,center_x,center_y))) % 7
                r = self.gradient2['r'][d]
                g = self.gradient2['g'][d]
                b = self.gradient2['b'][d]
                self.strip.setPixelColor(a, Color(r,b,g))
                #print d
        self.strip.show()

    def close(self):
        self.analogInput.close()

    def main(self):
        try:
            while True:
                self.update()
        except KeyboardInterrupt:
            pass

        finally:
            self.close()

if __name__ == '__main__':
    m = standard()
    m.main()