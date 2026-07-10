from time import sleep
import plasma
import settings

############################ WARNING ############################
# This file is the core engine of the 1d game system. 
# You should be careful editing here because it might break every game.
# However please do look around and see how it works!
# You can find the original code for this, linked in the workshop material in case of disaster.
#################################################################

class BaseGame:
    """Games should override init(), update(), and draw()."""

 
    def init(self, engine):
        pass

    def update(self, engine, button):
        pass

    def draw(self, engine, display):
        pass


class GameEngine:
    def __init__(self):
        # Set up the LED strip based on the settings in settings.py
        self.led_strip = plasma.WS2812(settings.LED_LENGTH, color_order= plasma.COLOR_ORDER_RGB if settings.LED_COLOUR_ORDER == "RGB" else plasma.COLOR_ORDER_GRB if settings.LED_COLOUR_ORDER == "GRB" else plasma.COLOR_ORDER_BRG)
        self.running = False
        self.buttons_in = {}

    def setButtons(self, buttons):
        self.buttons_in = buttons

    def loadGame(self, game):
        self.game = game

    def stop(self):
        self.running = False
        self.led_strip.stop()

    def run(self):
        self.running = True
        self.led_strip.start()
        self.game.init(self)

        while self.running:
            if self.buttons_in:
                btns = {'a': self.buttons_in['a'].value()==0, 'b': self.buttons_in['b'].value()==0}
            else:
                btns = {'a': False, 'b': False}
            self.game.update(self, btns)
            self.game.draw(self, self.led_strip)
            sleep(1.0 / settings.MAX_FPS)  # Limit the frame rate to MAX_FPS

