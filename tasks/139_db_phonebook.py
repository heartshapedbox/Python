# Создайте базу данных SQL с именем PhoneBook. База данных должна содержать таблицу Names со следующими данными:
# ID    First Name     Surname       Phone Number
# 1     Simon           Howeis        01223 349752
# 2     Karen           Phillips      01954 295773
# 3     Darren          Smith         01583 749012
# 4     Anne            Jones         01323 567322
# 5     Mark            Smith         01223 855534

import sqlite3
import os
os.chdir('C:\\Users\\baben\\Documents\\DB')

db = sqlite3.connect('PhoneBook.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Names(
    ID integer PRIMARY KEY,
    FirstName text NOT NULL,
    Surname text NOT NULL,
    PhoneNumber text NOT NULL
)""")
db.commit()


list = [('Simon', 'Howeis', '01223 349752'), ('Karen', 'Phillips', '01954 295773'), ('Darren', 'Smith', '01583 749012'), ('Anne', 'Jones', '01323 567322'), ('Mark', 'Smith', '01223 855534')]


for i in list:
    cursor.execute("""INSERT INTO Names('ID', 'FirstName', 'Surname', 'PhoneNumber') VALUES(?,?,?,?)""", (list.index(i) + 1, i[0], i[1], i[2]))
    db.commit()

db.close()

