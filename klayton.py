import pyautogui
from PIL import Image
from pytesseract import *
import time

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

screenWidth, screenHeight = pyautogui.size()
photoWidth, photoHeight = 500, screenHeight//10
photoLeft = screenWidth//2 - photoWidth//2
photoTop = screenHeight//2 - photoHeight

time.sleep(10)
pyautogui.screenshot('Images/numberMemory.png', region=(photoLeft, photoTop, photoWidth, photoHeight))
image = Image.open('Images/numberMemory.png').convert('1')
image.save('Images/numberMemory.png')
number = pytesseract.image_to_string(image, config='--psm 13')

print(number)
