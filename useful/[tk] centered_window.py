from tkinter import *

root = Tk()
root.title('')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry(f'200x300+{x}+{y}')
mainloop()