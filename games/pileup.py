from engine.game_engine import BaseGame
from .util import gameover
from random import uniform
import settings
import time

class PileUp(BaseGame):
    """
    PileUp: a light will move up the string, and you must press the button to stop it before it hits another light
    Try and light up every light!

    This game provides a simple template to copy/paste and make your own game.
    """

    # init(ialise) is run once, when the game first starts. 
    # It is the place where we will set up our game board, and get ready.
    def init(self, engine):
        self.board = [0] * settings.LED_LENGTH #Make a variable that is a list of "0"s equal to the length of the LED strip. This is our game board, and it starts empty.
        self.ready = True # This is used for us to keep track if the game is ready to handle the button being pressed.
        self.position = settings.LED_LENGTH # position tracks the current position of the player. They start at 50, which is the position furthest from the Plasma board.
    #-------------------------------------------
    # update is run up to 60 times per second. The game engine will also tell us which buttons have been pressed.
    # This is where we do the logic of the game, and handle input.
    def update(self, engine, button):
        
        # Let's check to see if the button has been pressed. For this game there is a bit of logic where we wait until we are "ready". This means we only handle each button press once. For other games you might want to allow players to hold the button down.
        if(button['b'] and self.ready): #if self.ready is "True" that means the button has just been pressed and is not held down.
            self.ready = False #We only want to do the next bit of code once, to avoid the holding down.
            self.board[self.position] = 1 #Set the space of the game board where the player is, to indicate there is now an obstacle here
            self.position = 0 # Reset the player back to the start of the game.
        
        elif (not button['b']): #Else If the button is not being pressed: 
            self.ready = True # Now we are ready for the player to press it again, next time the update code is run.

        # Game Logic that happens every time:
        self.position = self.position - 1 # the player pixel moves down the board one space automatically

        if(self.position < 0): # If the player has gone off the end of the board!
            self.position = settings.LED_LENGTH -1 # put it back to the top
        
        #Check for collisions:
        if (self.board[self.position] != 0): # the player has crashed into something!
            pass
            
        
    #-------------------------------------------
    # draw is run straight after update, and is where we actually "draw" the lights onto the LED strip.
    def draw(self, engine, display):
        # Draw the game board
        for i in range(settings.LED_LENGTH): # this loops through every pixel, running the code below, where i=0, then i=1, etc, to i=50
            if(self.board[i] == 0): # If the game board element "i" is 0, then there is nothing at that position
                display.set_hsv(i, 0, 0, 0) # so turn off this pixel (set it to "black")
            else: # something IS in this position
                display.set_hsv(i, self.board[i], 1.0, 0.6) #set the pixel to be lit up

        # Draw the pixel where the player is:
        display.set_rgb(self.position, 120, 120, 0)

        time.sleep(0.1) # wait a bit extra before the next frame, to make it look nice
