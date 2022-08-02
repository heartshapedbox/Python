from tkinter import *
from threading import Timer

root = Tk()
root.title('')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry(f'200x50+{x}+{y}')


def reset_copy_message():
    message.configure(text = '')
    
    
def copy():
    message.configure(text = 'Copied!')
    Timer(0.5, reset_copy_message).start()
    

button = Button(root, text = 'Copy', command = copy)
button.pack()
message = Label(root, text = '')
message.pack()
    

mainloop()