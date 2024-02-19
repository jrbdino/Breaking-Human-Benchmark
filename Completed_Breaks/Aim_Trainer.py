import pyautogui
import time


class AimTrainer:
    def __init__(self):
        time.sleep(1)
        pyautogui.PAUSE = 0.015
        screen_size = pyautogui.size()

        # for i in range(31):
        while 1:
            x, y = pyautogui.locateCenterOnScreen('..\Images\light blue.PNG')
            pyautogui.click(x, y)
