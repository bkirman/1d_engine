import engine
from engine.game_engine import GameEngine
import animations
import games
from buttons import buttons

####################### Welcome to the Fairy Light Game Engine! #######################
# If you've used Python before, this will all be a bit familiar, but don't worry if you haven't, we'll guide you each step of the way.
#
# This bunch of code is what runs when the Plasma is switched on. It happens automatically.
# This file, main.py, has been set up to work a bit like a game console. You connect the controllers, you put the cartridge in, and then you press Go
# The code (e.g. "cartridges"!) for the games are in the games folder. There are also some non-interactive but cool animations in the animations folder.
#######################################################################################

def main():
    # This is the code the Plasma runs when it is powered on.
    # Text starting with # are comments, and are ignored by the Plasma, and are to help read what's going on.
    engine = GameEngine() # This sets up the game engine, and the LED strip, and prepares it to run a game. You should never need to change this line.

    # Load the game you want to run. Think of this like putting the cartridge in!
    engine.loadGame(games.SpaceLads())
    
    # Connect the controller on the line below
    engine.setButtons(buttons) #TODO del

    # Start the game!
    engine.run()

    # To try different built in games, change the line above like: engine.loadGame(x.y())
    # List of games and animations installed by default:
    # animations.FireEffect()
    # animations.AlternatingBlinkies()
    # animations.Pulse()
    # animations.Rainbows()
    # animations.RandomBlinkies()
    # animations.Snow()
    # animations.Demo() is a special one, that cycles through the animations when the button is pressed.

    # Games from the workshop:
    # games.PressyPressy() ❤️ 
    # games.PileUp() 💥 (part 5)
    # games.BendySnake() 🐍 (part 6)
    # games.LiteBeer() 🍺 (part 7)

    # More games as demos
    # games.RainbowPuzzle() 🌈
    # games.SpaceLads() 👾



##boring stuff to ignore
if __name__ == "__main__":
    main()