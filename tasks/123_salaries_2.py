# Создайте следующее меню:
# 1) Add to file
# 2) View all records
# 3) Delete a record
# 4) Quit program
# Enter the number of your selection: Если пользователь выбрал вариант 1, данные должны добавляться в файл Salaries.csv, содержащий имена и зарплаты. Если пользователь выбрал вариант 2, программа выводит все записи из файла Salaries.csv. Если пользователь выбрал вариант 3, программа удаляет запить из Salaries.csv. Если пользователь выбрал вариант 4, программа завершается. Если выбран несуществующий вариант, выводится сообщение об ошибке. Пользователь снова и снова возвращается к меню, пока не будет выбран вариант 3.

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

header = ['Name','Salary']
with open('Salaries.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)


def show_menu():
    print('\nMenu:\n--------------------\n1. Add a record\n2. View all records\n3. Delete a record\n4. Quit\n--------------------')


def add_data(data_list):
    with open('Salaries.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(data_list)


def read_data():
    with open('Salaries.csv', 'r', newline = '') as file:
        reader = csv.reader(file)
        row = list(reader)
        for i in range(1, len(row)):
            print(': '.join(row[i]))


def remove_data(name):
    with open('Salaries.csv', 'r', newline = '') as file:
        reader = csv.reader(file)
        row = list(reader)
        tmp_list = [i for i in row]
        for i in tmp_list:
            if name in i:
                tmp_list.remove(i)

    with open('Salaries.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        for i in tmp_list:
            writer.writerow(i)


def check_name(name, option):
    if len(name) < 2:
        print('Error! Name is too short!')
        do(option)


def do(option):
    try:
        option = int(option)
        if option == 1:
            name = input('Please, enter a name: ').title()
            check_name(name, option)
            salary = '$' + input('Please, enter a salary in $: ')
            data_list = [name,salary]
            print('Output: Done!')
            add_data(data_list)
        elif option == 2:
            print('Output:')
            read_data()
        elif option == 3:
            read_data()
            name = input('Please, enter a name you would like to remove: ').title()
            check_name(name, option)
            print('Output: Done!')
            remove_data(name)
        elif option == 4:
            print('Program closed.')
            quit()
        else:
            print('Error! The number is out of menu range.')
    except ValueError:
        print('Error! You entered not a number.')


def main():
    condition = True
    while condition == True:
        show_menu()
        option = input('Please, choose an option: ')
        do(option)
main()
