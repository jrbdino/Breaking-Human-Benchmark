import pyautogui as gui

for n in range(21):
    seq_xy = []
    curr_len = 4 + n
    for i in range(1, curr_len + 1):
        ref = 'Images\Chimp_Test_Images\%s.png' %(str(i))
        print(ref)
        x, y = gui.locateCenterOnScreen(ref)
        seq_xy.append([x, y])
    print(seq_xy)
    for i in range(len(seq_xy)):
        gui.click(seq_xy[i][0], seq_xy[i][1])

    x, y = gui.locateCenterOnScreen("Images\Chimp_Test_Images\Conf_Button.png")
    gui.click(x, y)