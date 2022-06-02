# Определите подпрограмму, которая предлагает пользователю выбрать большое и маленькое число, а затем генерирует случайное число из этого диапазона и сохраняет его в переменной с именем comp_num. Определите другую подпрограмму, которая выводит сообщение «I am thinking of a number…», после чего предлагает пользователю угадать загаданное число. Определите третью подпрограмму, которая проверяет, совпадает ли comp_num с предположением пользователя. Если совпадает, то подпрограмма выводит сообщение «Correct, you win»; в противном случае цикл продолжается, а подпрограмма сообщает, больше или меньше их предположение загаданного числа, и предлагает сделать новую попытку до тех пор, пока пользователь его не угадает.

import csv
import random
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\python\\tasks')
from datetime import datetime

header = ['Min. number','Max. number','Random number from the range','Tries','Date']
with open('guess_number_log.csv', 'a', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)

log_list = []
def log(*args):
    for i in args:
        log_list.append(i)
    return log_list

def get_range():
    min_num = int(input('Please, enter a number as a minimum value: '))
    max_num = int(input('Please, enter a number as a maximum value: '))
    comp_num = random.randrange(min_num, max_num)
    log(min_num, max_num, comp_num)
    return comp_num

def guess():
    print("I've picked a nubmer.")
    guess_num = int(input('Guess the number: '))
    return guess_num

def check(comp_num, guess_num):
    count = 0
    condition = False
    while condition == False:
        if guess_num == comp_num:
            print(f'Correct! You win! The number is {comp_num}.')
            condition = True
        elif guess_num > comp_num:
            print('Incorrect! Your number is higher. Try again!')
            guess_num = int(input('Guess the number: '))
        else:
            print('Incorrect! Your number is lower. Try again!')
            guess_num = int(input('Guess the number: '))
        count += 1
    log(count)

def get_date():
    now = datetime.now()
    now_string = now.strftime('%d/%m/%y %H:%M:%S')
    log(now_string)

def main():
    comp_num = get_range()
    guess_num = guess()
    check(comp_num, guess_num)
    get_date()
    with open('guess_number_log.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(log_list)
main()
