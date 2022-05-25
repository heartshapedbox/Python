# Откройте файл Names.txt. Предложите пользователю ввести новое имя. Добавьте его в конец файла и выведите все содержимое файла.

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

file = open('Names.txt', 'a')
name = input("Please, enter some name: ")
file.write(f'\n{name}')
file.close()

file = open('Names.txt', 'r')
print(file.read())
file.close()
