# Создайте окно, которое предлагает пользователю ввести число в текстовом поле. При нажатии кнопки используйте конструкцию varialble.isdigit() для проверки того, является ли число целым. Если проверка дает положительный результат, оно добавляется в список; в противном случае содержимое текстового поля стирается. Создайте дополнительную кнопку для очистки списка. Добавте третью кнопку для сохранения списка в файле .csv.

from fileinput import filename
from tkinter import *
from tkinter import filedialog
import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks\\')

root = Tk()
root.title('Numbers')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
x, y = str(x), str(y)
root.geometry(f'300x200+{x}+{y}')
root.resizable(False, False)

list = []

class Numbers():
    def __init__(self):
        self.input_label = Label(root, text = 'Enter a number: ').pack()
        self.input_field = Entry(root, width = 19)
        self.input_field.place(x = 90, y = 30)
        self.input_field.focus()
        self.add_button = Button(root, text = 'Add', bg = '#3c3c3c', fg = '#ffffff', command = self.add)
        self.add_button.place(x = 90, y = 60, width = 40, height = 40)
        self.save_button = Button(root, text = 'Save', bg = '#3c3c3c', fg = '#ffffff', command = self.save)
        self.save_button.place(x = 130, y = 60, width = 40, height = 40)
        self.reset_button = Button(root, text = 'Reset', bg = '#ff4d4d', fg = '#ffffff', command = self.reset)
        self.reset_button.place(x = 170, y = 60, width = 40, height = 40)
        self.output_field = Message(root, text = '', width = 250)
        self.output_field.place(x = 15, y = 115)
    
    def add(self):
        self.x = self.input_field.get()
        if str(self.x).isdigit():
            list.append(self.x)
            self.input_field.delete(0, END)
            self.output_field['text'] = ', '.join(str(i) for i in list)
        else:
            self.input_field.delete(0, END)
        
    
    def reset(self):
        self.input_field.delete(0, END)
        self.output_field['text'] = ''
        while len(list) > 0:
            for i in list:
                list.remove(i)
    
    
    def save(self):
        filename = filedialog.asksaveasfilename(initialdir = '/', title = 'Save as', initialfile = 'numbers_log', filetypes = (('csv files','*.csv'),('all files', '*.*')))
        with open(f'{filename}.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            for i in list:
                writer.writerow(i)

        
if __name__ == '__main__':
    numbers = Numbers()
root.mainloop()
