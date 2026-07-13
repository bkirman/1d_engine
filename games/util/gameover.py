import time
import settings

# A simple animation to flash the lights on and off a few times when a game finishes.
def gameover(engine):
    for x in range(5):
        for i in range(settings.LED_LENGTH):
            engine.led_strip.set_rgb(i,100,0,0)
        time.sleep(0.1)
        for i in range(settings.LED_LENGTH):
            engine.led_strip.set_rgb(i,0,0,0)
        time.sleep(0.1)
        