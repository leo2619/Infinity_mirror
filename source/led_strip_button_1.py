##led_strip_button.py
#to control the led strip via push button

#imports necessary for the button
#import RPi.GPIO as GPIO
#from button import *

#imports necessary for the led strip
from rpi_ws281x import PixelStrip, Color
import argparse
from LED_color import *
import time

class LEDStrip(PixelStrip):
    def __init__(self, led_count, led_pin, led_freq_hz, led_dma, led_brightness, led_invert, led_channel):
        super().__init__(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness, led_channel)
        #self.strip = PixelStrip(led_count, led_pin, led_freq_hz, led_dma, led_invert, led_brightness, led_channel)
        self.begin()

    def color_wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.setPixelColor(i, color)
            self.show()
            time.sleep(wait_ms / 1000.0)

    def theater_chase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i + q, color)
                self.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i + q, 0)

    def wheel(self, pos):
        """Generate rainbow colors across 0-255 positions."""
        if pos < 85:
            return Color(pos * 3, 255 - pos * 3, 0)
        elif pos < 170:
            pos -= 85
            return Color(255 - pos * 3, 0, pos * 3)
        else:
            pos -= 170
            return Color(0, pos * 3, 255 - pos * 3)

    def rainbow(self, wait_ms=20, iterations=1):
        """Draw rainbow that fades across all pixels at once."""
        for j in range(256 * iterations):
            for i in range(self.strip.numPixels()):
                self.setPixelColor(i, self.wheel((i + j) & 255))
            self.show()
            time.sleep(wait_ms / 1000.0)

    def rainbow_cycle(self, wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        for j in range(256 * iterations):
            for i in range(self.numPixels()):
                self.setPixelColor(i, self.wheel((int(i * 256 / self.numPixels()) + j) & 255))
            self.show()
            time.sleep(wait_ms / 1000.0)

    def theater_chase_rainbow(self, wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i + q, self.wheel((i + j) % 255))
                self.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i + q, 0)


if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # LED strip configuration:
    LED_COUNT = 120        # Number of LED pixels.
    LED_PIN = 18           # GPIO pin connected to the pixels (18 uses PWM!).
    LED_FREQ_HZ = 800000   # LED signal frequency in hertz (800khz)
    LED_DMA = 10           # DMA channel to use for generating signal (10)
    LED_BRIGHTNESS = 255   # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False     # True to invert the signal
    LED_CHANNEL = 0        # set to '1' for GPIOs 13, 19, 41, 45 or 53

    # Button configuration
    #BUTTON_PIN = 17        # GPIO pin connected to the button

    # Setup GPIO for button
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button.button_callback, bouncetime=300)

    # Create LEDStrip object with appropriate configuration.
    led_strip = LEDStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_BRIGHTNESS, LED_INVERT, LED_CHANNEL)

    animations = [
        lambda: led_strip.color_wipe(LED_color.red),
        lambda: led_strip.color_wipe(LED_color.green),
        lambda: led_strip.color_wipe(LED_color.blue),
        lambda: led_strip.theater_chase(Color(127, 127, 127)),
        lambda: led_strip.theater_chase(Color(127, 0, 0)),
        lambda: led_strip.theater_chase(Color(0, 0, 127)),
        lambda: led_strip.rainbow(),
        lambda: led_strip.rainbow_cycle(),
        lambda: led_strip.theater_chase_rainbow()
    ]

    animation_index = 0

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        while True:
            animations[animation_index]()
            time.sleep(1)  # Wait a bit before starting the next animation

    except KeyboardInterrupt:
        if args.clear:
            led_strip.color_wipe(Color(0, 0, 0), 10)
        GPIO.cleanup()