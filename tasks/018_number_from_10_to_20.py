# Предложите пользователю ввести число. Если оно меньше 10, выведите сообщение «Too low»; если число лежит в диапазоне от 10
# до 20 — сообщение «Correct». В остальных случаях выведите сообщение «Too high».

num = int(input("Please, enter a number: "))
if num < 10:
    print("Too low!")
elif num > 10 and num < 20:
    print("Correct!")
else:
    print("Too high!")
