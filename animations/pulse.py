from math import sin
import time
from engine.game_engine import BaseGame
import settings


# The following is adapted from the Pimoroni Plasma library's example code, that can be found here: https://github.com/pimoroni/plasma/tree/main/examples
# It has been adjusted to work with the 1d engine framework developed for the EMF workshop on games for LED strips.

class Pulse(BaseGame):

    """
    Pulsing effect generated using a sine wave.
    """

    def init(self, engine):
         # we're using HSV colours in this example - find more at https://colorpicker.me/
        # to convert a hue that's in degrees, divide it by 360
        self.COLOUR = 0.5
        self.offset = 0

    def draw(self, engine, display):
        # use a sine wave to set the brightness
        for i in range(settings.LED_LENGTH):
            display.set_hsv(i, self.COLOUR, 1.0, (1+sin(self.offset)*0.6)/2)
        self.offset += 0.02

