# Создайте массив из пяти чисел от 10 до 100,
# каждое из которых содержит два знака в дробной части. Предложите пользователю ввести
# целое число от 2 до 5. Если пользователь введет
# значение, выходящее за границы диапазона, выведите сообщение об ошибке и предложите выбрать снова, пока не будет введено допустимое
# значение. Разделите каждое из чисел в массиве
# на число, введенное пользователем, и выведите
# ответы с точностью до двух знаков.

from array import *
import random
import math

nums_array = array ('f', [])

while len(nums_array) != 5:
    random_num = random.random() * 100
    if random_num > 10 and random_num < 100:
        nums_array.append(random_num)
print(", ".join(str(i) for i in nums_array))

correct = False
while correct == False:
    num = int(input('Please, enter a number from 2 to 5: '))
    if num > 2 and num < 5:
        for i in nums_array:
            result = i / num
            print(f'{i} / {num} = rounded {round(result,2)}')
        correct = True
    else:
        print('Your number is out of range.')
        correct = False
