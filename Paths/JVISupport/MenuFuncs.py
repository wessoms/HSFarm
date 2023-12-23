import time
import pyautogui as pya

screenWidth, screenHeight = pya.size()

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
    while not(checkFound('./MainImages/NotLoadingCheck.png', .99) and checkFound('./MainImages/HealthSample.png', .99)):
        time.sleep(1)
    print("Successfully detected exit")
    time.sleep(1)
    
def TPToWarp(imageName, conf):
    mouseLoc = find(imageName, conf)

    pya.moveTo(mouseLoc)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    HitTPButton()
    time.sleep(2)

    waitForLoadIn()

def selectPlanet():
    PlanetMenu = find('./MainImages/OpenPlanetMenu.png', .98)
    pya.moveTo(PlanetMenu)
    time.sleep(.2)
    pya.click()
    time.sleep(1)

    Planet = find('./MainImages/JVI/JVIPlanet.png', .80)
    Planety = Planet.y - 70
    pya.moveTo(Planet.x, Planety)
    time.sleep(.5)
    pya.mouseDown()
    time.sleep(.1)
    pya.mouseUp()
    time.sleep(2)

def HitTPButton():
    TPButton = find('./MainImages/TeleportButton.png', .90)

    pya.moveTo(TPButton)
    time.sleep(.2)
    pya.click()
    time.sleep(1)

def adjustMenu(direction, times, timer):
    Zoomout = find('./MainImages/Zoomout.png', .98)
    pya.moveTo(Zoomout)
    time.sleep(.2)
    pya.mouseDown()
    time.sleep(timer)
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

def resetCursor():
    pya.press('alt')
    pya.press('alt')

def walk(direction, timer):
    pya.keyDown(direction)
    time.sleep(timer)
    pya.keyUp(direction)

def sprW(timer):
    pya.keyDown('w')
    time.sleep(.4)
    pya.mouseDown(button='right')
    time.sleep(.1)
    pya.mouseUp(button='right')
    if timer > .5:
        time.sleep(timer - .5)
    pya.keyUp('w')

def angleDown():
    resetCursor()
    pya.dragRel(0, 300, .3)
    
def turnLeft(degrees): #DO NOT turn more than 90 deg as cursor may go off screen
    resetCursor()
    #magic ratio of pixels to degrees
    if screenHeight == 1440:
        pix = degrees * 6.37
    elif (screenHeight == 2160):
        pix = degrees * 6.3
        print("4k screen detected")
    else:
        print("Your resolution has not been implemented yet")
    pya.dragRel(0-pix, 0, degrees/45.0, button='left')
    time.sleep(.2)
    resetCursor()

def turnRight(degrees):
    resetCursor()
    if screenHeight == 1440:
        pix = degrees * 6.37
    elif (screenHeight == 2160):
        pix = degrees * 6.3
        print("4k screen detected")
    else:
        print("Your resolution has not been implemented yet")
    pya.dragRel(pix, 0, degrees/45, button='left')
    time.sleep(.2)
    resetCursor()

def scan(timer): #Timer is supposed to be seconds scanned
    windowLeft, windowY = find('./MainImages/NotLoadingCheck.png', .98)
    windowTop = windowY - 950
    angleDown()
    pya.press('alt')
    for i in range(10 * timer):
        try:
            pya.locateCenterOnScreen("./MainImages/EnemyMarkerTest1.png", region = (windowLeft, windowTop, 1750, 950), confidence = .97)
            print("Target Detected")
            pya.click()
            pya.press('alt')
            return True
        except pya.ImageNotFoundException:
            pass
        try:
            pya.locateCenterOnScreen("./MainImages/EnemyMarkerTest2.png", region = (windowLeft, windowTop, 1750, 950), confidence = .97)
            print("Target Detected")
            pya.click()
            pya.press('alt')
            return True
        except pya.ImageNotFoundException:
            pass
        
    pya.press('alt')
    return False


def scanFor(scanTimer, waitTime):
    if(not(scan(scanTimer))):
        print("Scan unsuccessful")
    num = countEnemies()
    print(f"{num} enemies counted")
    time.sleep(waitTime)
    waitForLoadIn()
    return num
