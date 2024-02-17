import pyautogui
from PIL import Image
from pytesseract import *
import time

# pyautogui.mouseInfo()
(355, 555, 1540, 680)

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

screenWidth, screenHeight = pyautogui.size()
photoWidth, photoHeight = 1000, 1000
photoLeft = 355
photoTop = 555

time.sleep(1)
pyautogui.screenshot('Images/numberMemory.png', region=(355, 555, 1240, 150))
image = Image.open('Images/numberMemory.png').convert('L')
image.save('Images/numberMemory.png')
number = pytesseract.image_to_string(image, config='')

print(number)


pyautogui.PAUSE = 2.5
benchmark = pyautogui.prompt("Please accuratly type the benchmark test snippet.  Take your time.\nWhen done, click OK and then click into the benchmark test.")
print(benchmark)
pyautogui.typewrite(benchmark)