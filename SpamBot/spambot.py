__author__ = "Adrián Gómez"
__credits__ = ["Adrian Gomez"]
__version__ = "1"
__maintainer__ = "Adrián Goméz"
__email__ = "adrian.gd@live.com"
__status__ = "Production"
__description__ = """Spambot that writes in any chat and sends the message until pressing the 'q'.
                     Be careful because if you are somewhere other than a textbox, it will press enter again and again and the computer will go crazy!"""

import pyautogui
import time
import keyboard

frase = ''      #Change to whatever you want to spam
time.sleep(5)   #Change to the time you have to click on the textbox (in seconds)

while True:
    if keyboard.is_pressed('q'): #Change to the letter you want to press to finish (Trying to improve this since sometimes it doesn't stop)
        break
    pyautogui.typewrite(frase)
    pyautogui.press('enter')