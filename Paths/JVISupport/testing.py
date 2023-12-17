from .MenuFuncs import *
from .OutlyingSnowPlains import *
from .MovementFuncs import *


def testFunc():
    altOff()
    if(not(scan(20))):
        print("Scan unsuccessful")
    num = countEnemies()
    print(f"{num} enemies counted")