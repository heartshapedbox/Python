# Используя базу данных BookInfo из программы 141, предложите пользователю ввести год. Выведите все книги, изданные после этого года; список должен быть упорядочен по году издания.

import sqlite3
import os
os.chdir('C:\\Users\\baben\\Documents\\DB\\')

requested_year = int(input('Enter a year: '))

db = sqlite3.connect('BookInfo.db')
cursor = db.cursor()
cursor.execute("""SELECT * FROM Books WHERE DatePublished > ? ORDER BY DatePublished""", [requested_year])
for i in cursor.fetchall():
    print(i)