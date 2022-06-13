# Напишите программу, моделирующую бросок шестигранного кубика в настольной игре. Когда пользователь нажимает кнопку, на экране должно выводиться случайное целое число от 1 до 6 (включительно).

from tkinter import *
import random

window = Tk()
window.title('Random number')
window.geometry('300x100')

def do():
    num = random.randrange(1, 7)
    output['text'] = str(num)
    output.pack()

btn = Button(master = window, text = 'Generate', command = do)
btn.pack()

output = Message(master = window, text = ' ')

window.mainloop()
