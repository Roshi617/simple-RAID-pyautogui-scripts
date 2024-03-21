#!/usr/bin/env python

# modules
import pyautogui
import time
import tkinter
from tkinter import messagebox

# hide main tkinter window
root = tkinter.Tk()
root.withdraw()

# emergency stop the script when you move the mouse to the upper-left of the screen 
pyautogui.FAILSAFE = True

# configurations and type conversions
lengthOfBattle = input("How long will the legnth of the battle be? NOTE: This includes the loading screen. ")
converted_lengthOfBattle = int(lengthOfBattle)

timesToRepeat = input("How many times to repeat battle? ")
converted_timesToRepeat = int(timesToRepeat)

resToCheck = pyautogui.Size(1920, 1080)
resXandY = pyautogui.size()

print("NOTE: You are given 10 seconds to switch to the game if the screen resolution is correct.")
print("")
print("Your screen's current resolution is:")
print(resXandY)
time.sleep(3)
print("")

# the function that does all the magic
def mainScript():
    for x in range(1,converted_timesToRepeat):
        # actual code for the script goes below
        pyautogui.moveTo(1700,975)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(1180,660)
        pyautogui.click()
        time.sleep(converted_lengthOfBattle)
        pyautogui.moveTo(1400,990)
        pyautogui.click()
        time.sleep(5)

    messagebox.showinfo("Script is done!", "Script is done running! Script ran " + timesToRepeat + " times!")

# check the screen's resolution, then runs the mainScript function above
if resXandY == resToCheck:
    print("Correct screen resolution for script detected.")
    print("Starting script in 10 seconds...")
    print("")
    time.sleep(10)
    mainScript()
else:
    print("Incorrect screen resolution detected.")
    print("Change your monitor's resolution to 1920x1080 to use this script.")
    print("")