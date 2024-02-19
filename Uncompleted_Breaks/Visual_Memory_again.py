#starting at 3x3, every 3 levels n+1xn+1.  Level 6 gets us to 4x4 and so forth.
import time
import pyautogui as gui


height, width = gui.size()
time.sleep(2.0)
gui.click(gui.locateCenterOnScreen("Images/1080p_start_button.png"))
time.sleep(0.5)
b1x, b1y = int(height / 4.5), int(width / 4)
b2x, b2y = (b1x * 2), (b1y * 2)
gui.screenshot("Vis_Mem_Test.png", region=(b1x, b1y, b2x, b2y))
print(b1x, b1y, b2x, b2y)
while True:
    arr = list(gui.locateAllOnScreen("Images/White_Square.png", region=(b1x, b1y, b2x, b2y)))
    for i in range(len(arr)):
        gui.click(arr[i])
    