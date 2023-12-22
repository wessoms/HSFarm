import time
import pyautogui as pya
from .MenuFuncs import *
from .AreaClear import *
from .MovementFuncs import *

def testFunc():
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