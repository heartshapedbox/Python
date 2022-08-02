# Создайте базу данных SQL с именем BookInfo, предназначенную для хранения списка авторов и написанных ими книг. Она состоит из двух таблиц. Первая таблица с именем Authors содержит следующие данные:
# Name                Place of Birth
# Agatha Christie     Torquay
# Cecelia Ahern       Dublin
# J. K. Rowling       Bristol
# Oscar Wilde         Dublin

# Вторая таблица Books должна содержать следующие данные:
# ID     Title                                         Author                 Date Published
#  1     De Profundis                                  Oscar Wilde            1905
#  2     Harry Potter and the chamber of secrets       J. K. Rowling          1998
#  3     Harry Potter and the prisoner of Azkaban      J. K. Rowling          1999
#  4     Lyrebird                                      Cecelia Ahern          2017
#  5     Murder on the Orient Express                  Agatha Christie        1934
#  6     Perfect                                       Cecelia Ahern          2017
#  7     The marble collector                          Cecelia Ahern          2016
#  8     The murder on the links                       Agatha Christie        1923
#  9     The picture of Dorian Gray                    Oscar Wilde            1890
# 10     The secret adversary                          Agatha Christie        1921
# 11     The seven dials mystery                       Agatha Christie        1929
# 12     The year I met you                            Cecelia Ahern          2014

import sqlite3
import os
os.chdir('C:\\Users\\baben\\Documents\\DB\\')

db = sqlite3.connect('BookInfo.db')
cursor = db.cursor()

tables = ['Authors', 'Books']
header = ['ID', 'Name', 'PlaceOfBirth', '']
header2 = ['ID', 'Title', 'Athor', 'DatePublished']


for i in range(len(tables)):
    if tables[i] == 'Authors':
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tables[i]}(
        {header[0]} integer PRIMARY KEY,
        {header[1]} text NOT NULL,
        {header[2]} text NOT NULL
        )""")
    else:
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {tables[i]}(
        {header2[0]} integer PRIMARY KEY,
        {header2[1]} text NOT NULL,
        {header2[2]} text NOT NULL,
        {header2[3]} text NOT NULL
        )""")
db.commit()


authors_list = [('Agatha Christie', 'Torquay'), ('Cecelia Ahern', 'Dublin'), ('J. K. Rowling', 'Bristol'), ('Oscar Wilde', 'Dublin')]
for i in authors_list:
    cursor.execute("""INSERT INTO Authors(ID, Name, PlaceOfBirth) VALUES(?,?,?)""", (authors_list.index(i)+1, i[0], i[1]))
    db.commit()


books_list = [('De Profundis', 'Oscar Wilde', '1905'), ('Harry Potter and the chamber of secrets', 'J. K. Rowling', '1998'), ('Harry Potter and the prisoner of Azkaban', 'J. K. Rowling', '1999'), ('Lyrebird', 'Cecelia Ahern', '2017'), ('Murder on the Orient Express', 'Agatha Christie', '1934'), ('Perfect', 'Cecelia Ahern', '2017'), ('The marble collector', 'Cecelia Ahern', '2016'), ('The murder on the links', 'Agatha Christie', '1923'), ('The picture of Dorian Gray', 'Oscar Wilde', '1890'), ('The secret adversary', 'Agatha Christie', '1921'), ('The seven dials mystery', 'Agatha Christie', '1929'), ('The year I met you', 'Cecelia Ahern', '2014')]
for i in books_list:
    cursor.execute("""INSERT INTO Books(ID, Title, Athor, DatePublished) VALUES(?,?,?,?)""", (books_list.index(i)+1, i[0], i[1], i[2]))
    db.commit()
db.close()