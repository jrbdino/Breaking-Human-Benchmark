import pyautogui
from PIL import Image
from pytesseract import *
import time

# pyautogui.mouseInfo()
(345, 505, 1540, 680)

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# screenWidth, screenHeight = pyautogui.size()
# photoWidth, photoHeight = 1000, 1000
# photoLeft = 355
# photoTop = 545
screenWidth, screenHeight = pyautogui.size()
print(screenWidth)
photoWidth, photoHeight = screenWidth, screenHeight//5
# photoLeft = ((7*screenWidth)//216) - ((31 * photoWidth)//48)
photoLeft = 0
photoTop = screenHeight//2 - photoHeight//2 + 90


# left_x, top_y = pyautogui.locateCenterOnScreen('Images/typing_top_left.PNG')
# right_x, bottom_y = pyautogui.locateCenterOnScreen('Images/typing_bottom_right.PNG')


time.sleep(1)
# pyautogui.screenshot('Images/numberMemory.png', region=(photoLeft, photoTop, photoWidth, photoHeight))
pyautogui.screenshot('Images/Typing_Test.png', region=(photoLeft, photoTop, photoWidth, photoHeight))
# pyautogui.screenshot('Images/Typing_Test.png', region=(355, 495, 1240, 275))
# pyautogui.screenshot('Images/Typing_Test.png', region=(left_x, top_y, (right_x - left_x), (bottom_y - top_y)))
image = Image.open('Images/Typing_Test.png').convert('L')
image.save('Images/Typing_Test.png')
number = pytesseract.image_to_string(image, config='')

print(number)


pyautogui.PAUSE = 2.5
benchmark = pyautogui.prompt("Please accurately type the benchmark test snippet.  Take your time.\nWhen done, click OK and then click into the benchmark test.")
print(benchmark)
pyautogui.typewrite(benchmark)