import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1,brightness=0.1)
dot.brightness = 0.5

print("Make it red!")

while True:
    dot.fill((255, 255, 255))