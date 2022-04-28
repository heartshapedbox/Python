# Предложите пользователю
# ввести его возраст. Если
# введенное значение равно
# 18 и более, выведите сообщение «You can vote»; если
# 17 — сообщение «You can
# learn to drive»; если 16 —
# сообщение «You can buy a
# lottery ticket». Если значение
# меньше 16, выведите сообщение «You can go Trickor-Treating».

age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote!")
elif age == 17:
    print("You can learn to drive!")
elif age == 16:
    print("You can buy a lottery ticket!")
else:
    print("You can go Trick-or-Treating")
