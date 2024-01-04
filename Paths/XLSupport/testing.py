import time
import pyautogui as pya
from .MenuFuncs import *
from .AreaClear import *
from .MovementFuncs import *

def testFunc():

    walk('d', 1.9)
    turnRight(90)
    turnRight(90)
    sprW(3.5)
    time.sleep(1)
    walk('a', 1.8)
    sprW(7.3)
    turnLeft(38)
    sprW(3)
    scanFor(10, 5)
    

