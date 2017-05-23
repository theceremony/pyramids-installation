import gradient
import grid

if __name__ == '__main__':
    print (gradient.linear_gradient("#0f0f0f","#000000"))
    g = grid.create_led_grid(14,14)
    np = grid.neoPixelRing(8,0)
    g.insertPixlRing(np,7,2)
    print(np.pixelMask)
