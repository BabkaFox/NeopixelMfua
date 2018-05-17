# Based on NeoPixel library and strandtest example by Tony DiCola (tony@tonydicola.com)
# To be used with a 12x1 NeoPixel LED stripe.
# Place the LEDs in a circle an watch the time go by ...
# red = hours
# blue = minutes 1-5
# green = seconds
# (To run the program permanently and with autostart use systemd.)

import time
import datetime
import math
import Image

from neopixel import *

# LED strip configuration:
LED_COUNT = 256  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 1  # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False

filename = "/home/pi/Downloads/h10.png"
img = Image.open(filename).convert("RGB")

width = img.size[0];
height = img.size[1]
pixels = img.load()

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(
        LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    gamma = bytearray(256)
    for i in range(256):
        gamma[i] = int(pow(float(i) / 255.0, 2.7) * 255.0 + 0.5)

    p = 0
    z = 0

    for w in range(width):
        for x in (range(z, width)):
            if (x % 2 == 0):
                for y in range(width):
                    colorPixel = pixels[x, y]
                    if (p > 255-width*z): p = 0
                    # strip.setPixelColor(p, Color(colorPixel[1], colorPixel[0], colorPixel[2]))
                    strip.setPixelColor(p, Color(gamma[colorPixel[1]], gamma[colorPixel[0]], gamma[colorPixel[2]]))
                    print(x, y, p, colorPixel[0], colorPixel[1], colorPixel[2])
                    p = p + 1
                    strip.show()
            else:
                for y in reversed(range(width)):
                    colorPixel = pixels[x, y]
                    if (p > 255-width*z): p = 0
                    # strip.setPixelColor(p, Color(colorPixel[1], colorPixel[0], colorPixel[2]))
                    strip.setPixelColor(p, Color(gamma[colorPixel[1]], gamma[colorPixel[0]], gamma[colorPixel[2]]))
                    print(x, y, p, colorPixel[0], colorPixel[1], colorPixel[2])
                    p = p + 1
                    strip.show()
        z = z + 1
time.sleep(0.1)
