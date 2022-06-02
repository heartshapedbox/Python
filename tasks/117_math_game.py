# Создайте простую математическую игру, которая запрашивает у пользователя имя, а затем генерирует два случайных вопроса. Сохраните имя, введенные вопросы, ответы пользователя и итоговый
# счет в файле .csv. При каждом запуске программа должна добавлять информацию в файл .csv без
# перезаписи существующих данных.

import csv
import random
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')
from datetime import datetime

name = input('Please, enter your name: ')
questions_quantity = random.randrange(2, 6)
header = ['Name','Points','Date']
start = 1
for i in range(0, 5):
    header.insert(start, f'Question {i + 1}')
    header.insert(start + 1, f'Answer {i + 1}')
    header.insert(start + 2, f'Result {i + 1}')
    start += 3
print(f'{name}, answer to {questions_quantity} math questions, please.')


with open('math.csv', 'a', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(header)


expressions_list = ['+', '-', '*', '/']

class Math:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def do(self, expression):
        if expression == "+":
            self.x += self.y
        elif expression == "-":
            self.x -= self.y
        elif expression == "*":
            self.x *= self.y
        else:
            self.x /= self.y
        return round(self.x, 2)


count = 0
log_list = []
for i in range(0, questions_quantity):
    random_x = random.randrange(1, 10)
    random_y = random.randrange(1, 10)
    random_expression = random.choice(expressions_list)
    nums = Math(random_x, random_y)
    result = nums.do(random_expression)
    question = f"What is the result of {random_x} {random_expression} {random_y}?"
    print(f'\n{question}')
    log_list.append(question)
    answer = input("Your answer is: ")
    log_list.append(answer)

    try:
        answer = int(answer)
    except ValueError:
        try:
            answer = float(answer)
        except:
            print('Error!')

    if answer == result:
        print(f"[+] Correct! The result is: {result}.\n+1 point.")
        positive = True
        count += 1
    else:
        print(f"[-] Incorrect! The result is: {result}.")
        positive = False
        count += 0
    log_list.append(positive)
print(f'\nYou got {count} points.')


log_list.insert(0, name)

none = 3 * (5 - questions_quantity)
for i in range(0, none):
    log_list.append(None)

log_list.append(count)

now = datetime.now()
now_string = now.strftime("%d/%m/%Y %H:%M:%S")
log_list.append(now)


with open('math.csv', 'a') as file:
    writer = csv.writer(file)
    writer.writerow(log_list)
