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

    turnRight(90)
    sprW(6.5)
    turnRight(90)
    sprW(.9)
    scanFor(10, 5)

def CFSecondEnemy():
    menu()
    TPToWarp('./MainImages/XL/CF/FirstTP.png', .90)

    turnRight(90)
    sprW(6.5)
    turnLeft(90)
    sprW(.8)
    turnLeft(90)
    sprW(1.7)
    scanFor(10, 5)

def CFThirdEnemy():
    menu() 
    TPToWarp('./MainImages/XL/CF/FirstTP.png', .90)

    turnRight(90)
    sprW(6.5)
    turnRight(90)
    sprW(3.3)
    turnRight(90)
    if(scanFor(15, 5) == 1):
        menu()
        TPToWarp('./MainImages/XL/CF/FirstTP.png', .90)
        turnRight(90)
        sprW(6.5)
        turnRight(90)
        sprW(3.3)
        turnRight(90)
        scanFor(30, 5)

def CFFourthEnemy():
    menu()
    TPToWarp('./MainImages/XL/CF/FirstTP.png', .90)

    turnRight(90)
    sprW(3.1)
    turnRight(90)
    sprW(2.7)
    turnRight(60)
    sprW(.6)
    if(scanFor(15, 10) != 3):
        menu()
        TPToWarp('./MainImages/XL/CF/FirstTP.png', .90)
        turnRight(90)
        sprW(3.1)
        turnRight(90)
        sprW(2.7)
        turnRight(60)
        sprW(.6)
        scanFor(45, 10)

def CFFifthEnemy():
    menu()
    adjustMenu('s', 5, 3)
    adjustMenu('w', 2, 0)
    time.sleep(1)
    TPToWarp('./MainImages/XL/CF/SecondTP.png', .90)

    turnRight(90)
    turnRight(45)
    sprW(1)
    turnLeft(45)
    sprW(.6)
    scanFor(15, 10)

def CFSixthEnemy():
    menu()
    TPToWarp('./MainImages/XL/CF/ThirdTP.png', .90)

    walk('d', 1.9)
    turnRight(90)
    turnRight(90)
    sprW(2.7)
    turnLeft(90)
    sprW(3.8)
    turnLeft(90)
    scanFor(15, 5)

def CFSeventhEnemy():
    menu()
    TPToWarp('./MainImages/XL/CF/ThirdTP.png', .90)

    walk('d', 1.9)
    turnRight(90)
    turnRight(90)
    sprW(2.7)
    turnLeft(90)
    sprW(3.8)
    turnLeft(90)
    sprW(3)
    scanFor(15, 5)

def CFEighthEnemy():
    menu()
    TPToWarp('./MainImages/XL/CF/ThirdTP.png', .90)

    walk('d', 1.9)
    turnRight(90)
    turnRight(90)
    sprW(3.5)
    time.sleep(1)
    walk('a', 1.8)
    sprW(7.3)
    turnLeft(60)
    sprW(1)
    scanFor(30, 5)

def CFNinthEnemy():
    menu()
    TPToWarp('./MainImages/XL/CF/ThirdTP.png', .90)

    walk('d', 1.9)
    turnRight(90)
    turnRight(90)
    sprW(3.5)
    time.sleep(1)
    walk('a', 1.8)
    sprW(7.3)
    turnLeft(38)
    sprW(3)
    scanFor(10, 5)
    