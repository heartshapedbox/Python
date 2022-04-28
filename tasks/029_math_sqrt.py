# Предложите пользователю ввести целое число больше 500. Вычислите квадратный корень из этого числа
# и выведите его с точностью до двух знаков в дробной
# части.

import math
num = int(input("Please, enter an integer higher than 500: "))
num = math.sqrt(num)
result = round(num, 2)
print(result)
