# Используя файл Books.csv, выведите данные
# с нумерацией строк.

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    tmp_list = list(reader)
    for i in range(1, len(tmp_list)):
        string = ", ".join(tmp_list[i])
        print(f'{i}) {string}')
