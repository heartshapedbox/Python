 #  Напишите программу, которая предлагает пользователю ввести число в текстовом поле. Когда пользователь нажимает кнопку, это число прибавляется к накапливаемой сумме и выводится в другом поле. Ввод может повторяться сколько угодно раз на усмотрение пользователя, при этом вводимые данные будут прибавляться к сумме. В окне должна присутствовать еще одна кнопка, которая обнуляет накапливаемую сумму и стирает содержимое исходного поля, чтобы пользователь мог начать ввод заново

from tkinter import *
window = Tk()
window.title('Sum')
window.geometry('300x125')

screen = Label()
screen.place(x = 20, width = 250, height = 35)
screen['bg'] = 'silver'

log = Message(text = 'log', font = ('Consolas', 8, 'italic'), width = 150)
log.place(x = 20)
log['bg'] = 'silver'
log['fg'] = 'grey'

output = Message(text = 0, font = ('Consolas', 18), width = 100)
output.place(x = 185)
output['bg'] = 'silver'

separator = ''.join(str("_") for i in range(0, 49))
separator = Label(text = separator)
separator.place(x = 20, y = 30)
separator['fg'] = 'silver'

prompt = Label(text = 'Enter a number: ')
prompt.place(x = 20, y = 75)

input = Entry(text = 0, font = ('Consolas', 18))
input.place(x = 120, y = 65, width = 50, height = 40)
input.focus()

def do():
    num = input.get()
    output['text'] = int(output['text']) + int(num)
    
    if log['text'] == "log":
        log['text'] = num
    elif len(log['text']) > 40:
        log['text'] = num
    else:
        log['text'] = f"{log['text']}+{num}"
        
    input.delete(0, END)
    
def reset():
    output['text'] = 0
    log['text'] = 'log'

sum = Button(text = 'Sum', command = do)
sum.place(x = 190, y = 65, width = 40, height = 40)
sum['bg'] = 'orange'
sum['fg'] = 'white'

reset = Button(text = 'Reset', command = reset)
reset.place(x = 230, y = 65, width = 40, height = 40)
reset['bg'] = 'red'
reset['fg'] = 'white'

window.mainloop()