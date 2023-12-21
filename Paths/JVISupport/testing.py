import time
import pyautogui as pya
from .MenuFuncs import *
from .OutlyingSnowPlains import *
from .MovementFuncs import *

def testFunc():
    menu()
    TPToWarp('./MainImages/JVIImages/OSP/ThirdTP.png', .95)
    print("Successfully loaded third warp")

    turnLeft(90)
    turnLeft(13)
    SprW(9)
    if(not(scan(5))):
        print("Scan unsuccessful")
    num = countEnemies()
    print(f"{num} enemies counted")
    time.sleep(5)
    waitForLoadIn()

