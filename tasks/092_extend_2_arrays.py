# Создайте два массива:
# один будет содержать три
# числа, введенных пользователем, а другой — пять
# случайных чисел. Объедините эти два массива
# в один большой. Отсортируйте и выведите его, при
# этом каждое число должно
# выводиться в отдельной
# строке.

from array import *
import random

nums_array = array ('i', [])
random_nums_array = array ('i', [])

for i in range(0, 3):
    num = int(input("Please, enter a number: "))
    nums_array.append(num)

for i in range(0, 5):
    random_num = random.randint(0, 100)
    random_nums_array.append(random_num)

nums_array.extend(random_nums_array)
nums_array = sorted(nums_array)

for i in nums_array:
    print(i)
