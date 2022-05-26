# С помощью созданного ранее файла Names.txt выведите список имен в Python. Попросите пользователя ввести одно из имен, а затем сохраните все, кроме выбранного в новом файле, под названием Names2.txt.

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

file = open('Names.txt', 'r')
print(file.read())
file.close()

file = open('Names.txt', 'r')
file.read()
name = input("Please, pick a name from the list above: ")
name = name + "\n"

for i in file:
    if i != name:
        file = open('Names2.txt', 'a')
        file.write(i)
        file.close()
file.close()

file = open('Names2.txt', 'r')
print(file.read())
