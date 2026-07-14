from engine.game_engine import BaseGame
from .util import gameover
from random import random
import settings
import time

class RainbowPuzzle(BaseGame):
    """
    RainbowPuzzle: Rotate the rainbow so pixels 0 and 1 match the target hue. You have a few seconds!
    """
    def init(self, engine):
        self.offset = 0.0  # Rainbow offset that shifts the colors
        self.target_hue = random()  # Random target hue for pixels 0 and 1
        self.start_time = time.time()  # When the game started
        self.time_limit = 5  # Seconds to complete the puzzle
        self.speed = 0.03  # How much the offset changes per frame when button held
        self.tolerance = 0.08  # How close the hue needs to match
        
    #-------------------------------------------
    def update(self, engine, button):
        # If button is held, shift the rainbow offset
        if button['b']:
            self.offset += self.speed
            self.offset %= 1.0  # Keep offset in 0-1 range
        
        # Check if time has run out
        elapsed_time = time.time() - self.start_time
        if elapsed_time > self.time_limit:
            # Time is up - check win condition
            pixel_0_hue = (self.offset + 0.0 / settings.LED_LENGTH) % 1.0
            pixel_1_hue = (self.offset + 1.0 / settings.LED_LENGTH) % 1.0
            
            # Check if both pixels match the target hue within tolerance
            if (abs(pixel_0_hue - self.target_hue) < self.tolerance and 
                abs(pixel_1_hue - self.target_hue) < self.tolerance):
                # Success! Flash green lights on pixels 0 and 1 to celebrate
                for x in range(4):
                    engine.led_strip.set_rgb(0, 0, 100, 0)
                    engine.led_strip.set_rgb(1, 0, 100, 0)
                    time.sleep(0.1)
                    engine.led_strip.set_rgb(0, 0, 0, 0)
                    engine.led_strip.set_rgb(1, 0, 0, 0)
                    time.sleep(0.1)
                # Reset the game
                self.init(engine)
            else:
                # Failed - time ran out and puzzle not solved
                gameover(engine)
                self.init(engine)
        
    #-------------------------------------------
    def draw(self, engine, display):
        # Draw the rainbow across all LEDs with current offset
        for i in range(settings.LED_LENGTH): 
            hue = (self.offset + float(i) / settings.LED_LENGTH) % 1.0
            display.set_hsv(i, hue, 1.0, 0.6)
        
        # Draw the target hue as a bright indicator on pixels 0 and 1
        # Convert target hue to RGB to show what we're aiming for
        display.set_hsv(0, self.target_hue, 1.0, 0.7)  # Target indicator
        display.set_hsv(1, self.target_hue, 1.0, 0.7)  # Target indicator

        time.sleep(0.1) # wait a bit extra before the next frame, to make it look nice
