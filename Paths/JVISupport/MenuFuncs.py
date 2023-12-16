import time
import pyautogui as pya


def menu():
    time.sleep(.5)
    pya.press('m')
    time.sleep(1)

'''def smoothScroll(num):
    for i in num:
        pya.scroll(1)
        time.sleep(.1)

        Not needed'''

def find(imageFile, conf):
    try:
        location = pya.locateCenterOnScreen(imageFile, confidence = conf)
        print(f"'{imageFile}' found successfully")
    except pya.ImageNotFoundException:
        print(f"'{imageFile}' not found")
        exit()
    return location

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

def checkMatch(givenImage):
    try:
        pya.locateOnScreen(givenImage, confidence = .80)
        return True
    except pya.ImageNotFoundException:
        return False

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

    FirstTP = find('./MainImages/JVIImages/OSP/FirstTP.png', .98)

    pya.moveTo(FirstTP)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    HitTPButton()
    time.sleep(2)

    while not(checkMatch('./MainImages/NotLoadingCheck.png')):
        time.sleep(1)

    print("Detected Exit")
    time.sleep(1)
    pya.click()

    
