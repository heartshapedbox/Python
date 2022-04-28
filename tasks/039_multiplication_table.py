# Предложите пользователю ввести число от 1
# до 12. Выведите таблицу умножения для этого
# числа.

num = int(input("Please, enter a number from 1 to 12: "))
for i in range(1, 10):
    print(f"{num} * {i} = {num * i}")
