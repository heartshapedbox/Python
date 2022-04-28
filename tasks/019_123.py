# Предложите пользователю ввести значение 1, 2 или 3. Если введено значение 1, выведите сообщение «Thank you»; если 2 — сообщение «Well done»; если 3 — сообщение «Correct». Если введено
# любое другое значение, выведите сообщение «Error message».

num = int(input("Please, enter 1, 2 or 3: "))
if num == 1:
    print("Thank you!")
elif num == 2:
    print("Well done!")
else:
    print("Error!")
