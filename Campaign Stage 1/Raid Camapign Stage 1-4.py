#!/usr/bin/env python

import pyautogui
import time
import tkinter
from tkinter import messagebox

# hide main tkinter window
root = tkinter.Tk()
root.withdraw()

#################################################################################################

pyautogui.FAILSAFE = True

timesToRepeat = 20

converted_timesToRepeat = str(timesToRepeat)

#################################################################################################

resToCheck = pyautogui.Size(1360, 768)
resXandY = pyautogui.size()
print("NOTE: You are given 10 seconds to switch to the game if the screen resolution is correct.")
print("")
print("Your screen's current resolution is:")
print(resXandY)
time.sleep(3)
print("")      

def mainScript():
    for x in range(1,timesToRepeat):
        # actual code for the script goes below
        pyautogui.moveTo(1230,515)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(1220,650)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(800,435)
        pyautogui.click()
        time.sleep(75)
        pyautogui.moveTo(1275,55)
        pyautogui.click()
        time.sleep(5)

    messagebox.showinfo("Script is done!", "Script is done running! Script ran " + converted_timesToRepeat + " times!")

# check the screen's resolution, then runs the mainScript function above
if resXandY == resToCheck:
    print("Correct screen resolution for script detected.")
    print("Starting script in 10 seconds...")
    print("")
    time.sleep(10)
    mainScript()
else:
    print("Incorrect screen resolution detected.")
    print("Change your monitor's resolution to 1360x768 to use this script.")
    print("")