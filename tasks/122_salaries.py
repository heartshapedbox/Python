# Создайте следующее меню:
# 1) Add to file
# 2) View all records
# 3) Quit program
# Enter the number of your selection: Если пользователь выбрал вариант 1, данные должны добавляться в файл Salaries.csv, содержащий имена и зарплаты. Если пользователь выбрал вариант 2, программа выводит все записи из файла Salaries.csv. Если пользователь выбрал вариант 3, программа завершается. Если выбран несуществующий вариант, выводится сообщение об ошибке. Пользователь снова и снова возвращается к меню, пока не будет выбран вариант 3.

import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

header = ['Name','Salary']
with open('Salaries.csv','w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)


def show_menu():
    print('\nMenu:\n--------------------\n1. Add to file\n2. View all records\n3. Quit\n--------------------\n')


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


def do(option):
    try:
        option = int(option)
        if option == 1:
            name = input('\nEnter your name: ').title()
            salary = input('Enter your salary in $: ')
            salary = '$' + salary
            data_list = [name,salary]
            print('\nOutput: Done!')
            add_data(data_list)
        elif option == 2:
            print('\nOutput:')
            read_data()
        elif option == 3:
            print('\nProgram closed.')
            quit()
        else:
            print('Error!')
    except ValueError:
        print('Error!')


def main():
    condition = True
    while condition == True:
        show_menu()
        option = input('Choose an option: ')
        do(option)
main()
