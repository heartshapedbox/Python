# Импортируйте данные из файла Books.csv в список. Выведите список, предложите пользователю выбрать, какую строку он хочет исключить, и удалите ее.
# Спросите пользователя, какие данные он хочет изменить, и предоставьте ему
# соответствующую возможность. Запишите данные обратно в файл .csv с заменой существующих.

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    tmp_list = list(reader)
    for i in range(1, len(tmp_list)):
        string = ', '.join(tmp_list[i])
        print(f'{i}. {string}')


row_number_to_remove = int(input('\nWhich row would you like to remove? '))
if row_number_to_remove > len(tmp_list):
    print('Error!')
else:
    del tmp_list[row_number_to_remove]
    for i in range(1, len(tmp_list)):
        string = ', '.join(tmp_list[i])
        print(f'{i}. {string}')


    row_number_to_change = int(input('\nWhich row would you like to change? '))
    if row_number_to_change >= len(tmp_list):
        print('Error!')
    else:
        row_list = tmp_list[row_number_to_change]
        for i in row_list:
            print(f'{row_list.index(i)}. {i}')


        data_number_to_change = int(input('\nWhich part of the row would you like to change? '))
        if data_number_to_change >= len(row_list):
            print('Error!')
        else:
            new_data = input("Please, enter new data: ")
            row_list[data_number_to_change] = new_data
            tmp_list[row_number_to_change] = row_list
            with open('books.csv', 'w', newline = '') as file:
                writer = csv.writer(file)
                for i in tmp_list:
                    writer.writerow(i)


with open('books.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    list = list(reader)
    for i in range(1, len(list)):
        sting = ', '.join(list[i])
        print(f'{i}. {sting}')
