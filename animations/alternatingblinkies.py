import time
from engine.game_engine import BaseGame
import settings


# The following is adapted from the Pimoroni Plasma library's example code, that can be found here: https://github.com/pimoroni/plasma/tree/main/examples
# It has been adjusted to work with the 1d engine framework developed for the EMF workshop on games for LED strips.


class AlternatingBlinkies(BaseGame):
    """
    Set up two alternating colours, great for festive lights!
    """

    def init(self, engine):
         # Pick two hues from the colour wheel (from 0-360°, try https://www.cssscript.com/demo/hsv-hsl-color-wheel-picker-reinvented/ )
        
        self.HUE_1 = 40
        self.HUE_2 = 285
        self.BRIGHTNESS = 0.5
        # Set up speed (wait time between colour changes, in seconds)
        self.SPEED = 0.5

    def draw(self, engine, display):
        for i in range(settings.LED_LENGTH):
            # the if statements below use a modulo operation to identify the even and odd numbered LEDs
            if (i % 2) == 0:
                display.set_hsv(i, self.HUE_1 / 360, 1.0, self.BRIGHTNESS)
            else:
                display.set_hsv(i, self.HUE_2 / 360, 1.0, self.BRIGHTNESS)
        time.sleep(self.SPEED)

        for i in range(settings.LED_LENGTH):
            if (i % 2) == 0:
                display.set_hsv(i, self.HUE_2 / 360, 1.0, self.BRIGHTNESS)
            else:
                display.set_hsv(i, self.HUE_1 / 360, 1.0, self.BRIGHTNESS)
        time.sleep(self.SPEED)
