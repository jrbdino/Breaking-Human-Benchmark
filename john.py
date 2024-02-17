import pyautogui
import time

time.sleep(1)
screen_size = pyautogui.size()

pyautogui.screenshot(region=(5, 220, 1890, 830))

for i in range(31):
    x, y = pyautogui.locateCenterOnScreen('Images/light blue.PNG')
    print(x, y)
    pyautogui.click(x, y)
    # print(pyautogui.mouseInfo())
