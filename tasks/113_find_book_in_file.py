# Используя файл Books.csv, спросите пользователя, сколько записей он хочет добавить в список, и предоставьте ему такую возможность. После того как данные будут добавлены, запросите автора и выведите все книги указанного автора из списка. Если в списке нет ни одной книги
# этого автора, выведите соответствующее сообщение.

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

books = int(input('How many books would you like to add to the file? '))
for i in range(0, books):
    book = input("Please, enter a book title, its author and publishing year using ',': ")
    book = book.split(',')
    striped_book = []
    for i in book:
        striped_book.append(i.lstrip().rstrip())
    with open('books.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(striped_book)

author = input('Please, enter some author: ').title()
striped_author = author.rstrip().lstrip()
with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    author_books_list = []
    for row in reader:
        if row[1] == striped_author:
            author_books_list.append(row)
    if len(author_books_list) > 0:
        author_books = '\n'.join(str(i) for i in author_books_list)
        print(f"{author}'s books:\n{author_books}")
    else:
        print("Sorry! There are no books by this author in the file!")
