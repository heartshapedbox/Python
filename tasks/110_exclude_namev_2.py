# С помощью созданного ранее файла Names.txt выведите список имен в Python. Попросите пользователя ввести одно из имен, а затем сохраните все, кроме выбранного в новом файле, под названием Names2.txt.

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

with open('Names.txt', 'r') as file:
    print(file.read())
file.close()

with open('Names.txt', 'r') as file:
    name = input("Please, pick a name from the list above: ")
    name += "\n"
    for i in file:
        if i != name:
            with open('Names2.txt', 'a') as file:
                file.write(i)
            file.close()
file.close()

with open('Names2.txt', 'r') as file:
    print(file.read())
file.close()
