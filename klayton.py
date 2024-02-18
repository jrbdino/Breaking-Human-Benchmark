import PIL.ImageOps
import pyautogui
from PIL import Image
from pytesseract import *
import time

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


class NumberMemory:

    # Initial set up____________________________________________________________________________________________________
    def __init__(self):
        self.screenWidth, self.screenHeight = pyautogui.size()
        self.photoWidth, self.photoHeight = self.screenWidth // 5, self.screenHeight // 10
        self.photoLeft = self.screenWidth // 2 - self.photoWidth // 2
        self.photoTop = self.screenHeight // 2 - self.photoHeight

        self.value = None

        self.round = 0

    # Takes a screenshot, then opens and alters the image_______________________________________________________________
    def get_image(self):
        pyautogui.screenshot('Images/numberMemory.png', region=(self.photoLeft, self.photoTop,
                                                                self.photoWidth, self.photoHeight))

        image = Image.open('Images/numberMemory.png').convert('L')
        image = PIL.ImageOps.invert(image)
        image.save('Images/numberMemory.png')
        return image

    # Stores the string value of the numbers in the screenshot__________________________________________________________
    def set_value(self):
        image = self.get_image()

        # Uses the configuration for single character if it is the first round
        if self.value is None:
            self.value = pytesseract.image_to_string(image,
                                                     config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            self.round += 1
            print('round 0 value:', self.value)

        # Uses the configuration for single word if not the first round
        else:
            self.value = pytesseract.image_to_string(image,
                                                     config='--psm 8 --oem 3 -c tessedit_char_whitelist=0123456789')
            self.round += 1
            print('other round value:', self.value)

    # Writes the values in the list to the input box____________________________________________________________________
    def write_values(self):
        self.value = self.value.strip()
        pyautogui.typewrite(self.value, .1)

    # clicks the submit then next button to go to the next round________________________________________________________
    def next_round(self):
        # click submit
        time.sleep(2)
        pos = pyautogui.locateCenterOnScreen('Images/number_memory_yellow.png')
        pyautogui.moveTo(pos.x, pos.y, 1)
        pyautogui.click()
        time.sleep(2)
        # click next
        pos = pyautogui.locateCenterOnScreen('Images/number_memory_yellow.png')
        pyautogui.moveTo(pos.x, pos.y, 1)
        pyautogui.click()

    # Checks to see of the photo width should be increased______________________________________________________________
    def check_increase(self):
        if self.round == 5:
            self.photoWidth = self.screenWidth // 2
            self.photoLeft = self.screenWidth // 2 - self.photoWidth // 2
        elif self.round == 13:
            self.photoWidth = self.screenWidth
            self.photoLeft = self.screenWidth // 2 - self.photoWidth // 2

    # Runs and controls the flow of the program_________________________________________________________________________
    def run(self):
        self.check_increase()
        print('round:', self.round)
        self.set_value()
        time.sleep(self.round*1.8)
        print('Writing values')
        self.write_values()
        print('next round')
        self.next_round()
        print('running again')
        self.run()


time.sleep(5)
pos = pyautogui.locateCenterOnScreen('Images/number_memory_yellow.png')
pyautogui.moveTo(pos.x, pos.y, 1)
pyautogui.click()
NumberMemory().run()


