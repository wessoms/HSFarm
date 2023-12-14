import pyautogui as pya
import time

test = pya.locateCenterOnScreen('DockIcon.png')

if test == None:
    print("Not found")

pya.moveTo(test, test)
time.sleep(.5)
pya.click()
time.sleep(1)


time.sleep(.5)
pya.press('m')
time.sleep(.5)

test = pya.locateCenterOnScreen('ParlorCar1.png')
if test == None:
    test = pya.locateCenterOnScreen('ParlorCar2.png')
    if test == None:
        print("Map not entered successfully")
        exit

pya.moveTo(test)
time.sleep(.5)
pya.click()
time.sleep(.2)

test = pya.locateCenterOnScreen('PomPomLogo.png', confidence=.8)
pya.moveTo(test)
time.sleep(.3)
pya.click()
time.sleep(.2)

test = pya.locateCenterOnScreen('TeleportButton.png')
pya.moveTo(test)
time.sleep(.2)
pya.click()