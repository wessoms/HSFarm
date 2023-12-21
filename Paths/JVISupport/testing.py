import time
import pyautogui as pya
from .MenuFuncs import *
from .AreaClear import *
from .MovementFuncs import *

def testFunc():
    turnLeft(90)
    turnLeft(90)
    SprW(5.5)
    turnLeft(53)
    SprW(0.9)
    scanFor(5, 10)

