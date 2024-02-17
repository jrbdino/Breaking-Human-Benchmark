import pyautogui
from PIL import Image
from pytesseract import *
import time

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

screenWidth, screenHeight = pyautogui.size()

time.sleep(5)
pyautogui.screenshot('Images/numberMemory.png', region = ())
image = Image.open('Images/numberMemory.png')
number = pytesseract.image_to_string(image)

print(number)
