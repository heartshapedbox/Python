# Создайте программу, которая предоставляет пользователю возможность создать новый файл .csv. Программа предлагает ввести имя и возраст, а затем добавляет введенные данные в конец только что созданного файла.

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks\\')
from tkinter import *

class User():
    def __init__(self):
        self.root = Tk()
        self.root.title('User data')
        self.x = int(self.root.winfo_screenwidth() // 2)
        self.y = int(self.root.winfo_screenheight() * 0.2)
        self.x, self.y = str(self.x), str(self.y)
        self.root.geometry(f'300x200+{self.x}+{self.y}')
        self.root.resizable(False, False)
        
        
        for i in range(2):
            for y in range(4):
                self.frame = Frame(self.root);
                self.frame.grid(column = i, row = y)
            
        self.name_label = Label(self.frame, text = 'User name: ')
        self.name_label.grid(column = 0, row = 0, sticky = 'e', padx = 30, pady = 5)
        self.age_label = Label(self.frame, text = 'User age: ')
        self.age_label.grid(column = 0, row = 1, sticky = 'e', padx = 30, pady = 5)
        self.name_entry = Entry(self.frame, width = 15)
        self.name_entry.grid(column = 1, row = 0, sticky = 'w')
        self.name_entry.focus()
        self.age_entry = Entry(self.frame, width = 15)
        self.age_entry.grid(column = 1, row = 1, sticky = 'w')
        self.save_button = Button(self.frame, text = 'Save', width = 12, height = 1, bg = '#ff4d4d', fg = '#ffffff', command = self.save)
        self.save_button.grid(column = 1, row = 2, sticky = 'w')
        self.root.mainloop()
    
    def save(self):
        self.x = self.name_entry.get()
        self.y = self.age_entry.get()
        
        if self.y.isdigit():
            with open('user_data.csv', 'a', newline = "") as file:
                writer = csv.writer(file)
                tmp = [self.x, self.y]
                writer.writerow(tmp)
                self.name_entry.delete(0, END)
                self.age_entry.delete(0, END)
        else:
            self.age_entry.delete(0, END)

if __name__ == '__main__':
    user = User()