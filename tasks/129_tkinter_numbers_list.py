# Создайте окно, которое предлагает пользователю ввести число в текстовом поле. При нажатии кнопки используйте конструкцию varialble.isdigit() для проверки того, является ли число целым. Если проверка дает положительный результат, оно добавляется в список; в противном случае содержимое текстового поля стирается. Создайте дополнительную кнопку для очистки списка.

from os import remove
from tkinter import *

from numpy import number

root = Tk()
root.title('Numbers')
root.resizable(False, False)
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry('300x200+' + str(x) + '+' + str(y))


numbersList = []


def add():
    i = input.get()
    if i.isdigit():
        numbersList.append(i)
    output['text'] = ','.join(i for i in numbersList)
    input.delete(0, END)
    
    
def reset():
    while len(numbersList) > 0:
        for i in numbersList:
            numbersList.remove(i)
        output['text'] = ''


lbl = Label(root, text = 'Enter a number: ')
lbl.pack()
input = Entry(root, width = 16)
input.pack()
input.focus()
addToListButton = Button(root, text = 'Add', bg = '#3c3c3c', fg = '#ffffff', command = add)
addToListButton.place(x = 100, y = 50, width = 50, height = 50)
cleanListButton = Button(root, text = "Reset", bg = '#ff4d4d', fg = '#ffffff', command = reset)
cleanListButton.place(x = 150, y = 50, width = 50, height = 50)
output = Message(root, text = '', width = 225)
output.place(x = 25, y = 100)
root.mainloop()