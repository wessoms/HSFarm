import time
import pyautogui as pya

def SprW(timer):
    pya.keyDown('w')
    pya.sleep(.2)
    pya.press('shift')
    if timer > .2:
        pya.sleep(timer - .2)
    pya.keyUp('w')