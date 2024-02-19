import pyautogui
import pytesseract
from PIL import Image
from pytesseract import *
import time


class TypingTest:
    def __init__(self):
        pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        screenWidth, screenHeight = pyautogui.size()
        # print(screenWidth)
        photoWidth, photoHeight = screenWidth, screenHeight // 5
        photoLeft = 0
        photoTop = screenHeight // 2 - photoHeight // 2 + 90

        time.sleep(1)
        pyautogui.screenshot('../Images/Typing_Test.png', region=(photoLeft, photoTop, photoWidth, photoHeight))
        image = Image.open('../Images/Typing_Test.png').convert('L')
        image.save('../Images/Typing_Test.png')
        paragraph = pytesseract.image_to_string(image)
        benchmark = paragraph.replace("\n", " ")
        benchmark = benchmark.replace("|", "I")
        benchmark = benchmark.replace("  ", " ")

        # print(benchmark)

        pyautogui.PAUSE = 2.5
        # print(benchmark)
        pyautogui.typewrite(benchmark)
