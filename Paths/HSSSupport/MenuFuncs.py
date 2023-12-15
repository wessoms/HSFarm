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

def selectParlor():
    time.sleep(.2)

#Scroll to top
    try: 
        MapMenu = pya.locateCenterOnScreen('./MainImages/Stamina.png', confidence = .95)
        print("Stamina Image found")
    except pya.ImageNotFoundException:
        print("Stamina image not found")
        exit()

    Mapy = MapMenu.y + 400 #idk why I cant change MapMenu.y manually
    pya.moveTo(MapMenu.x, Mapy)
    time.sleep(.2)
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
    selectParlor()
    try:
        test = pya.locateCenterOnScreen('./MainImages/HSSImages/OutlyingSnowPlains.png', confidence = .98)
        print("image found")
    except pya.ImageNotFoundException:
        print("image not found")
        exit()

    time.sleep(.2)
    pya.moveTo(test)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)