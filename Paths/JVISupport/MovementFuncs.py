import time
import pyautogui as pya
from .MenuFuncs import *

def OSPStart():
    menu()
    selectPlanet()
    selectParlor()
    OSPName = find('./MainImages/JVIImages/OSP/OutlyingSnowPlains.png', .95)

    time.sleep(.2)
    pya.moveTo(OSPName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def OSPFirstEnemy():
    adjustMenu('a', 3)

    TPToWarp('./MainImages/JVIImages/OSP/FirstTP.png', .98)

    altOff()
    turnLeft(90)
    turnLeft(26)
    SprW(2.0)
    if(not(scan(15))):
        print("Scan unsuccessful")
    num = countEnemies()
    print(f"{num} enemies counted")
    time.sleep(10)
    waitForLoadIn()

def OSPSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVIImages/OSP/SecondTP.png', .95)
    print("Successfully loaded second warp")

    turnLeft(90)
    turnLeft(8)
    SprW(5.3)
    if(not(scan(5))):
        print("Scan unsuccessful")
    num = countEnemies()
    print(f"{num} enemies counted")
    time.sleep(5)
    waitForLoadIn()

