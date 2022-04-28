# Предложите пользователю
# ввести два числа. Если первое
# число больше второго, сначала выведите второе число,
# а потом первое. В противном
# случае выведите сначала первое число, а потом второе.

num1 = int(input("Hello! Enter a nubmer, please: "))
num2 = int(input("Enter another number, please: "))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)
