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
    sprW(2.0)
    scanFor(15,10)

def OSPSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVI/OSP/SecondTP.png', .95)
    print("Successfully loaded second warp")

    turnLeft(90)
    turnLeft(13)
    sprW(5.3)
    scanFor(5, 5)

def OSPThirdEnemy():
    menu()
    TPToWarp('./MainImages/JVI/OSP/ThirdTP.png', .95)
    print("Successfully loaded third warp")

    turnLeft(90)
    turnLeft(21)
    sprW(9)
    scanFor(5, 15)

def OSPFourthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/OSP/ThirdTP.png', .95)
    print("Successfully loaded fourth warp")

    turnLeft(90)
    turnLeft(13)
    sprW(7)
    turnRight(50)
    sprW(3.2)
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
    sprW(3)
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
    sprW(5.5)
    turnLeft(53)
    sprW(0.9)
    scanFor(5, 10)

def BPThirdEnemy():
    menu()

    firstWarp = find('./MainImages/JVI/BP/FirstTP.png', .90)
    pya.moveTo(firstWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

    TPToWarp('./MainImages/JVI/BP/FirstTP2.png', .90)

    sprW(.9)
    time.sleep(1)
    pya.keyDown('d')
    time.sleep(2)
    pya.keyUp('d')
    sprW(3.5)
    scanFor(5, 5)

def BPFourthEnemy():
    menu()
    adjustMenu('w', 1, 3)

    TPToWarp('./MainImages/JVI/BP/SecondTP.png', .90)
    turnLeft(90)
    turnLeft(90)
    sprW(5.4)
    turnLeft(90)
    sprW(1.5)
    scanFor(5, 10)

def BPFifthEnemy():
    menu()

    TPToWarp('./MainImages/JVI/BP/SecondTP.png', .90)
    turnLeft(90)
    turnLeft(90)
    sprW(5.8)
    turnLeft(90)
    sprW(3.6)
    scanFor(10,5)

def BPSixthEnemy():
    menu()

    TPToWarp('./MainImages/JVI/BP/SecondTP.png', .90)

    turnLeft(90)
    turnLeft(90)
    sprW(3.7)
    turnRight(90)
    sprW(4)
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
    sprW(4.8)
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
    sprW(3.7)
    time.sleep(.2)
    turnLeft(90)
    time.sleep(.2)
    sprW(7.5)
    scanFor(20, 5)

def CFEThirdEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/ThirdTP.png', .90)


    walk('a', 1.7)

    sprW(1.7)
    turnLeft(90)
    sprW(2.7)
    turnRight(90)
    sprW(3.5)
    scanFor(25, 5)

def CFEFourthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/ThirdTP.png', .90)

    walk('a', 1.7)

    sprW(1.7)
    turnLeft(90)
    sprW(2.7)
    turnRight(90)
    sprW(3.5)
    turnRight(45)
    sprW(4.2)
    turnRight(90)
    sprW(2)
    turnRight(60)
    sprW(1)
    scanFor(20, 5)

def CFEFifthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/FourthTP.png', .90)

    turnRight(30)
    sprW(3.3)
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
        sprW(2.7)
        scanFor(15, 5)

def CFESixthEnemy():
    menu()
    adjustMenu('w', 4, 3)
    adjustMenu('d', 2, 0)
    TPToWarp('./MainImages/JVI/CFE/FifthTP.png', .90)
   
    turnLeft(90)
    turnLeft(90)
    sprW(2.7)
    turnRight(60)
    scanFor(10, 5)

def CFESeventhEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/FifthTP.png', .90)

    turnLeft(90)
    turnLeft(90)
    sprW(3.1)
    turnRight(90)
    sprW(2)
    turnLeft(90)
    sprW(4)
    scanFor(5, 10)

def CFEEighthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/CFE/FifthTP.png', .90)

    turnLeft(90)
    turnLeft(90)
    sprW(3.8)
    turnLeft(45)
    sprW(4.7)
    turnRight(48)
    sprW(4.2)
    turnRight(87)
    sprW(1.0)
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
    sprW(1.7)
    turnRight(57)
    sprW(2.4)
    scanFor(5, 10)

def EHSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVI/EH/TP1.png', .90)

    turnLeft(90)
    turnLeft(45)
    sprW(1.7)
    turnRight(57)
    sprW(3.8)
    turnRight(90)
    sprW(2)
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

    sprW(4.5)
    turnLeft(80)
    sprW(3.2)
    turnLeft(35)
    sprW(1.6)
    scanFor(3, 10)

def EHFourthEnemy():
    menu()

    secondWarp = find('./MainImages/JVI/EH/SecondTP1.png', .90)
    pya.moveTo(secondWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    TPToWarp('./MainImages/JVI/EH/SecondTP2.png', .90)

    sprW(4.5)
    turnLeft(80)
    sprW(3.2)
    turnLeft(35)
    sprW(1.6)
    turnRight(20)
    sprW(1)
    turnRight(20)
    sprW(1)
    scanFor(10, 5)

#----------------------------------------------------------------------
    
def GMStart():
    menu()
    selectPlanet()
    selectParlor()
    pya.scroll(-5000)
    time.sleep(1)
    pya.scroll(-5000)
    time.sleep(1)

    GMName = find('./MainImages/JVI/GM/GreatMine.png', .85)
    time.sleep(.2)
    pya.moveTo(GMName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def GMFirstEnemy():
    adjustMenu('w', 3, 3)
    adjustMenu('d', 3, 0)
    
    TPToWarp('./MainImages/JVI/GM/FirstTP.png', .90)

    turnLeft(90)
    turnLeft(18)
    sprW(3.5)
    scanFor(5, 10)

def GMSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVI/GM/FirstTP.png', .90)

    turnLeft(90)
    turnLeft(18)
    sprW(4)
    turnRight(33)
    sprW(2.5)
    turnRight(25)
    scanFor(10, 5)

def GMThirdEnemy():
    menu()
    TPToWarp('./MainImages/JVI/GM/FirstTP.png', .90)

    turnLeft(90)
    turnLeft(18)
    sprW(4)
    turnRight(33)
    sprW(3.8)
    turnRight(90)
    turnRight(35)
    sprW(2)
    turnRight(55)
    sprW(2)
    turnLeft(38)
    sprW(1)
    turnLeft(60)
    sprW(1.5)
    scanFor(5, 5)

def GMFourthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/GM/FirstTP.png', .90)

    sprW(1.6)
    turnRight(67)
    sprW(2.5)
    scanFor(10, 5)

def GMFifthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/GM/SecondTP.png', .90)

    turnLeft(90)
    turnLeft(40)
    sprW(3.4)
    turnRight(70)
    sprW(1.0)
    turnLeft(63)
    sprW(1.6)
    scanFor(5, 5)

def GMSixthEnemy():
    thirdWarp = find('./MainImages/JVI/GM/ThirdTP1.png', .90)
    pya.moveTo(thirdWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    TPToWarp('./MainImages/JVI/GM/ThirdTP2.png', .90)

    turnRight(90)
    turnRight(12)
    sprW(2.5)
    turnLeft(45)
    sprW(2)
    scanFor(5, 5)

def GMSeventhEnemy():
    thirdWarp = find('./MainImages/JVI/GM/ThirdTP1.png', .90)
    pya.moveTo(thirdWarp)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)
    TPToWarp('./MainImages/JVI/GM/ThirdTP2.png', .90)

    turnRight(90)
    turnRight(12)
    sprW(2.5)
    turnLeft(45)
    sprW(2)
    turnLeft(55)
    sprW(1.8)
    turnRight(40)
    scanFor(10, 5)

def GMEighthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/GM/FourthTP.png', .90)

    turnLeft(65)
    sprW(2.7)
    turnLeft(65)
    sprW(2)
    altOn()
    time.sleep(.1)
    pya.click()
    altOff()
    num = countEnemies()
    print(f"{num} enemies counted")
    time.sleep(10)
    waitForLoadIn()
    if num != 3:
        menu()
        TPToWarp('./MainImages/JVI/GM/FourthTP.png', .90)
        turnLeft(65)
        sprW(2.7)
        turnLeft(60)
        sprW(2)
        scanFor(10, 5)

def GMNinthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/GM/FourthTP.png', .90)

    turnLeft(65)
    sprW(2.7)
    turnLeft(65)
    sprW(2)
    turnRight(90)
    turnRight(25)
    sprW(3)
    turnRight(75)
    sprW(1)
    scanFor(5, 10)

#----------------------------------------------------------------------
    
def RTStart():
    menu()
    selectPlanet()
    selectParlor()
    pya.scroll(-5000)
    time.sleep(1)
    pya.scroll(-5000)
    time.sleep(1)

    GMName = find('./MainImages/JVI/RT/RivetTown.png', .85)
    time.sleep(.2)
    pya.moveTo(GMName)
    time.sleep(.2)
    pya.click()
    time.sleep(.2)

def RTFirstEnemy():
    adjustMenu('w', 2, 0)
    adjustMenu('d', 1, 0)

    TPToWarp('./MainImages/JVI/RT/FirstTP.png', .90)

    walk('d', 2.7)
    walk('w', .8)
    walk('a', 3)
    walk('w', .8)
    walk('a', 5.5)
    turnLeft(15)
    sprW(1)
    scanFor(5, 5)

def RTSecondEnemy():
    menu()
    TPToWarp('./MainImages/JVI/RT/FirstTP.png', .90)

    walk('d', 2.7)
    walk('w', .8)
    walk('a', 3)
    walk('w', .8)
    walk('a', 5.5)
    sprW(2)
    turnLeft(55)
    sprW(1.5)
    scanFor(10, 5)

def RTThirdEnemy():
    menu()
    adjustMenu('s', 1, 3)
    TPToWarp('./MainImages/JVI/RT/SecondTP.png', .90)

    turnRight(90)
    turnRight(72)
    sprW(1.2)
    turnRight(90)
    sprW(1.5)
    turnRight(26)
    sprW(2.1)
    scanFor(5, 5)

def RTFourthEnemy():
    menu()
    TPToWarp('./MainImages/JVI/RT/SecondTP.png', .90)

    turnRight(90)
    turnRight(55)
    sprW(2.5)
    turnLeft(55)
    sprW(1.3)
    turnRight(90)
    sprW(3.5)
    turnLeft(90)
    sprW(2.5)
    turnLeft(90)
    sprW(1)
    if(scanFor(10, 5) == 1):
        menu()
        TPToWarp('./MainImages/JVI/RT/SecondTP.png', .90)

        turnRight(90)
        turnRight(55)
        sprW(2.5)
        turnLeft(55)
        sprW(1.3)
        turnRight(90)
        sprW(3.5)
        turnLeft(90)
        sprW(2.5)
        turnLeft(90)
        sprW(1)
        scanFor(10, 5)
