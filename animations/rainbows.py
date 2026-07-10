import time
from engine.game_engine import BaseGame
import settings

# The following is adapted from the Pimoroni Plasma library's example code, that can be found here: https://github.com/pimoroni/plasma/tree/main/examples
# It has been adjusted to work with the 1d engine framework developed for the EMF workshop on games for LED strips.

class Rainbows(BaseGame):

    """
    Make some rainbows!
    """

    def init(self, engine):

        self.SPEED = 20 # The SPEED that the LEDs cycle at (1 - 255)
        self.offset = 0.0 # The offset of the rainbow cycle

    def draw(self, engine, display):
        self.SPEED = min(255, max(1, self.SPEED))
        self.offset += float(self.SPEED) / 2000.0
        self.offset %= 1

        for i in range(settings.LED_LENGTH):
            hue = (self.offset + float(i) / settings.LED_LENGTH) % 1
            display.set_hsv(i, hue + self.offset, 1.0, 0.6)



