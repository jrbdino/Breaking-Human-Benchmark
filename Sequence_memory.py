import time
import pyautogui


class SequenceMemory:
    def __init__(self):
        self.screen_width = pyautogui.size()[0]
        self.screen_height = pyautogui.size()[1]
        self.points = []
        self.find_grid()
        self.start()
        self.move()

    # Find the 9 points on the grid_____________________________________________________________________________________
    def find_grid(self):
        self.points = [[1576, 850], [1910, 850],
                       [2218, 850], [1576, 1180],
                       [1910, 1180], [2218, 1180],
                       [1576, 1508], [1910, 1508],
                       [2218, 1508]]

    def move(self):
        for point in self.points:
            pyautogui.moveTo(point[0], point[1], 1)

    def start(self):
        pos = pyautogui.locateCenterOnScreen('Images/number_memory_yellow.png')
        pyautogui.moveTo(pos.x, pos.y, .5)
        pyautogui.click()


time.sleep(5)
SequenceMemory()
