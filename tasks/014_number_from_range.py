# Предложите пользователю
# ввести число от 10 до 20 (включительно). Если будет введено
# число из этого диапазона, выведите сообщение «Thank you»;
# в противном случае выведите
# сообщение «Incorrect answer».

num = int(input("Please, enter a number from 10 to 20: "))
if num >= 10 and num <= 20:
    print("Thank you!")
else:
    print("Incorrect!")
