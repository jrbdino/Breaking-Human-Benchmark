import time
import pyautogui


class SequenceMemory:
    def __init__(self):
        self.screen_width = pyautogui.size()[0]
        self.screen_height = pyautogui.size()[1]
        self.level = 1
        self.points = []
        self.sequence = []
        self.find_grid()

        self.start()
        self.run()

    # Find the 9 points on the grid_____________________________________________________________________________________
    def find_grid(self):
        self.points = [[1576, 850], [1910, 850],
                       [2218, 850], [1576, 1180],
                       [1910, 1180], [2218, 1180],
                       [1576, 1508], [1910, 1508],
                       [2218, 1508]]

    def find_sequence(self):
        time.sleep(.5)
        for levels in range(self.level):
            time.sleep(.4)
            for point in self.points:
                if pyautogui.pixelMatchesColor(point[0], point[1], (255, 255, 255)):
                    self.sequence.append([point[0], point[1]])
        self.level += 1

    def execute_sequence(self):
        time.sleep(1)
        while len(self.sequence) > 0:
            pos = self.sequence.pop(0)
            pyautogui.moveTo(pos[0], pos[1], .1)
            pyautogui.click()

    def move(self):
        for point in self.points:
            pyautogui.moveTo(point[0], point[1], 1)

    def start(self):
        # pos = pyautogui.locateCenterOnScreen('../Images/start_button.png')
        # pyautogui.moveTo(pos.x, pos.y, .5)
        pyautogui.moveTo(1900, 1440, .5)
        pyautogui.click()

    def run(self):
        self.find_sequence()
        self.execute_sequence()
        self.run()

        # self.move()
        # pyautogui.mouseInfo()


time.sleep(5)
SequenceMemory()
