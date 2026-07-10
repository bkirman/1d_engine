from random import uniform

from engine.game_engine import BaseGame
import settings

# The following is adapted from the Pimoroni Plasma library's example code, that can be found here: https://github.com/pimoroni/plasma/tree/main/examples
# It has been adjusted to work with the 1d engine framework developed for the EMF workshop on games for LED strips.

class Snow(BaseGame):

    """
    Snow in a bottle! Always winter, never Christmas!
    Adjust SNOW_INTENSITY for more snow.
    """

    def init(self, engine):
        # How much snow? [bigger number = more snowflakes]
        self.SNOW_INTENSITY = 0.0002

        # Change RGB colours here (RGB colour picker: https://g.co/kgs/k2Egjk )
        self.BACKGROUND_COLOUR = [30, 50, 50]  # dim blue
        self.SNOW_COLOUR = [180, 180, 180]  # bluish white

        # how quickly current colour changes to target colour [1 - 255]
        self.FADE_UP_SPEED = 255  # abrupt change for a snowflake
        self.FADE_DOWN_SPEED = 1

        # Create a list of [r, g, b] values that will hold current LED colours, for display
        self.current_leds = [[0] * 3 for i in range(settings.LED_LENGTH)]
        # Create a list of [r, g, b] values that will hold target LED colours, to move towards
        self.target_leds = [[0] * 3 for i in range(settings.LED_LENGTH)]                

    def update(self, engine, button):
        for i in range(settings.LED_LENGTH):
            # randomly add snow
            if self.SNOW_INTENSITY > uniform(0, 1):
                # set a target to start a snowflake
                self.target_leds[i] = self.SNOW_COLOUR
            # slowly reset snowflake to background
            if self.current_leds[i] == self.target_leds[i]:
                self.target_leds[i] = self.BACKGROUND_COLOUR
        # nudge our current colours closer to the target colours
        for i in range(settings.LED_LENGTH):
            for c in range(3):  # 3 times, for R, G & B channels
                if self.current_leds[i][c] < self.target_leds[i][c]:
                    self.current_leds[i][c] = min(self.current_leds[i][c] + self.FADE_UP_SPEED, self.target_leds[i][c])  # increase current, up to a maximum of target
                elif self.current_leds[i][c] > self.target_leds[i][c]:
                    self.current_leds[i][c] = max(self.current_leds[i][c] - self.FADE_DOWN_SPEED, self.target_leds[i][c])  # reduce current, down to a minimum of target


    def draw(self, engine, display):
        for i in range(settings.LED_LENGTH):
            display.set_rgb(i, self.current_leds[i][0], self.current_leds[i][1], self.current_leds[i][2])



