
from engine.game_engine import BaseGame
from random import uniform
import settings
import time
from pimoroni import RGBLED


class PressyPressy(BaseGame):
    """This is the very basic intro game that just shoots up a light when the button is pressed."""

    def init(self, engine):
        self.lit = False
        self.led = RGBLED("LED_R", "LED_G", "LED_B") # this is the on board led, not the led strip.
        self.fireworks = []
        self.clear = True


    def update(self, engine, button):
        self.lit = button['a'] or button['b'] # either button can be pressed
        # move any existing fireworks up the strip, and remove them if they reach the top
        for firework in self.fireworks:
            firework[1] += 1 # move the firework up one pixel
            if firework[1] >= settings.LED_LENGTH: # if it has reached the top, remove it from the list
                self.fireworks.pop(0)

        # Think about adding a new firework
        if(button['b'] and self.clear): 
            self.fireworks.append([uniform(0, 1), 0]) # add new one, with a random hue, at the start
            self.clear = False
        elif (not button['b']):
            self.clear = True # this means the button has to be let go before the next firework can be added. otherwise it gets busy!


    def draw(self, engine, display):
        # on board LED:
        if self.lit:
            self.led.set_rgb(100,0,100) #Purple: 100 red, 0 green, 100 blue. Try changing these numbers to see what happens! Choose a number between 0 and 100 for each colour channel. 0 = off, 100 = full brightness.
        else:
            self.led.set_rgb(0,10,0) #"dark" green
        # LED strip:
        for i in range(settings.LED_LENGTH):
            display.set_hsv(i, 0, 0, 0) # turn off all the pixels
        for firework in self.fireworks:
            display.set_hsv(firework[1], firework[0], 1.0, 0.6) # set the pixel at the firework's position to the firework's hue, full saturation, full brightness
        time.sleep(0.05) # wait a bit before the next frame, to make it look nice