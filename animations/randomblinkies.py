import time
from random import randrange, uniform
from engine.game_engine import BaseGame
import settings

# The following is adapted from the Pimoroni Plasma library's example code, that can be found here: https://github.com/pimoroni/plasma/tree/main/examples
# It has been adjusted to work with the 1d engine framework developed for the EMF workshop on games for LED strips.

class RandomBlinkies(BaseGame):

    """
    This example randomises LED colours and brightness for a subtly sparkly effect.
    """

    def init(self, engine):

        # Pick what bits of the colour wheel to use (from 0-360°, try https://www.cssscript.com/demo/hsv-hsl-color-wheel-picker-reinvented/ )
        self.HUE_START = 180
        self.HUE_END = 260

        # Set up brightness minimum and maximum (between 0.0 and 1.0)
        self.BRIGHTNESS_MIN = 0.2
        self.BRIGHTNESS_MAX = 0.7

        # Set up speed (wait time between updates, in seconds.)
        self.SPEED = 0.3
        # Light up all the leds random colours and brightnesses from the specified ranges...
        # randrange is for picking integers from a range,
        # uniform is for generating random uniform floats between a minimum and maximum value.
        for i in range(settings.LED_LENGTH):
            engine.led_strip.set_hsv(i, randrange(self.HUE_START, self.HUE_END) / 360, 1.0, uniform(self.BRIGHTNESS_MIN, self.BRIGHTNESS_MAX))

    def draw(self, engine, display):
        # ...and then update one random pixel at a time to keep things fresh and sparkly.
        # Comment out the lines below if you want static lights.
        display.set_hsv(randrange(0, settings.LED_LENGTH), randrange(self.HUE_START, self.HUE_END) / 360, 1.0, uniform(self.BRIGHTNESS_MIN, self.BRIGHTNESS_MAX))




