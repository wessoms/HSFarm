import pyautogui as pya
import time
import subprocess


'''def executeFile(filepath):
    try:
        completed_process = subprocess.run(['python', filepath], capture_output=True, text=True)
        if completed_process.returncode ==1:
            print(f"Failed to execute '{filepath}'")
        else:
            print("File Opened Properly")
    except FileNotFoundError:
        print(f"Error: file '{filepath}' does not exist")
'''

def openGame():
    try:
        dockIcon = pya.locateCenterOnScreen('./Mainimages/DockIcon.png')
        print("image found")
    except pya.ImageNotFoundException:
        print("image not found")
        exit()

    pya.moveTo(dockIcon.x, dockIcon.y)
    time.sleep(.5)
    pya.click()
    time.sleep(.5)
    pya.press('alt')
    pya.press('alt')
    