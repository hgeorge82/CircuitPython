import board
import neopixel
import time


dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1



while True:
    print("Make it red!")
    dot.fill((255 , 0 , 0))
    time.sleep  (1.5)
    print("Make it Orange!")
    dot.fill((255 , 128 , 0))
    time.sleep (1.5)
    print("Make it Yellow!")
    dot.fill((255, 255, 0))
    time.sleep (1.5)
    print("Make it Green!")
    dot.fill((0,173,0))
    time.sleep (1.5)
    print("Make it Blue!")
    dot.fill((0, 191, 255))
    time.sleep (1.5)
    print("Make it Purple!")
    dot.fill((128, 0, 255))
    time.sleep (1.5)
