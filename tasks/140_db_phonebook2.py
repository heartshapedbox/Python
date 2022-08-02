# Используя базу данных PhoneBook из программы 139, напишите программу, которая выводит следующее меню:
# Main Menu
# 1) View phone book
# 2) Add to phone book
# 3) Search for surname
# 4) Delete person from phone book
# 5) Quit
# Enter your selection: Если пользователь выбирает пункт 1, он сможет просмотреть всю телефонную книгу. Если он выбирает пункт 2, он сможет добавить новую запись в телефонную книгу. Если выбран пункт 3, программа предлагает ввести фамилию, а затем выводит записи всех людей с заданной фамилией. При выборе пункта 4 программа предлагает ввести идентификатор и удаляет соответствующую запись из таблицы. При выборе пункта 5 программа завершается.

from tkinter import *
import customtkinter
import sqlite3
import os
os.chdir('C:\\Users\\baben\\Documents\\DB')
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme('dark-blue')

class App():
    def __init__(self):
        self.accent_color1 = '#ededed'
        self.accent_color2 = '#2e4f87'
        self.accent_color3 = '#608bd5'
        self.accent_color4 = '#f878b6'
        self.accent_color5 = '#d6478d'
        
        self.root = customtkinter.CTk()
        self.root.title('Phone numbers')
        x = int(self.root.winfo_screenwidth() // 2.5)
        y = int(self.root.winfo_screenheight() * 0.2)
        self.root.geometry(f'400x400+{x}+{y}')
        self.root.resizable(0, 0)
        self.root['bg'] = self.accent_color1
        
        self.show_menu()
        self.root.mainloop()
    
    def show_menu(self):
        self.btn_frame = Frame(self.root, background = self.accent_color1)
        self.btn_frame.pack(pady = 70)
        
        self.btn1 = customtkinter.CTkButton(self.btn_frame, text = 'View phone book', cursor = 'hand2', width = 200, command = lambda:self.get_numbers_from_db())
        self.btn2 = customtkinter.CTkButton(self.btn_frame, text = 'Add to phone book', cursor = 'hand2', width = 200)
        self.btn3 = customtkinter.CTkButton(self.btn_frame, text = 'Search for surname', cursor = 'hand2', width = 200)
        self.btn4 = customtkinter.CTkButton(self.btn_frame, text = 'Delete person from phone book', cursor = 'hand2', width = 200)
        self.btn5 = customtkinter.CTkButton(self.btn_frame, text = 'Quit', cursor = 'hand2', width = 200)
        
        for i in (self.btn1, self.btn2, self.btn3, self.btn4):
            i.configure(
                fg_color = self.accent_color2,
                hover_color = self.accent_color3,
                text_color = self.accent_color1,
                corner_radius = 6
            )
            self.btn_hover(i, self.accent_color2, self.accent_color1)
            i.pack(pady = 2, ipadx = 2, ipady = 5)
            
            
        self.btn5.configure(
            fg_color = self.accent_color5,
            hover_color = self.accent_color4,
            text_color = self.accent_color1,
            corner_radius = 6
        )
        self.btn_hover(self.btn5, self.accent_color5, self.accent_color1)
        self.btn5.pack(pady = 2, ipadx = 2, ipady = 5)
    
    
    def btn_hover(self, btn, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.configure(text_color = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.configure(text_color = colorfgOnLeave)) 
    
    
    def get_numbers_from_db(self):
        self.btn_frame.destroy()
        self.db_frame = Frame(self.root, background = self.accent_color1)
        self.db_frame.pack(pady = 40)
        self.label = customtkinter.CTkLabel(self.db_frame, text = '')
        self.btn_back = customtkinter.CTkButton(self.root, text = '<', command = lambda:self.back())
        self.btn_back.configure(
            fg_color = self.accent_color2,
            hover_color = self.accent_color3,
            text_color = self.accent_color1,
            corner_radius = 6
        )
        self.btn_hover(self.btn_back, self.accent_color2, self.accent_color1)
        self.btn_back.place(x = 30, y = 30, width = 30, height = 30)
        
        tmp = []
        db = sqlite3.connect('PhoneBook.db')
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM Names""")
        for i in cursor.fetchall():
            tmp.append(f'{i[0]}: {i[1]} {i[2]}, Phone: {i[3]}')
            
        self.label.configure(
            text = '\n\n'.join(str(i) for i in tmp),
            justify = LEFT,
            bg_color = self.accent_color1
            )
        self.label.pack()
    
    
    def back(self):
        self.db_frame.destroy()
        self.btn_back.destroy()
        self.show_menu()


if __name__ == "__main__":
    App()