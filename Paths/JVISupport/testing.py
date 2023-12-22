import time
import pyautogui as pya
from .MenuFuncs import *
from .AreaClear import *
from .MovementFuncs import *

def testFunc():

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