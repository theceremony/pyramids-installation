import gradient
import grid

if __name__ == '__main__':
    print (gradient.linear_gradient("#0f0f0f","#000000"))
    g = grid.create_led_grid(13,13)
    pixel = g.getPixel(2,10);
    print(pixel)
