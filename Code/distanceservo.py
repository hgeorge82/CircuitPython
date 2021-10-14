import time
import board
import adafruit_hcsr04
import neopixel
import simpleio


dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness = 0.1)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
cm = 0

while True:
    try:
        cm = sonar.distance
        print((cm,))
        if cm < 5:
            print("Red")
            r = 209
            g = 0
            b = 0


        elif cm < 20:
            print("not red")
            r = int(simpleio.map_range(cm, 5, 20, 209, 0))
            g = 0
            b = int(simpleio.map_range(cm, 5, 20, 0, 209))

        elif cm > 20:
            print("not red or blue")
            r = 0
            g = int(simpleio.map_range(cm, 20, 35, 0, 209))
            b = int(simpleio.map_range(cm, 20, 35, 209, 0))


        dot.fill((r, g, b))

    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)