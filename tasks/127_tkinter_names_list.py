 #  Создайте окно, которое предлагает пользователю ввести имя в текстовом поле. Когда пользователь нажимает кнопку, имя добавляется в конец списка, выводимого на экране. Создайте еще одну кнопку для очистки списка.

from tkinter import *

window = Tk()
window.title('Names list')
window.geometry('400x200')

names_list = []

def add():
    name = input.get()
    names_list.append(name)
    output['text'] = ', '.join(str(i) for i in names_list)
    input.delete(0, END)

def reset():
    while len(names_list) > 0:
        for i in names_list:
            names_list.remove(i)
    output['text'] = ''

lbl = Label(text = 'Enter a name: ')
lbl.place(x = 150, y = 10)

input = Entry(text = '')
input.place(x = 140, y = 30, width = 100)
input.focus()

add = Button(text = 'Add', command = add)
add.place(x = 140, y = 55, width = 50, height = 50)
add['bg'] = '#3c3c3c'
add['fg'] = '#ffffff'

reset = Button(text = 'Reset', command = reset)
reset.place(x = 190, y = 55, width = 50, height = 50)
reset['bg'] = '#ff4d4d'
reset['fg'] = '#ffffff'

output = Message(text = '', width = 270)
output.place(x = 50, y = 120)

window.mainloop()