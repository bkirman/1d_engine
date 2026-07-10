from engine.game_engine import BaseGame
from . import alternatingblinkies, fire, pulse, rainbows, snow, randomblinkies

class Demo(BaseGame):
    """A demo mode, that cycles through animations when buttons are pressed"""
    # Basically acts as a passthrough, but intervening on button presses to load different games. the issue is that interactive games don't work because we are using the button!
    # You could dom something similar with a timer, or use a global variable to track when a game is over. Or wire in a separate button (or use the on board ones)
 
    def init(self, engine):
        self.clear = True
        self.current = 0
        self.game = alternatingblinkies.AlternatingBlinkies()
        self.game.init(engine)

    def update(self, engine, button):
                
        if(button['b'] and self.clear): 
            self.current += 1
            if self.current >5:
                self.current = 0

            if(self.current==0):
                self.game = alternatingblinkies.AlternatingBlinkies()
            elif(self.current==1):
                self.game = fire.FireEffect()
            elif(self.current==2):
                self.game = pulse.Pulse()
            elif(self.current==3):
                self.game = rainbows.Rainbows()
            elif(self.current==4):
                self.game = snow.Snow()
            elif(self.current==5):
                self.game = randomblinkies.RandomBlinkies()
            
            self.game.init(engine)
            self.clear = False
        elif (not button['b']):
            self.clear = True 
        
        self.game.update(engine, button)
        

    def draw(self, engine, display):
        self.game.draw(engine,display)