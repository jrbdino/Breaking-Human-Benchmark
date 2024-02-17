import pyautogui
import time

time.sleep(1)
screen_size = pyautogui.size()

pyautogui.screenshot()

print(pyautogui.locateOnScreen('Images/Target.png'))
print("John Cyberclubb")
