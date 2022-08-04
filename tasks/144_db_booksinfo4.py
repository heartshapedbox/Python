# Используя базу данных BookInfo из программы 141, предложите пользователю ввести имя автора. Сохраните все книги этого автора в текстовом файле; поля должны разделяться дефисами, так что выводимая информация должна выглядеть примерно так:
# 5 - Murder on the Orient Express - Agatha Christie - 1934
# 8 - The murder on the links - Agatha Christie - 1923
# 10 - The secret adversary - Agatha Christie - 1921
# 11 - The seven dials mystery - Agatha Christie - 1929

import sqlite3
import os
os.chdir('C:\\Users\\baben\\Documents\\DB\\')

db = sqlite3.connect('BookInfo.db')
cursor = db.cursor()

required_author_name = input('Enter an author name: ')

if ' ' in required_author_name:
    cursor.execute("""SELECT * FROM Books WHERE Author = ? ORDER BY DatePublished""", [required_author_name])
    for i in cursor.fetchall():
        print(i)
        db.commit()
else:    
    cursor.execute(f"""SELECT * FROM Books WHERE Author LIKE '%{required_author_name}%' ORDER BY DatePublished""")
    for i in cursor.fetchall():
        print(i)
        db.commit()   
db.close()