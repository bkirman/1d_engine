##################################################################################
# This code connects the buttons between the physical connections to the Plasma, and the game engine

# It is not necessary to edit this code for the workshop, but it shows how we access the pins on the Plasma, and also how we access the built in buttons.

import machine


buttons ={'b': machine.Pin(0,machine.Pin.IN,machine.Pin.PULL_UP)}
# The external button pins are soldered to the GND and TX pins on the Plasma. The TX pin corresponds to GP0 (so Pin 0 in the first bit of this line), look at the schematic here: https://shop.pimoroni.com/products/plasma-2350?variant=42092628246611
# If you wanted more buttons, you would add them a similar way, using the line above as a template, and changing the pin number to the correct pin for your button. The other pin should always be to GND. (there are 3 GND pins on the Plasma - it doesn't matter which you use)
# Technical note: we are using PULL_UP and not PULL_DOWN due to a bug in this version of the RP2350: https://forums.raspberrypi.com/viewtopic.php?t=375631

buttons['a'] = machine.Pin("BUTTON_A",machine.Pin.IN,machine.Pin.PULL_UP) # This is the built in button A.