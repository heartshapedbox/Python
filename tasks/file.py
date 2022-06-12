# Создайте окно, которое предлагает пользователю ввести имя. Когда пользователь нажимает кнопку, в окне должно выводиться сообщение «Hello [имя]» с изменением цвета фона и цвета шрифта текстовой области.

from tkinter import *

window = Tk()
window.title('Name')
window.geometry('300x300')

def do():
    name = input.get()
    lbl_output = Label(master = frame, text = 'Output:')
    lbl_output.place(x = 80, y = 72)
    output = Message(master = frame, text = '')
    output['text'] = name
    output.grid(row = 2, column = 1, pady = 5)

for i in range(0, 2):
    for y in range(0, 2):
        frame = Frame(master = window)
        frame.grid(row = i, column = y)

lbl = Label(master = frame, text = 'Please, enter your name: ')
lbl.grid(row = 0, column = 0, pady = 5)

input = Entry(master = frame, text = '')
input.grid(row = 0, column = 1, pady = 5)

btn = Button(master = frame, text = 'Confirm', command = do, padx = 35)
btn.grid(row = 1, column = 1, pady = 5)

window.mainloop()
