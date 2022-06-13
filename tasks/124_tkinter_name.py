# Создайте окно, которое предлагает пользователю ввести имя. Когда пользователь нажимает кнопку, в окне должно выводиться сообщение «Hello [имя]» с изменением цвета фона и цвета шрифта текстовой области.

from tkinter import *

window = Tk()
window.title('Name')
window.geometry('300x150')

def get_name():
    name = input.get()
    output['text'] = str(f'Hello, {name}')
    output['bg'] = 'blue'
    output['fg'] = 'white'
    input.delete(0, END)

for i in range(0, 3):
    for y in range(0, 2):
        frame = Frame(master = window)
        frame.grid(row = i, column = y, padx = 2, pady = 2)

lbl_input = Label(master = frame, text = 'Please, enter your name: ')
lbl_input.grid(row = 0, column = 0, padx = 2, pady = 2)
lbl_input['justify'] = 'right'

lbl_output = Label(master = frame, text = 'Output:', justify = 'left')
lbl_output.grid(row = 2, column = 0, padx = 2, pady = 2)

input = Entry(master = frame, width = 20)
input.grid(row = 0, column = 1, padx = 2, pady = 2)
input.focus()

output = Message(master = frame, width = 120, text = ' ', justify = 'left')
output.grid(row = 2, column = 1, padx = 2, pady = 2)
    
btn = Button(master = frame, width = 17, text = 'Confirm', command = get_name)
btn.grid(row = 1, column = 1, padx = 2, pady = 2)
    
window.mainloop()