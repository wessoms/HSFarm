import time
import pyautogui as pya
from .MenuFuncs import *
from .AreaClear import *
from .MovementFuncs import *

def testFunc():
    turnLeft(90)
    turnLeft(28)
    sprW(1.5)
    turnRight(45)
    sprW(1.4)
    turnLeft(45)
    sprW(1.2)
    scanFor(5, 5)