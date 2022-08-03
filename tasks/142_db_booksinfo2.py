# Используя базу данных BookInfo из программы 141, выведите список авторов с местами рождений. Предложите пользователю ввести место рождения, а затем выведите название, дату издания и имя автора для всех книг авторов, родившихся в указанном месте.

import sqlite3
import os
os.chdir('C:\\Users\\baben\\Documents\\DB')

db = sqlite3.connect('BookInfo.db')
cursor = db.cursor()
cursor.execute('SELECT * FROM Authors')
for i in cursor.fetchall():
    print(f'[+] {i}')
    
place_of_birth = input('Enter a place of birth: ').title()

cursor.execute("""SELECT Books.Title, Books.Author, Books.DatePublished, Authors.PlaceOfBirth
FROM Books, Authors
WHERE Authors.Name = Books.Author AND Authors.PlaceOfBirth = ?""", [place_of_birth])
for i in cursor.fetchall():
    print(i)