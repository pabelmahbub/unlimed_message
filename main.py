import pyautogui
import time
message = 50

while message > 0:
    time.sleep(3)
    pyautogui.typewrite('Happy Moments')
    time.sleep(1)
    pyautogui.press("enter")
    message = message -1
