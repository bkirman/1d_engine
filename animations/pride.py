from engine.game_engine import BaseGame
import settings
import time


class Pride(BaseGame):
    """Scroll a pride flag pattern with trans pride stripes along the LED strip."""

    def init(self, engine):
        self.offset = 0.0
        self.speed = 0.03
        self.stripes = [
            (0.00, 1.0),  # red
            (0.06, 1.0),  # orange
            (0.14, 1.0),  # yellow
            (0.33, 1.0),  # green
            (0.55, 1.0),  # blue
            (0.78, 1.0),  # violet
            (0.00, 0.0),  # white
            (0.90, 0.7),  # pink
            (0.60, 0.7),  # light blue
        ]

    def draw(self, engine, display):
        self.offset += self.speed
        self.offset %= len(self.stripes)

        for i in range(settings.LED_LENGTH):
            stripe_index = int((i + self.offset) % len(self.stripes))
            hue, saturation = self.stripes[stripe_index]

            if saturation == 0.0:
                display.set_hsv(i, 0.0, 0.0, 0.8)
            else:
                display.set_hsv(i, hue, saturation, 0.7)

        time.sleep(0.05)
