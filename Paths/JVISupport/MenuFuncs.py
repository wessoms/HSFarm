import time
import pyautogui as pya
from .MovementFuncs import *


def menu():
    time.sleep(.5)
    pya.press('m')
    altOff()
    time.sleep(1)

def altOn():
    try:
        pya.locateCenterOnScreen('./Mainimages/Alt.png', confidence = .98)
    except pya.ImageNotFoundException:
        pya.press('alt')


def altOff():
    try:
        pya.locateCenterOnScreen('./Mainimages/Alt.png', confidence = .98)
        pya.press('alt')
    except pya.ImageNotFoundException:
        time.sleep(.2)

def resetCursor():
    pya.press('alt')
    pya.press('alt')

def find(imageFile, conf):
    try:
        location = pya.locateCenterOnScreen(imageFile, confidence = conf)
        print(f"'{imageFile}' found successfully")
    except pya.ImageNotFoundException:
        print(f"'{imageFile}' not found")
        exit()
    return location

def checkFound(imageFile, conf):
    try:
        pya.locateCenterOnScreen(imageFile, confidence = conf)
        return True
    except pya.ImageNotFoundException:
        return False
    
def waitForLoadIn():
    while not(checkFound('./MainImages/NotLoadingCheck.png', .98)):
        time.sleep(1)
    
def TPToWarp(imageName, conf):
    mouseLoc = find(imageName, conf)

    pya.moveTo(mouseLoc)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    HitTPButton()
    time.sleep(.2)

    waitForLoadIn()

def selectPlanet():
    PlanetMenu = find('./MainImages/OpenPlanetMenu.png', .98)
    pya.moveTo(PlanetMenu)
    time.sleep(.2)
    pya.click()
    time.sleep(1)

    Planet = find('./MainImages/JVIImages/JVIPlanet.png', .80)
    Planety = Planet.y - 70
    pya.moveTo(Planet.x, Planety)
    time.sleep(.5)
    pya.mouseDown()
    time.sleep(.1)
    pya.mouseUp()
    time.sleep(2)

def HitTPButton():
    TPButton = find('./MainImages/TeleportButton.png', .98)

    pya.moveTo(TPButton)
    time.sleep(.2)
    pya.click()
    time.sleep(1)

def adjustMenu(direction, times):
    Zoomout = find('./MainImages/Zoomout.png', .98)
    pya.moveTo(Zoomout)
    time.sleep(.2)
    pya.mouseDown()
    time.sleep(5)
    pya.mouseUp()
    time.sleep(.2)

    for i in range(times):
        pya.keyDown(direction)
        time.sleep(.05)
        pya.keyUp(direction)
        time.sleep(1)

def selectParlor():
    time.sleep(.2)

#Scroll to top
    MapMenu = find('./MainImages/Stamina.png', .95)

    Mapy = MapMenu.y + 400 #idk why I cant change MapMenu.y manually
    pya.moveTo(MapMenu.x, Mapy)
    time.sleep(.2)
    pya.scroll(5000)
    time.sleep(1)
    pya.scroll(5000)
    time.sleep(1)


    try:
        PCLoc = pya.locateCenterOnScreen('./MainImages/ParlorCar1.png', confidence = .95)
        print("Parlor found")
    except pya.ImageNotFoundException:
        try:
            PCLoc = pya.locateCenterOnScreen('./MainImages/ParlorCar2.png', confidence = .95)
            print("Parlor found")
        except pya.ImageNotFoundException:
            print("Parlor image not found")
            exit()

    pya.moveTo(PCLoc)
    time.sleep(.2)
    pya.click()

def countEnemies():
    for i in range(40):
        if(checkFound('./MainImages/3Enemies.png', .98)):
            return 3
        if(checkFound('./MainImages/2Enemies.png', .98)):
            return 2
        time.sleep(.1)
    return 1



def OSPStart():
    menu()
    selectPlanet()
    selectParlor()
    OSPName = find('./MainImages/JVIImages/OSP/OutlyingSnowPlains.png', .98)

    time.sleep(.2)
    pya.moveTo(OSPName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    adjustMenu('a', 3)

    TPToWarp('./MainImages/JVIImages/OSP/FirstTP.png', .98)

    #Movement to first enemy
    altOff()
    turnLeft(90)
    turnLeft(26)
    SprW(2.0)
    if(not(scan(20))):
        print("Scan unsuccessful")
    num = countEnemies()
    print(f"{num} enemies counted")
    time.sleep(10)
    waitForLoadIn

def OSPSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVIImages/OSP/OSPSecondTP.png', .98)
    print("Successfully loaded second warp")
    
