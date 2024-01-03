import time
import pyautogui as pya
from .MenuFuncs import *

def CFStart():
    menu()
    selectPlanet()
    selectParlor()
    CFName = find('./MainImages/XL/CF/Cloudford.png', .90)

    time.sleep(.2)
    pya.moveTo(CFName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def CFFirstEnemy():
    adjustMenu('w', 5, 3)
    adjustMenu('d', 1, 0)

    NormalizeFloor = find('./MainImages/XL/CF/NormalizeFloor.png', .90)
    pya.moveTo(NormalizeFloor)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/XL/CF/FirstTP.png', .90)
    calibrate()