# Создайте список с названиями двух видов
# спорта. Предложите пользователю ввести
# свой любимый вид спорта и добавьте его
# в конец списка. Отсортируйте список и выведите его.

sports = ["Football","Basketball"]
prompt = input("What is your favourite sport? ").title()
sports.append(prompt)
sports.sort()
print(sports)
