from tkinter import *
from tktooltip import ToolTip

root = Tk()
root.title('')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry(f'150x100+{x}+{y}')
root.resizable(False, False)

label = Label(root, text = "Label")
label.pack()

tip = ToolTip(label, msg = 'Label', parent_kwargs={"bg": '#000000', "padx": 1, "pady": 1}, fg='#FFFFFF', bg='#000000', pady = 2.5, delay = 0.5)

mainloop()