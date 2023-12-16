import time
import pyautogui as pya

def SprW(timer):
    pya.keyDown('w')
    time.sleep(.2)
    pya.press('shift')
    if timer > .2:
        time.sleep(timer - .2)
    pya.keyUp('w')