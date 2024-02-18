import tkinter
import os
from Completed_Breaks.Aim_Trainer import AimTrainer
from Completed_Breaks.Chimp_Test import ChimpTest
from Completed_Breaks.Reaction_Times import ReactionTime
from Completed_Breaks.Typing_Test import TypingTest
from Completed_Breaks.Sequence_memory import SequenceMemory
from Completed_Breaks.Number_Memory import NumberMemory


screen = tkinter.Tk()
screen.title('Breaking Human Benchmark')


def add_buttons():
    dir = os.listdir('./')
    for file in dir:
        if file == '__pycache__' or file == 'main.py':
            pass
        elif file == 'Aim_Trainer.py':
            button = tkinter.Button(screen, text='Aim Trainer', width=25, command=AimTrainer)
            button.pack()
        elif file == 'Chimp_Test.py':
            button = tkinter.Button(screen, text='Chimp Test', width=25, command=ChimpTest)
            button.pack()
        elif file == 'Number_Memory.py':
            button = tkinter.Button(screen, text='Number Memory', width=25, command=NumberMemory)
            button.pack()
        elif file == 'Reaction_Times.py':
            button = tkinter.Button(screen, text='Reaction Times', width=25, command=ReactionTime)
            button.pack()
        elif file == 'Sequence_memory.py':
            button = tkinter.Button(screen, text='Sequence Memory', width=25, command=SequenceMemory)
            button.pack()
        elif file == 'Typing_Test.py':
            button = tkinter.Button(screen, text='Typing Test', width=25, command=TypingTest)
            button.pack()


add_buttons()
screen.mainloop()
