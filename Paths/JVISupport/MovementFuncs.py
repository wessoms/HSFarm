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
    adjustMenu('a', 3, 3)

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

#----------------------------------------------------------------------

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
    adjustMenu('s', 4, 3)
    adjustMenu('d', 3, 0)

    firstWarp = find('./MainImages/JVI/BP/FirstTP.png', .90)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/JVI/BP/FirstTP2.png', .90)

    altOff()
    turnLeft(90)
    turnLeft(90)
    SprW(3)
    scanFor(10,5)

def BPSecondEnemy():
    menu()

    firstWarp = find('./MainImages/JVI/BP/FirstTP.png', .90)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/JVI/BP/FirstTP2.png', .90)

    turnLeft(90)
    turnLeft(90)
    SprW(5.5)
    turnLeft(53)
    SprW(0.9)
    scanFor(5, 10)

def BPThirdEnemy():
    menu()

    firstWarp = find('./MainImages/JVI/BP/FirstTP.png', .90)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/JVI/BP/FirstTP2.png', .90)

    SprW(.9)
    time.sleep(1)
    pya.keyDown('d')
    time.sleep(2)
    pya.keyUp('d')
    SprW(3.5)
    scanFor(5, 5)

def BPFourthEnemy():
    menu()
    adjustMenu('w', 1, 3)

    TPToWarp('./MainImages/JVI/BP/SecondTP.png', .90)
    turnLeft(90)
    turnLeft(90)
    SprW(5.4)
    turnLeft(90)
    SprW(1.5)
    scanFor(5, 10)

def BPFifthEnemy():
    menu()

    TPToWarp('./MainImages/JVI/BP/SecondTP.png', .90)
    turnLeft(90)
    turnLeft(90)
    SprW(5.8)
    turnLeft(90)
    SprW(3.6)
    scanFor(10,5)

def BPSixthEnemy():
    menu()

    TPToWarp('./MainImages/JVI/BP/SecondTP.png', .90)

    turnLeft(90)
    turnLeft(90)
    SprW(3.7)
    turnRight(90)
    SprW(4)
    scanFor(5, 5)

#----------------------------------------------------------------------
    
def CFEStart():
    menu()
    selectPlanet()
    selectParlor()

    CFEName = find('./MainImages/JVI/CFE/CFE.png', .90)
    time.sleep(.2)
    pya.moveTo(CFEName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def CFEFirstEnemy():
    adjustMenu('s', 4, 3)
    adjustMenu('d', 2, 0)

    TPToWarp('./MainImages/JVI/CFE/FirstTP.png', .90)
    turnRight(90)
    turnRight(40)
    SprW(4.8)
    scanFor(10, 5)

def CFESecondEnemy():
    menu()
    adjustMenu('w', 2, 3)
    
    secondWarp = find('./MainImages/JVI/CFE/SecondTP1.png', .90)
    pya.moveTo(secondWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/JVI/CFE/SecondTP2.png', .90)
    SprW(3.7)
    time.sleep(.2)
    turnLeft(90)
    time.sleep(.2)
    SprW(7.5)
    scanFor(20, 5)

def CFEThirdEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/ThirdTP.png', .90)

    pya.keyDown('a')
    time.sleep(1.7)
    pya.keyUp('a')

    SprW(1.7)
    turnLeft(90)
    SprW(2.7)
    turnRight(90)
    SprW(3.5)
    scanFor(25, 5)

def CFEFourthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/ThirdTP.png', .90)

    pya.keyDown('a')
    time.sleep(1.7)
    pya.keyUp('a')

    SprW(1.7)
    turnLeft(90)
    SprW(2.7)
    turnRight(90)
    SprW(3.5)
    turnRight(45)
    SprW(4.2)
    turnRight(90)
    SprW(2)
    turnRight(60)
    SprW(1)
    scanFor(20, 5)

def CFEFifthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/FourthTP.png', .90)

    turnRight(30)
    SprW(3.3)
    altOn()
    time.sleep(.2)
    pya.click()
    altOff()
    num = countEnemies()
    print(f"{num} enemies counted")
    time.sleep(10)
    waitForLoadIn()
    if num != 3:
        menu() 
        TPToWarp('./MainImages/JVI/CFE/FourthTP.png', .90)
        turnRight(25)
        SprW(2.7)
        scanFor(15, 5)

def CFESixthEnemy():
    menu()
    adjustMenu('w', 4, 3)
    adjustMenu('d', 2, 0)
    TPToWarp('./MainImages/JVI/CFE/FifthTP.png', .90)
   
    turnLeft(90)
    turnLeft(90)
    SprW(2.7)
    turnRight(60)
    scanFor(10, 5)

def CFESeventhEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/FifthTP.png', .90)

    turnLeft(90)
    turnLeft(90)
    SprW(3.1)
    turnRight(90)
    SprW(2)
    turnLeft(90)
    SprW(4)
    scanFor(5, 10)

def CFEEighthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/FifthTP.png', .90)

    turnLeft(90)
    turnLeft(90)
    SprW(3.8)
    turnLeft(45)
    SprW(4.7)
    turnRight(48)
    SprW(4.2)
    turnRight(87)
    SprW(1.0)
    scanFor(10, 5)

#----------------------------------------------------------------------
    
def EHStart():
    menu()
    selectPlanet()
    selectParlor()

    EHName = find('./MainImages/JVI/EH/EverwinterHill.png', .85)
    time.sleep(.2)
    pya.moveTo(EHName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def EHFirstEnemy():
    adjustMenu('w', 3, 3)
    adjustMenu('d', 3, 0)
    adjustMenu('s', 1, 0)
    adjustMenu('a', 1, 0)

    TPToWarp('./MainImages/JVI/EH/TP1.png', .90)

    turnLeft(90)
    turnLeft(45)
    SprW(1.7)
    turnRight(57)
    SprW(2.4)
    scanFor(5, 10)

def EHSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVI/EH/TP1.png', .90)

    turnLeft(90)
    turnLeft(45)
    SprW(1.7)
    turnRight(57)
    SprW(3.8)
    turnRight(90)
    SprW(2)
    scanFor(5, 5)

def EHThirdEnemy():
    menu()
    adjustMenu('d', 1, 0)
    
    secondWarp = find('./MainImages/JVI/EH/SecondTP1.png', .90)
    pya.moveTo(secondWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    TPToWarp('./MainImages/JVI/EH/SecondTP2.png', .90)

    SprW(4.5)
    turnLeft(80)
    SprW(3.2)
    turnLeft(35)
    SprW(1.6)
    scanFor(3, 10)

def EHFourthEnemy():
    menu()

    secondWarp = find('./MainImages/JVI/EH/SecondTP1.png', .90)
    pya.moveTo(secondWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    TPToWarp('./MainImages/JVI/EH/SecondTP2.png', .90)

    SprW(4.5)
    turnLeft(80)
    SprW(3.2)
    turnLeft(35)
    SprW(1.6)
    turnRight(20)
    SprW(1)
    turnRight(20)
    SprW(1)
    scanFor(10, 5)

