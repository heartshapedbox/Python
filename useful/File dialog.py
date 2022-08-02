from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('')
x = int(root.winfo_screenwidth() // 2)
y = int(root.winfo_screenheight() * 0.2)
root.geometry(f'150x50+{x}+{y}')
root.resizable(False, False)

text = 'Some text.'

def save():
    filename =  filedialog.asksaveasfilename(initialdir = "/", title = "Save as", initialfile = 'file_name', filetypes = (("txt files","*.txt"),("all files","*.*")))
    with open(f'{filename}.txt', 'w', newline = '') as file:
        string = text
        file.write(string)
        
button = Button(root, text = "Save", command = save)
button.pack()

mainloop()