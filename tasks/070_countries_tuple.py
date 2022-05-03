# Создайте кортеж с названиями пяти стран. Выведите все содержимое кортежа. Предложите
# поользователю
# ввести число и выведите название
# страны, находящейся в заданной
# позиции.

countries = ("USA","Ukraine","Poland","France","German")
print(countries)

prompt = int(input("Please, enter a number from 1 to 5: "))
print(countries[prompt - 1])
