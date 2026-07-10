from engine.game_engine import BaseGame
import settings
import time

from random import random, uniform


# The following is adapted from the Pimoroni Plasma library's example code, that can be found here: https://github.com/pimoroni/plasma/tree/main/examples
# It has been adjusted to work with the 1d engine framework developed for the EMF workshop on games for LED strips.

class FireEffect(BaseGame):
    """
    A fire effect.
    """

    def draw(self, engine, display):
        # fire effect! Random red/orange hue, full saturation, random brightness
        for i in range(settings.LED_LENGTH):
            display.set_hsv(i, uniform(0.0, 50 / 360), 1.0, random())
        time.sleep(0.05)  
