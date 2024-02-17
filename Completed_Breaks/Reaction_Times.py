import pyautogui as gui

gui.PAUSE = 2
x, y = gui.position()
green = (75, 219, 106)
while not(gui.pixelMatchesColor(x, y, (75, 219, 106))):
    pass
gui.click(x, y)