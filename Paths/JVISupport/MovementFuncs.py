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

def scan(timer): #Timer is supposed to be seconds scanned
    pya.press('alt')
    for i in range(4 * timer): #Rougly 3 scans can be done per sec. Doing 4 just in case
        try:
            pya.locateCenterOnScreen("./MainImages/EnemyMarker.png", confidence = .90, grayscale = True)
            print("Target Detected")
            pya.click()
            pya.press('alt')
            return True
        except:
            time.sleep(.05)
        try:
            pya.locateCenterOnScreen("./MainImages/EnemyMarker2.png", confidence = .90, grayscale = True)
            print("Target Detected")
            pya.click()
            pya.press('alt')
            return True
        except:
            time.sleep(.05)
        
    pya.press('alt')
    return False

