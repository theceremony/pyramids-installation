import gradient
import grid
import analogInput

from neopixel import *

if __name__ == '__main__':
    # print (gradient.linear_gradient("#0f0f0f","#000000"))
    g = grid.create_led_grid(14,14)

    np = grid.neoPixelRing(8,0)
    np2 = grid.neoPixelRing(8,1)
    np3 = grid.neoPixelRing(8,2)

    g.insertPixlRing(np,7,2)
    g.insertPixlRing(np2,2,8)
    g.insertPixlRing(np3,11,8)
    center = g.getCenter()

    print(np.getActualPixelDistance(0,center[0],center[1]))
    # print(np3.pixelMask)
