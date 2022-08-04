# Напишите программу, которая содержит: Enter student's name, Enter student's grade.
# При нажатии кнопки Add данные должны сохраняться в базе данных SQL с именем TestScores. Кнопка Clear стирает текущее содержимое окна.

from tkinter import *
from threading import Timer
import customtkinter
import sqlite3
import os
os.chdir('C:\\Users\\baben\\Documents\\DB\\')
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('dark-blue')

class App():
    def __init__(self):
        self.accent_color0 = '#ffffff'
        self.accent_color1 = '#ededed'
        self.accent_color2 = '#d9d7d7'
        self.accent_color3 = '#c7c5c5'
        self.accent_color4 = '#8c8c8c'
        self.accent_color5 = '#3b65ad'
        self.accent_color6 = '#608bd5'
        self.accent_color7 = '#f878b6'
        self.accent_color8 = '#d6478d'
        self.accent_color9 = '#000000'
        
        self.root = customtkinter.CTk()
        self.root.title('')
        self.root['bg'] = self.accent_color1
        x = int(self.root.winfo_screenwidth() // 2.3)
        y = int(self.root.winfo_screenheight() * 0.3)
        x, y = str(x), str(y)
        self.root.geometry(f'400x260+{x}+{y}')
        self.root.resizable(0, 0)
        self.show_entry()
        self.root.mainloop()
    
    
    def show_entry(self):
        self.entry_frame = customtkinter.CTkFrame(self.root)
        self.entry_frame.pack(pady = 15)
        
        self.entry_lbl_name = customtkinter.CTkLabel(self.entry_frame, text = "Enter student's name: ")
        self.entry_lbl_name.configure(bg_color = self.accent_color1)
        self.entry_lbl_name.grid(row = 0, column = 0, pady = 3)
        
        self.entry_lbl_grade = customtkinter.CTkLabel(self.entry_frame, text = "Enter student's grade: ")
        self.entry_lbl_grade.configure(bg_color = self.accent_color1)
        self.entry_lbl_grade.grid(row = 1, column = 0, pady = 3)
        
        self.entry_name = customtkinter.CTkEntry(self.entry_frame, border_width = 0, corner_radius = 6)
        self.entry_name.grid(row = 0, column = 1)
        self.entry_name.after(700, lambda: self.entry_name.focus())
        
        self.entry_grade = customtkinter.CTkEntry(self.entry_frame, border_width = 0, corner_radius = 6)
        self.entry_grade.grid(row = 1, column = 1)
        
        self.message = customtkinter.CTkLabel(self.entry_frame, text = '')
        self.message.configure(bg_color = self.accent_color1)
        self.message.grid(row = 2, columnspan = 2, pady = 3)
        self.show_add_btn()
        self.show_clear_btn()
        self.show_close_btn()
        
    
    def show_add_btn(self):
        self.add_btn = customtkinter.CTkButton(self.entry_frame, width = 150, height = 35, cursor = 'hand2', text = 'Add', command = lambda:self.add())
        self.add_btn.configure(
            fg_color = self.accent_color5,
            bg_color = self.accent_color1,
            text_color = self.accent_color1,
            hover_color = self.accent_color6,
            corner_radius = 6
        )
        self.hover(self.add_btn, self.accent_color5, self.accent_color1)
        self.add_btn.grid(row = 3, columnspan = 2, pady = 3)
    
    
    def show_clear_btn(self):
        self.clear_btn = customtkinter.CTkButton(self.entry_frame, width = 150, height = 35, cursor = 'hand2', text = 'Clear', command = lambda:self.clear())
        self.clear_btn.configure(
            fg_color = self.accent_color3,
            bg_color = self.accent_color1,
            text_color = self.accent_color0,
            hover_color = self.accent_color2,
            border_color = self.accent_color9,
            corner_radius = 6
        )
        self.hover(self.clear_btn, self.accent_color4, self.accent_color0)
        self.clear_btn.grid(row = 4, columnspan = 2, pady = 3)
        
    
    def show_close_btn(self):
        self.close_btn = customtkinter.CTkButton(self.entry_frame, width = 150, height = 35, cursor = 'hand2', text = 'Quit', command = lambda:quit())
        self.close_btn.configure(
            fg_color = self.accent_color8,
            bg_color = self.accent_color1,
            text_color = self.accent_color1,
            hover_color = self.accent_color7,
            corner_radius = 6
        )
        self.hover(self.close_btn, self.accent_color8, self.accent_color1)
        self.close_btn.grid(row = 5, columnspan = 2, pady = 3)
        
        
    def hover(self, btn, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.configure(text_color = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.configure(text_color = colorfgOnLeave))
    
    
    def remove_message(self):
        self.message.configure(text = '')
    
    
    def add(self):
        if len(self.entry_name.get()) > 0 and len(self.entry_grade.get()) > 0:
            db = sqlite3.connect('TestScores.db')
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS Grades(
                ID integer PRIMARY KEY,
                Name text NOT NULL,
                Grade text NOT NULL
            )""")
            db.commit()
            
            cursor.execute("""INSERT INTO Grades (Name, Grade) VALUES (?,?)""", (self.entry_name.get(), self.entry_grade.get()))
            db.commit()
            db.close()
            self.message.configure(text = 'Added!', text_color = self.accent_color5)
            Timer(1.5, self.remove_message).start()
        else:
            self.entry_name.focus()
            self.message.configure(text = 'Please, fill all the fields!', text_color = self.accent_color8)
            Timer(1.5, self.remove_message).start()
        
    
    def clear(self):
        for i in (self.entry_name, self.entry_grade):
            i.delete(0, END)
        self.entry_name.focus()


if __name__ == "__main__":
    App()

