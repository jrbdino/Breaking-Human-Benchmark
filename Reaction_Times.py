import pyautogui as gui

gui.click(300, 300)
green = (75, 219, 106)
while not(gui.pixelMatchesColor(300, 300, (75, 219, 106))):
    pass
gui.click(300, 300)