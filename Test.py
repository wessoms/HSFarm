import pyautogui as pya
import time



try:
    test = pya.locateCenterOnScreen('DockIcon.png')
    print("image found")
except pya.ImageNotFoundException:
    print("image not found")
    exit()

pya.moveTo(test)
time.sleep(.5)
pya.click()
time.sleep(1)

pya.keyDown('w')
time.sleep(2)
pya.keyUp('w')