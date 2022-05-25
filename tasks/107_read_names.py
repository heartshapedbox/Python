# Откройте файл Names.txt и выведите данные из кода Python.

import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

file = open('Names.txt', 'r')
print(file.read())
file.close()
