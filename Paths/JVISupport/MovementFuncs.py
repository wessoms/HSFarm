import time
import pyautogui as pya
from .MenuFuncs import *

def OSPStart():
    menu()
    selectPlanet()
    selectParlor()
    OSPName = find('./MainImages/JVI/OSP/OutlyingSnowPlains.png', .85)

    time.sleep(.2)
    pya.moveTo(OSPName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def OSPFirstEnemy():
    adjustMenu('a', 3)

    TPToWarp('./MainImages/JVI/OSP/FirstTP.png', .98)

    altOff()
    turnLeft(90)
    turnLeft(32)
    SprW(2.0)
    scanFor(15,10)

def OSPSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVI/OSP/SecondTP.png', .95)
    print("Successfully loaded second warp")

    turnLeft(90)
    turnLeft(13)
    SprW(5.3)
    scanFor(5, 5)

def OSPThirdEnemy():
    menu()
    TPToWarp('./MainImages/JVI/OSP/ThirdTP.png', .95)
    print("Successfully loaded third warp")

    turnLeft(90)
    turnLeft(21)
    SprW(9)
    scanFor(5, 15)

def OSPFourthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/OSP/ThirdTP.png', .95)
    print("Successfully loaded fourth warp")

    turnLeft(90)
    turnLeft(13)
    SprW(7)
    turnRight(50)
    SprW(3.2)
    scanFor(5, 10)

def BPStart():
    menu()
    selectPlanet()
    selectParlor()
    BPName = find('./MainImages/JVI/BP/BackwaterPass.png', .85)

    time.sleep(.2)
    pya.moveTo(BPName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def BPFirstEnemy():
    adjustMenu('s', 4)
    adjustMenu('d', 3)

    firstWarp = find('./MainImages/JVI/BP/FirstTP.png', .95)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/JVI/BP/FirstTP2.png', .95)

    altOff()
    turnLeft(90)
    turnLeft(90)
    SprW(3)
    scanFor(10,5)

def BPSecondEnemy():
    menu()

    firstWarp = find('./MainImages/JVI/BP/FirstTP.png', .95)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/JVI/BP/FirstTP2.png', .95)

    turnLeft(90)
    turnLeft(90)
    SprW(5.5)
    turnLeft(53)
    SprW(0.9)
    scanFor(5, 10)