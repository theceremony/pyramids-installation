# -*- coding: utf-8 -*-

from neopixel import *
from Grid import *
import math
import time

LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10
LED_BRIGHTNESS = 255       # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)




class NEOPixel:

    def __init__(self):
        self.numberOfLEDS = 16
        self.surface = None
        self.center = (200,200)
        self.radius = 200
        self.strip = Adafruit_NeoPixel(16, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS,0)
        self.strip.begin()

        #time.sleep(1000)
        #print(self.strip)
        print("NEO PIXEL RUNNING")

    def run(self):
        if self.surface is not None:
            self.center = (self.surface.get_width() /2, self.surface.get_height() /2)
            #self.radius = self.surface.get_height() /2 - 50
            deg = 360 / self.numberOfLEDS
            #print(deg)
            for a in range(self.numberOfLEDS):
                x = int(math.floor(self.radius * math.cos(a * deg) + self.center[0]))
                y = int(math.floor(self.radius * math.sin(a * deg) + self.center[1]))
                #print(x)
                #print(y)
                color = self.surface.get_at((x, y))
                self.strip.setPixelColor(a, Color(color[0],color[1],color[2]))
            self.strip.show()

