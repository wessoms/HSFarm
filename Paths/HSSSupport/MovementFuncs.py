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

    turnRight(90)
    turnRight(90)
    sprW(1)
    scanFor(10, 5)

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

    TPToWarp('./MainImages/HSS/STZ/FirstTP.png', .90)

    turnRight(90)
    turnRight(90)
    sprW(3.8)
    scanFor(5, 5)

def STZSecondEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/FirstTP.png', .90)

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
    scanFor(10, 5)

def STZThirdEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/SecondTP.png', .90)

    turnLeft(90)
    turnLeft(90)
    scanFor(5, 5)

def STZFourthEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/FirstTP.png', .90)
    menu()
    TPToWarp('./MainImages/HSS/STZ/SecondTP.png', 90)

    sprW(1.4)
    turnLeft(35)
    sprW(1.4)
    turnLeft(60)
    sprW(.9)
    scanFor(5, 5)

def STZFifthEnemy():
    menu()
    TPToWarp('./MainImages/HSS/STZ/SecondTP.png', .90)

    sprW(1.4)
    turnLeft(35)
    sprW(1.4)
    turnLeft(60)
    sprW(.9)
    turnRight(90)
    turnRight(25)
    sprW(1.3)
    turnLeft(50)
    sprW(1)
    turnLeft(40)
    sprW(2.4)
    turnLeft(32)
    sprW(2.8)
    turnLeft(90)
    sprW(.8)
    turnRight(90)
    sprW(1)
    scanFor(5, 5)

def STZSixthEnemy():
    menu()
    adjustMenu('a', 2, 2)

    thirdWarp = find('./MainImages/JVI/CFE/SecondTP1.png', .90)
    pya.moveTo(thirdWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/HSS/STZ/ThirdTP2.png', .90)

    turnRight(90)
    turnRight(70)
    sprW(1.7)
    turnLeft(20)
    scanFor(5, 5)

def STZSeventhEnemy():
    menu()

    thirdWarp = find('./MainImages/JVI/CFE/SecondTP1.png', .90)
    pya.moveTo(thirdWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/HSS/STZ/ThirdTP2.png', .90)

    #Finish this!

