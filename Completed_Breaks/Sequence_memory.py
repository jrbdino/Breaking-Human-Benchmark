import time
import pyautogui


class SequenceMemory:

    # Initial set up____________________________________________________________________________________________________
    def __init__(self):
        time.sleep(5)
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

        midx = self.screen_width//2
        midy = self.screen_height//2
        separation = self.screen_width//15
        for y in range(3):
            for x in range(3):
                if x == 0:
                    posX = midx - separation
                elif x == 2:
                    posX = midx + separation
                else:
                    posX = midx

                if y == 0:
                    posY = midy - separation
                elif y == 2:
                    posY = midy + separation
                else:
                    posY = midy
                self.points.append([posX, posY])

    # Check each square to see where the next position is_______________________________________________________________
    def find_sequence(self):
        time.sleep(.5)
        for levels in range(self.level):
            time.sleep(.5)
        for point in self.points:
            if pyautogui.pixelMatchesColor(point[0], point[1], (255, 255, 255)):
                self.sequence.append([point[0], point[1]])
        self.level += 1

    # Iterate through the list of found points and click on them________________________________________________________
    def execute_sequence(self):
        time.sleep(1.5)
        for point in self.sequence:
            pyautogui.moveTo(point[0], point[1], .1)
            pyautogui.click()

    # Click the start button to begin the benchmark_____________________________________________________________________
    def start(self):
        pyautogui.moveTo(self.points[-2][0], self.points[-2][1], .2)
        pyautogui.click()

    # Control each part of the program__________________________________________________________________________________
    def run(self):
        self.find_sequence()
        self.execute_sequence()
        self.run()
