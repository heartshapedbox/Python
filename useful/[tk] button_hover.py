from tkinter import *

root = Tk()
root.title('Calculator')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry(f'320x50+{x}+{y}')
root.resizable(False, False)


background = '#1f1e24'
foreground = '#f0ebf0'
activebackground = '#f757a4'
activeforeground = '#363336'

def hover( btn, colorOnHover, colorOnLeave, colorfgOnHover, colorfgOnLeave):
    btn.bind("<Enter>", func = lambda i: btn.config(background = colorOnHover, foreground = colorfgOnHover))
    btn.bind("<Leave>", func = lambda i: btn.config(background = colorOnLeave, foreground = colorfgOnLeave))
    

btn = Button(root, text = 'Button', width = 10, height = 2)
btn.configure(
    font = ('Consolas', 8),
    background = background,
    foreground = foreground,
    relief = 'flat',
    activebackground = activebackground,
    activeforeground = activeforeground
    )
hover(btn, activebackground, background, activeforeground, foreground)
btn.pack()
root.mainloop()





