# -*- coding: utf-8 -*-
import math
import spidev


spi = spidev.SpiDev()
spi.open(0,0)

mcp3008_switch_channel = 0
mcp3008_x_voltage_channel = 1
mcp3008_y_voltage_channel = 2

class AnalogInput:

    def read_spi_data_channel(self,channel):
        adc = spi.xfer2([1,(8+channel) << 4, 0])
        return((adc[1] & 3) <<8) + adc[2]


    def convert_coordinates_to_angle(self,x,y,center_x_pos,center_y_pos):

        dx = x - center_x_pos
        dy = y - center_y_pos
        rads = math.atan2(-dy,dx)
        rads %= 2 * math.pi
        return math.degrees(rads)


    def update(self):

        self.center_x_pos = 528
        self.center_y_pos = 506

        self.switch = self.read_spi_data_channel(mcp3008_switch_channel)

        self.x_pos = self.read_spi_data_channel(mcp3008_x_voltage_channel)
        self.y_pos = self.read_spi_data_channel(mcp3008_y_voltage_channel)

        self.angle = self.convert_coordinates_to_angle(self.x_pos,self.y_pos,self.center_x_pos,self.center_y_pos)
        #print(self.angle)
        xDif = self.x_pos-self.center_x_pos
        yDif = self.y_pos-self.center_y_pos
        self.xPercent = (xDif * 100) / (self.center_x_pos) * 0.01
        self.yPercent = (yDif * 100) / (self.center_y_pos) * 0.01
        #print(xPercent,yPercent)
        #print(self.x_pos-self.center_x_pos,self.y_pos-self.center_y_pos)

    def close(self):
        spi.close()

    def main(self):

        try:
            while True:
                self.update()

        except KeyboardInterrupt:
            pass

        finally:
           self.close()