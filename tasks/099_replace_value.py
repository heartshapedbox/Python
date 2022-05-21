# Создайте двумерный список
# со стандартными индексами Python:
# Предложите пользователю выбрать строку и выведите только ее. Предложите выбрать столбец из выведенной строки и выведите только хранящееся там значение.
# Спросите, хочет ли пользователь изменить
# его. Если ответ будет положительным,
# предложите ввести новое значение и измените данные. Наконец, снова выведите
# измененную строку

import random

list = []
for i in range(0, 4):
    random_list = [random.randrange(1, 10) for i in range(0, 3)]
    list.append(random_list)
print(list)

row = int(input("Please, pick a row: "))
print(list[row])

column = int(input("Please, pick a column: "))
print(list[row][column])

prompt = input("Would you like to change the value? (y/n) ").lower()
if prompt == "y":
    new_value = int(input("Please, enter a new value: "))
    list[row][column] = new_value
    print(f"[+] The row has been changed: {list[row]}")
else:
    print(f"[-] The row hasn't been changed: {list[row]}")
