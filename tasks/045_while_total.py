# Присвойте total значение 0. Пока значение total равно
# 50 или менее, предложите пользователю ввести число. Прибавьте это число к total и выведите сообщение «The total
# is… [total]». Цикл должен остановиться, когда значение total
# превысит 50.

total = 0
while total <= 50:
    num = int(input("Please, enter some number: "))
    total += num
    print(f"The total is {total}.")
