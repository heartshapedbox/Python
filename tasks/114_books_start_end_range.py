# Используя файл Books.csv, предложите пользователю ввести начальный и конечный год.
# Выведите все книги, выпущенные в заданном
# промежутке времени

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

start_year = input("Please, enter a year for the start: ")
end_year = input("Please, enter a year for the end: ")
tmp_list = []

with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    for i in reader:
        if i[2] > start_year and i[2] < end_year:
            string = ", ".join(str(y) for y in i)
            tmp_list.append(string)
    if len(tmp_list) == 0:
        print(f"No books from the period of {start_year} to {end_year}.")
    else:
        book_list = "\n".join(str(i) for i in tmp_list)
        print(f"Books from the period of {start_year} to {end_year}:\n{book_list}")
