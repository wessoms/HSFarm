import time
import pyautogui as pya

def resetCursor():
    pya.press('alt')
    pya.press('alt')

def SprW(timer):
    pya.keyDown('w')
    time.sleep(.4)
    pya.mouseDown(button='right')
    time.sleep(.1)
    pya.mouseUp(button='right')
    if timer > .5:
        time.sleep(timer - .5)
    pya.keyUp('w')
    
def turnLeft(degrees): #DO NOT turn more than 90 deg as cursor may go off screen
    resetCursor()
    pix = degrees * 6.715 #magic ratio of pixels to degrees
    pya.dragRel(0-pix, 0, degrees/45, button='left')
    time.sleep(.2)
    resetCursor()

def turnRight(degrees):
    resetCursor()
    pix = degrees * 6.715
    pya.dragRel(pix, 0, degrees/45, button='left')
    time.sleep(.2)
    resetCursor()