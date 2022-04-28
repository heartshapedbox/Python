# Предложите пользователю ввести число, меньшее
# 20. Если введенное число
# больше или равно 20, выведите сообщение «Too high»;
# в противном случае выведите сообщение «Thank you».

num = int(input("Please, enter a number lower that 20: "))
if num >= 20:
    print("Too high!")
else:
    print("Thank you!")
