# Используя файл Books.csv из программы 111, предложите пользователю ввести новую запись и добавьте ее в конец файла. Выведите
# каждую строку файла .csv в отдельной строке

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

book = input("Please, enter some book name, its author and publishig year using ',': ")
with open('books.csv', 'a', newline = "") as file:
    book = book.split(",")
    striped_book = [str(i).lstrip().rstrip() for i in book]
    writer = csv.writer(file)
    writer.writerow(striped_book)

with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)
