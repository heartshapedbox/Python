# Предложите пользователю ввести число. Продолжайте запрашивать число, пока введенное
# число не будет больше 5, после
# чего выведите сообщение «The
# last number you entered was a
# [число]» и остановите программу.

num = 0
while num <= 5:
    num = int(input("Please, enter some number: "))
    print(f"The last number you entered was a {num}.")
