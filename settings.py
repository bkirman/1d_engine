# This file contains settings specifically for the EMF workshop on LED games. You hopefully won't need to change much in here during the workshop, but if you are following at home, or continuing to work, it will help get things working

##################### WIFI SETTINGS #####################
# This is the name and password for the WiFi network at EMF. When you get home you should change these to your own 2.4ghz WiFi network settings.

WIFI_SSID = "emf"
WIFI_PWD = "emf"

#If there are are any issues at EMF, try swapping and using the following lines to use the less secure network (we aren't doing anything sensitive!):
#WIFI_SSID = "emf-open"
#WIFI_PWD = ""

###################### LED STRIP SETTINGS #####################
# If you want to use your own WS2812/Neopixel LED strip, you can change the following settings to match your hardware. If you are using the EMF workshop kit, you shouldn't need to change anything here.

LED_COLOUR_ORDER = "RGB"  # The order of the color channels in your LED strip. Most strips are GRB, but some are RGB or BRG. Check your strip's datasheet if you're not sure, or just experiment until you figure it out!
LED_LENGTH = 50 # The number of LEDs in your strip. If you are using the EMF workshop kit, this should be 50. If you are using a different strip, change this to match the number of LEDs in your strip.

####################### ENGINE SETTINGS #####################
MAX_FPS = 60 # The max frames per second. This is quite crude at the moment