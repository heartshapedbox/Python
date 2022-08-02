from tkinter import *
import pyperclip

root = Tk()
root.title('')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry(f'150x100+{x}+{y}')
root.resizable(False, False)

label = Label(root, text = '')
label.pack()
label['text'] = "Copied!"

def copy():
    pyperclip.copy(label['text'])

button = Button(root, text = 'Copy', command = copy)
button.pack()

mainloop()