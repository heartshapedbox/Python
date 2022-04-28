# Предложите пользователю ввести два числа. Используйте целочисленное деление, чтобы разделить первое число на второе; вычислите остаток и выведите
# ответ в виде, удобном для пользователя (например,
# если пользователь ввел 7 и 2, выведите строку вида
# «если разделить 7 на 2, получится 3 с остатком 1»).

import math
num1 = int(input("Please, enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 // num2
leftover = num1 % num2
print(f"The result of division {num1} on {num2} is {result}. The leftover is {leftover}.")
