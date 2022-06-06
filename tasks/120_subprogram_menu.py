# Отобразите для пользователя следующее меню:
# 1) Addition
# 2) Subtraction
# 3) Multiplication
# 5) Division
# Если пользователь выбирает 1 или 3, запускается подпрограмма, генерирующая два случайных числа из диапазона между 5 и 20. Рассчитайте правильный ответ и выведите его для пользователя вместе с его ответом. Если он выбирает 2 или 4, должна запускаться подпрограмма, генерирующая случайное число между 25 и 50, а затем еще одно между 1 и 25. Выведите правильный ответ вместе с ответом пользователя. Создайте еще одну подпрограмму, которая будет проверять совпадение ответа пользователя с правильным ответом. Если ответы совпали, выведите сообщение «Correct»; в противном случае выведите «Incorrect, the answer is» и правильный ответ. Если пользователь ввел некорректное значение в самом первом меню, выведите соответствующее сообщение.

import csv
import random
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')
from datetime import datetime

header = ['Expression','User answer','Correct answer','Result','Date']
with open('log.csv', 'a', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)


log_list = []
def log(*args):
    for i in args:
        log_list.append(i)
    return log_list


def get_random_nums():
    if option == 1 or option == 3:
        random_num1 = random.randrange(5, 20)
        random_num2 = random.randrange(5, 20)
    elif option == 2 or option == 4:
        random_num1 = random.randrange(25, 50)
        random_num2 = random.randrange(1, 25)
    else:
        print('Error!')
    random_num_list = [random_num1,random_num2]
    return random_num_list


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('The result is correct!')
        condition = True
    else:
        print('The result is incorrect!')
        condition = False
    log(condition)


def get_date():
    now = datetime.now()
    now_string = now.strftime('%d/%m/%y %H:%M:%S')
    log(now_string)


print('Expressions:\n1. [+] Addition\n2. [-] Subtraction\n3. [*] Multiplication\n4. [/] Division')
option = int(input('\nEnter a number of the expression: '))


def process():
    random_num1 = get_random_nums()[0]
    random_num2 = get_random_nums()[1]
    if option == 1:
        print(f'What is the result of {random_num1} + {random_num2}? ')
        correct_answer = random_num1 + random_num2
        expression = f'{random_num1} + {random_num2}'
    elif option == 2:
        print(f'What is the result of {random_num1} - {random_num2}? ')
        correct_answer = random_num1 - random_num2
        expression = f'{random_num1} - {random_num2}'
    elif option == 3:
        print(f'What is the result of {random_num1} * {random_num2}? ')
        correct_answer = random_num1 * random_num2
        expression = f'{random_num1} * {random_num2}'
    elif option == 4:
        print(f'What is the result of {random_num1} / {random_num2}? ')
        correct_answer = random_num1 / random_num2
        expression = f'{random_num1} / {random_num2}'
    else:
        print('Error!')
    user_answer = int(input('Please, enter your answer: '))
    print(f'Your answer is: {user_answer}, Correct answer is: {correct_answer}')

    log(expression,user_answer,correct_answer)
    check_answer(user_answer, correct_answer)
    get_date()


def main():
    process()
    with open('log.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(log_list)
main()
