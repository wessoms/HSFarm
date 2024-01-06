import time
import pyautogui as pya
from .MenuFuncs import *

def BZStart():
    menu()
    selectPlanet()
    selectParlor()
    BZName = find('./MainImages/HSS/BZ/BaseZone.png', .85)

    time.sleep(.2)
    pya.moveTo(BZName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def BZFirstEnemy():
    adjustMenu('s', 3, 3)
    adjustMenu('d', 1, 0)

    TPToWarp('./MainImages/HSS/BZ/FirstTP.png', .90)
    calibrate()

    turnRight(90)
    turnRight(90)
    sprW(1)
    scanFor(25, 5)

#----------------------------------------------------------------------
    
def STZStart():
    menu()
    selectPlanet()
    selectParlor()
    STZName = find('./MainImages/HSS/STZ/StorageZone.png', .85)

    time.sleep(.2)
    pya.moveTo(STZName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def STZFirstEnemy():
    adjustMenu('d', 3, 3)
    adjustMenu('w', 1, 0)

    TPToWarp('./MainImages/HSS/STZ/FirstTP.png', .85)
    calibrate()

    turnRight(90)
    turnRight(90)
    sprW(3.8)
    scanFor(10, 5)

def STZSecondEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/FirstTP.png', .85)

    turnRight(90)
    turnRight(90)
    sprW(4.0)
    turnRight(90)
    sprW(1.8)
    turnRight(90)
    sprW(4.2)
    turnLeft(90)
    sprW(1.4)
    turnLeft(90)
    sprW(1.9)
    scanFor(15, 5)

def STZThirdEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/SecondTP1.png', .85)

    turnLeft(90)
    turnLeft(90)
    scanFor(10, 5)

def STZFourthEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/FirstTP.png', .85)
    menu()
    TPToWarp('./MainImages/HSS/STZ/SecondTP2.png', .80)

    sprW(1.6)
    turnLeft(35)
    sprW(1.6)
    turnLeft(60)
    sprW(1.1)
    scanFor(10, 5)

def STZFifthEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/SecondTP2.png', .80)

    sprW(1.6)
    turnLeft(35)
    sprW(1.6)
    turnLeft(60)
    sprW(1.1)
    turnRight(90)
    turnRight(25)
    sprW(1.4)
    turnLeft(50)
    sprW(1.2)
    turnLeft(40)
    sprW(2.5)
    turnLeft(32)
    sprW(2.8)
    turnLeft(90)
    sprW(.8)
    turnRight(90)
    sprW(1)
    scanFor(10, 5)

def STZSixthEnemy():
    menu()
    adjustMenu('a', 2, 2)

    thirdWarp = find('./MainImages/HSS/STZ/ThirdTP1.png', .90)
    pya.moveTo(thirdWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/HSS/STZ/ThirdTP2.png', .90)

    turnRight(90)
    turnRight(70)
    sprW(1.7)
    turnLeft(20)
    scanFor(10, 5)

def STZSeventhEnemy():
    menu()

    thirdWarp = find('./MainImages/HSS/STZ/ThirdTP1.png', .90)
    pya.moveTo(thirdWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/HSS/STZ/ThirdTP2.png', .90)

    turnLeft(90)
    turnLeft(30)
    sprW(1.6)
    turnRight(60)
    sprW(1.2)
    turnLeft(60)
    sprW(1.2)
    scanFor(10, 10)

#----------------------------------------------------------------------
    
def SUZStart():
    menu()
    selectPlanet()
    selectParlor()
    SUZName = find('./MainImages/HSS/SUZ/SupplyZone.png', .85)

    time.sleep(.2)
    pya.moveTo(SUZName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def SUZFirstEnemy():
    adjustMenu('d', 2, 3)
    adjustMenu('s', 1, 0)

    firstWarp = find('./MainImages/HSS/SUZ/FirstTP1.png', .90)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/HSS/SUZ/FirstTP2.png', .90)
    calibrate()

    sprW(2.7)
    scanFor(10, 10)

def SUZSecondEnemy():
    menu()

    firstWarp = find('./MainImages/HSS/SUZ/FirstTP1.png', .90)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/HSS/SUZ/FirstTP2.png', .90)

    sprW(5.3)
    time.sleep(.2)
    walk('a', 3.8)
    sprW(1.8)
    scanFor(15, 5)

def SUZThirdEnemy():
    menu()

    TPToWarp('./MainImages/HSS/SUZ/SecondTP.png', .90)

    sprW(4.2)
    scanFor(15, 5)

def SUZFourthEnemy():
    menu()
    TPToWarp('./MainImages/HSS/SUZ/ThirdTP.png', .90)

    turnLeft(90)
    turnLeft(70)
    sprW(2.2)
    turnLeft(75)
    pya.press('f')

    time.sleep(2)
    waitForLoadIn
    time.sleep(.5)
    walk('w', 1)
    turnRight(90)
    sprW(3.5)
    scanFor(15, 5)

def SUZFifthEnemy():
    menu()
    TPToWarp('./MainImages/HSS/SUZ/ThirdTP2.png', .85)

    turnLeft(90)
    turnLeft(70)
    sprW(2.2)
    turnLeft(75)
    pya.press('f')

    time.sleep(2)
    waitForLoadIn
    time.sleep(.5)
    walk('w', 1)
    turnLeft(90)
    sprW(3.8)
    turnRight(90)
    sprW(2.3)
    scanFor(15, 5)

#----------------------------------------------------------------------
    
def SZStart():
    menu()
    selectPlanet()
    selectParlor()
    SZName = find('./MainImages/HSS/SZ/SeclusionZone.png', .85)

    time.sleep(.2)
    pya.moveTo(SZName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def SZFirstEnemy():
    adjustMenu('s', 3, 3)
    adjustMenu('d', 1, 0)

    NormalizeFloor = find('./MainImages/HSS/SZ/NormalizeFloor.png', .90)
    pya.moveTo(NormalizeFloor)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    Floor2 = find('./MainImages/HSS/SZ/Floor2.png', .90)
    pya.moveTo(Floor2)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/HSS/SZ/FirstTP.png', .90)
    calibrate()

    walk('w', 1)
    turnRight(90)
    sprW(5)
    turnRight(27)
    sprW(4.2)
    turnRight(28)
    sprW(2.5)
    pya.press('alt')
    pya.click()
    pya.press('alt')
    scanFor(15, 10)

def SZSecondEnemy():
    menu()
    adjustMenu('s', 3, 3)
    adjustMenu('d', 1, 0)

    TPToWarp('./MainImages/HSS/SZ/FirstTP.png', .90)
    walk('w', 1)
    turnRight(90)
    sprW(5)
    turnRight(27)
    sprW(4.2)
    turnRight(24)
    sprW(3.2)
    turnRight(24)
    sprW(2.6)
    turnRight(18)
    scanFor(40, 10)

def SZThirdEnemy():
    menu()
    adjustMenu('w', 3, 3)
    adjustMenu('d', 1, 0)
    TPToWarp('./MainImages/HSS/SZ/SecondTP.png', .90)

    turnRight(42)
    sprW(1.4)
    turnRight(45)
    sprW(.8)
    turnRight(49)
    sprW(3.6)
    turnRight(90)
    sprW(1.85)
    turnLeft(90)
    sprW(2.7)
    turnRight(35)
    sprW(5.9)
    turnRight(41)
    sprW(1.4)
    scanFor(30, 15)