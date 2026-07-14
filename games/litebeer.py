from engine.game_engine import BaseGame
from .util import gameover
from random import randrange, choice
import settings
import time
from .util import connect
import urequests

class LiteBeer(BaseGame):
    """
    LiteBeer is a game about carefully pouring drinks. Don't over- or under-fill the glass! 

    The kind of drink changes based on live data from the bars at EMF.
    """

    def init(self, engine):
        self.goal = -1
        self.position = 0 # how far up the glass the player is.
        self.playing = False
        self.drink = choice(["ale"]*3 +["lager"]*2+["red_wine","white_wine"]) #get a random drink type (weighted since there is much more beer available)
        
        if(self.drink=="ale") :
            self.drink_colour = [40/360.0,0.8,0.6] #brown
            self.drink_foam = randrange(2,5) 
        elif(self.drink=="lager") :
            self.drink_colour = [70/360.0,0.8,0.6] #light yellow
            self.drink_foam = randrange(1,3)
        elif(self.drink=="red_wine") :
            self.drink_colour = [340/360.0,0.8,0.2] # dark purple
            self.drink_foam = 0
        elif(self.drink=="white_wine") :
            self.drink_colour = [82/360.0,0.2,0.7] # very light greeny yellow
            self.drink_foam = 0
        
        # Connect to the Wifi - it will then get some drink information
        #connect(settings.WIFI_SSID,settings.WIFI_PWD, verbose=True,connected= self.getDrink)
        self.getDrink("") 
        
        while(self.goal == -1):
            pass
    #-------------------------------------------
    # Ask the EMF API for information about a random drink:
    def getDrink(self,_):
        # Here are a selection of IDs, for drinks stocked at the EMF bars:
        stocklines = {'ale':[160,161,162,163,164,14,116,13,10,15,165,2,3],
                      'lager':[120,7,174,60,182,190,196],
                      'white_wine':[31,154,155,158],
                      'red_wine': [37,167]}
        stock = choice(stocklines[self.drink])
        
        if(self.drink in ['ale','lager']):
            self.goal = 49
        else:
            self.goal = 25
        
        return # <-- delete this when you edit the lines below
        # Get the data from the EMF data API:
        r = urequests.get()
        
        j = r.json()
        r.close()
        print("%s is served by the %s. There are %s units remaining from %s" %(j['fullname'], j['stock_unit_name'],j['base_units_remaining'],j['base_units_bought']))
        self.goal = int(float(j['base_units_remaining']) / float(j['base_units_bought']) * (settings.LED_LENGTH -1))

    #-------------------------------------------
    def update(self, engine, button):
        # We'll handle the button differently because we want the player to hold it down. Therefore we want to check when it is released!
        if(button['b']):
            self.playing = True
            if(self.position)> self.goal: # They overfill and lose!
                gameover(engine)
                self.init(engine)
            else:
                self.position +=1
        elif (self.playing): # If they just let go of the button but have been playing the game, figure out if they win.
            time.sleep(1) # just so we can see the results.
            if (self.position+5 < self.goal): # They stopped pouring 5 pixels too early
                gameover(engine)
            else: #they won!
                self.winner(engine) # this is an animation that "empties" the glass. See the bottom of this file
            self.init(engine) # reset the game
            
    #-------------------------------------------
    def draw(self, engine, display):
        
        # Draw the game board
        for i in range(settings.LED_LENGTH):
            if(i < self.position): #draw the drink up to that point
                if(i >= self.position - self.drink_foam): # draw the foam
                    display.set_rgb(49-i,120,120,118) #slightly yellowy white
                else:
                    display.set_hsv(49-i, self.drink_colour[0], self.drink_colour[1], self.drink_colour[2]) # draw the drink the right colour
            elif (i==self.goal):
                display.set_rgb(49-i,0,120,0) #draw the goal, to make it a bit easier! Once you get good you might delete this line.
            else:
                display.set_hsv(49-i, 0, 0, 0) # turn off this pixel (set it to "black")

        time.sleep(0.05) # wait a bit extra before the next frame, to make it look nice

    #-------------------------------------------
    # silly animation that makes the drink get drank(drunked?) when the player wins
    def winner(self,engine):
        while(self.position > 0):
            self.position -=1
            self.draw(engine, engine.led_strip)
