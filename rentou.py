import pyautogui
from tkinter import messagebox
pyautogui.PAUSE = 0.001

ret = messagebox.askyesno('確認', '連投したい文字はコピーしたかな?出来たらokを押そう!')
if ret == True:
    while True:
        pyautogui.hotkey("ctrl","v")
        pyautogui.press("enter")
