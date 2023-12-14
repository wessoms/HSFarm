import time
import pyautogui as pya


def menu():
    time.sleep(.5)
    pya.press('m')
    time.sleep(1)


def selectParlor():
    time.sleep(.2)
    try:
        PCLoc = pya.locateCenterOnScreen('./MainImages/ParlorCar1.png')
        print("image found")
    except pya.ImageNotFoundException:
        try:
            PCLoc = pya.locateCenterOnScreen('./MainImages/ParlorCar2.png')
            print("image found")
        except pya.ImageNotFoundException:
            print("image not found")
            exit()

    pya.moveTo(PCLoc)
    time.sleep(.2)
    pya.click()


def tpStart():
    menu()
    selectParlor()
    try:
        test = pya.locateCenterOnScreen('./MainImages/HSSImages/OutlyingSnowPlains.png')
        print("image found")
    except pya.ImageNotFoundException:
        print("image not found")
        exit()

    time.sleep(.2)
    pya.moveTo(test)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)