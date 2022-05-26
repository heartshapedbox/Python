# С помощью созданного ранее файла Names.txt выведите список имен в Python. Попросите пользователя ввести одно из имен, а затем сохраните все, кроме выбранного в новом файле, под названием Names2.txt.

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

file = open('Names.txt', 'r')
print(file.read())
file.close()

name = input("Please, pick a name from the list above: ")
file = open('Names.txt', 'r')
list = file.read().split("\n")
list.remove(name)
names = "\n".join(str(i) for i in list)
file.close()

file = open('Names2.txt', 'w')
file.write(names)
file.close()

file = open('Names2.txt', 'r')
print(file.read())
