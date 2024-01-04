import time
import pyautogui as pya

def menu():
    waitForLoadIn()
    time.sleep(.5)
    pya.press('m')
    altOff()
    time.sleep(1)

def altOn():
    try:
        pya.locateCenterOnScreen('./Mainimages/Alt.png', confidence = .94)
    except pya.ImageNotFoundException:
        pya.press('alt')

def altOff():
    try:
        pya.locateCenterOnScreen('./Mainimages/Alt.png', confidence = .94)
        pya.press('alt')
    except pya.ImageNotFoundException:
        time.sleep(.2)

def resetCursor():
    pya.press('alt')
    pya.press('alt')

def find(imageFile, conf):
    for i in range(10):
        try:
            location = pya.locateCenterOnScreen(imageFile, confidence = (conf - (i * .01)))
            print(f"'{imageFile}' found successfully")
            return location
        except pya.ImageNotFoundException:
            print(f"'{imageFile}' not found, trying again...")
    print("Could not find the image after 10 tries... Exiting.")
    exit()

def checkFound(imageFile, conf):
    try:
        pya.locateCenterOnScreen(imageFile, confidence = conf)
        return True
    except pya.ImageNotFoundException:
        return False
    
def checkFoundInRegion(imageFile, conf, regionX, regionY):
    try:
        pya.locateCenterOnScreen(imageFile, region = (regionX, regionY, 1750, 950), confidence = conf, grayscale = True)
        return True
    except pya.ImageNotFoundException:
        return False
    
def waitForLoadIn():
    while not(checkFound('./MainImages/NotLoadingCheck.png', .93) and checkFound('./MainImages/HealthSample.png', .93)):
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

    Planet = find('./MainImages/XL/XLPlanet.png', .80)
    Planety = Planet.y - 100
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
    for i in range(int(10 * calcedFPS)):
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

def calibrate(): #Calculates screen references and FPS while scanning
    global scanRegionX, scanRegionY
    global calcedFPS
    framesCaptured = 0
    waitForLoadIn()
    scanRegionX, scanRegionY = find('./MainImages/NotLoadingCheck.png', .90)
    windowLeft = scanRegionX
    windowTop = scanRegionY- 950
    timeStart = time.time()
    while (time.time() < timeStart + 3):
        if checkFoundInRegion("./MainImages/EnemyMarker1.png", .95, windowLeft, windowTop):
            print("Test failed, scan function confidence should be higher if possible")
        elif checkFoundInRegion("./MainImages/EnemyMarker2.png", .95, windowLeft, windowTop):
            print("Test failed, scan function confidence should be higher if possible")
        elif checkFoundInRegion("./MainImages/Ambushed.png", .95, windowLeft, windowTop):
            print("Test failed, scan function confidence should be higher if possible")
        framesCaptured += 1
    calcedFPS = framesCaptured/3
    print(calcedFPS)

    
def turnLeft(degrees): #DO NOT turn more than 90 deg as cursor may go off screen
    resetCursor()
    #Magic ratio of pixels to degrees
    #This ratio changes based off of your FPS. 6.37 is best for 60fps
    #Can manually calibrate by lining your head up and running
    #four turnLeft(90) functions, adjusting the ratio until you
    #make a perfect 360
    pix = degrees * 6.37
    pya.dragRel(0-pix, 0, degrees/45.0, button='left')
    time.sleep(.2)
    resetCursor()

def turnRight(degrees):
    resetCursor()
    pix = degrees * 6.37
    pya.dragRel(pix, 0, degrees/45, button='left')
    time.sleep(.2)
    resetCursor()

def scan(timer):
    #Get regions for scan and set up to hit enemy
    windowLeft = scanRegionX
    windowTop = scanRegionY - 950
    angleDown()
    altOn()
    #Using time * FPS instead of just seconds passed to reduce calculations done while scanning
    for i in range(int(timer * calcedFPS)):
        if checkFoundInRegion("./MainImages/EnemyMarker1.png", .95, windowLeft, windowTop):
            print("Target Detected (Light)")
            pya.click()
            pya.press('alt')
            return True
        elif checkFoundInRegion("./MainImages/EnemyMarker2.png", .95, windowLeft, windowTop):
            print("Target Detected (Mid)")
            pya.click()
            pya.press('alt')
            return True
        elif checkFoundInRegion("./MainImages/Ambushed.png", .97, windowLeft, windowTop):
            print("Ambushed!")
            pya.press('alt')
            return True
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
