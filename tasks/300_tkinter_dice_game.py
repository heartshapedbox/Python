import random
from tkinter import *
import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme('dark-blue')

app = customtkinter.CTk()
app.title('Dice Game')
x = int(app.winfo_screenwidth() // 2)
y = int(app.winfo_screenheight() * 0.45)
x, y = str(x), str(y)
app.geometry(f'500x300+{x}+{y}')
app.resizable(0, 0)

dices = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']

label = customtkinter.CTkLabel(
    master=app, text="")


def roll():
    label.place(relx=0.5, rely=0.35, anchor=CENTER)
    label.configure(
        text=f'{random.choice(dices)}{random.choice(dices)}',
        text_color="#ededed",
        font=("Consolas", 150)
    )


button = customtkinter.CTkButton(
    master=app, cursor='hand2', text='ROLL', command=roll)
button.place(relx=0.5, rely=0.75, anchor=CENTER)
button.configure(
    font=("Consolas", 18, "bold"),
    fg_color="#608bd5",
    text_color="#ededed",
    hover_color="#3b65ad",
    corner_radius=6,
    width=75,
    height=45
)

app.mainloop()
