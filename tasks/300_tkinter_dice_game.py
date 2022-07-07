from tkinter import *
import random

window = Tk()
window.title('Dice Game')
window.geometry('500x300')
window['bg'] = '#000000'

list = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']

lbl = Label(master = window, text = ' ', font = ("Consolas", 150))

def roll():
    lbl['text'] = f'{random.choice(list)}{random.choice(list)}'
    lbl.pack()
    lbl['bg'] = '#000000'
    lbl['fg'] = '#FFFFFF'


btn = Button(master = window, font = ("Consolas", 10), text = 'Roll the Dice', command = roll, padx = 10, pady = 5)
btn.pack()
btn['bg'] = '#ff4d4d'
btn['fg'] = '#000000'

window.mainloop()