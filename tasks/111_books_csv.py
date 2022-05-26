# Создайте файл .csv с данными, приведенными в следующей таблице. Назовите его Books.csv.
# Книга                                         Автор                   Год выпуска
# 0 To Kill a Mockingbird                       Harper Lee              1960
# 1 A Brief History of Time                     Stephen Hawking         1988
# 2 The Great Gatsby                            F. Scott Fitzgerald     1922
# 3 The Man Who Mistook His Wife for a Hat      Oliver Sacks            1985
# 4 Pride and Prejudice                         Jan Austen              1813

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

header = ['Book','Author','Publishing Year']
books_list = [['To Kill a Mockingbird','Harper Lee',1960],['A Brief History of Time','Stephen Hawking',1988],['The Great Gatsby','F. Scott Fitzgerald',1922],['The Man Who Mistook His Wife for a Hat','Oliver Sacks',1985],['Pride and Prejudice','Jan Austen',1813]]

with open('books.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for i in books_list:
        writer.writerow(i)

with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)
