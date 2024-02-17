import pyautogui as gui
gui.PAUSE = 2.5
benchmark = gui.prompt("Please accuratly type the benchmark test snippet.  Take your time.\nWhen done, click OK and then click into the benchmark test.")
print(benchmark)
gui.typewrite(benchmark)