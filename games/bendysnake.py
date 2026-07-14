from engine.game_engine import BaseGame
from .util import gameover
from random import randrange
from machine import Timer
import settings
import time

class BendySnake(BaseGame):
    """
    BendySnake: A Snake-inspired game for 1 dimension. Press the button to change the snake's direction. Try to eat the yellow fruits, and avoid the red walls. Careful, the walls move faster and you get longer!
    """

    def init(self, engine): #Setting up the game
        self.ready = True # This is used for us to keep track if the game is ready to handle the button being pressed.
        self.position = 0
        self.tail = [0] # This will hold the tail of the snake as it grows.
        self.fruit = randrange(settings.LED_LENGTH-1) # Put the fruit at a random location (but not the end)
        self.wall = settings.LED_LENGTH -1 # The wall starts at the end of the strip
        self.goingRight = True # The player starts the game moving away from the wall. In the real world this can be left! It's just for consistency in the code.
        self.timer = Timer(-1) 
        
        # Add the timer code on the line above.

    #-------------------------------------------
    def update(self, engine, button): #Game Logic
        
        if(button['b'] and self.ready): #Similar button logic to before
            self.ready = False 
            self.goingRight = not self.goingRight #This flips the variable. If it was True it becomes False, and vice versa, which changes the direction
        
        elif (not button['b']): 
            self.ready = True 

        # Game Logic that happens every time:

        if (self.goingRight):
            self.position += 1 # This means "add one to self.position" - moving the player away from the Plasma by one
        else:
            self.position -= 1 # and the same for going towards the Plasma

        #If the player has gone off the end of the LED strip, we make them appear at the other end. 
        self.position %= settings.LED_LENGTH # this uses a modulo operation, if you aren't familiar, here is an intro (but not urgent!): https://pytutorial.com/python-modulo-operator-guide-usage-examples/

        # Adding the current position to the tail
        self.tail.append(self.position)
        self.tail.pop(0) #removes the oldest pixel of the tail.

        #Check for collisions:
        if (self.position == self.wall): #if the player is in the same position as a wall, the game ends, and resets. 
            gameover(engine)
            self.timer.deinit() 
            self.init(engine)
        elif (self.position == self.fruit): #if the player is in the same position as a fruit...
            self.tail.insert(0,self.position) #make our tail longer...
            self.fruit = randrange(settings.LED_LENGTH) #Move the fruit somewhere else randomly

        
    #-------------------------------------------
    def draw(self, engine, display):
        # Draw the game board
        for i in range(settings.LED_LENGTH): 
            if (i==self.position or i in self.tail):
                display.set_rgb(i, 0, 120, 0) # our snake
            
            elif (i==self.fruit):
                display.set_rgb(i, 120, 120, 0) # a fruit
            elif (i==self.wall):
                display.set_rgb(i, 120, 0, 0) # a wall

            else:
                display.set_rgb(i,0,0,0) # nothing here    

        time.sleep(0.1) # wait a bit extra before the next frame, to make it look nice

    #--------------------------------------------
    # This is a custom method that is used to place the wall randomly. It should only generate a new position at least 5 LEDs away from the player
    def placeWall(self,t):
        self.wall = (randrange(settings.LED_LENGTH-5) + self.position + 5) % settings.LED_LENGTH
