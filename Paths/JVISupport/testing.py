import time
import pyautogui as pya
from .MenuFuncs import *
from .AreaClear import *
from .MovementFuncs import *

def testFunc():

    turnLeft(65)
    SprW(2.7)
    turnLeft(65)
    SprW(2)
    turnRight(90)
    turnRight(25)
    SprW(3)
    turnRight(75)
    SprW(1)
    scanFor(5, 10)