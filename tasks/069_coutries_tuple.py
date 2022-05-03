# Создайте кортеж с названиями пяти стран. Выведите все содержимое кортежа. Предложите
# пользователю ввести название одной из этих стран и выведите индекс (то есть позицию в списке)
# этого элемента кортежа.

countries = ("Ukraine","USA","Gernamy","France","Poland")
print(countries)

prompt = input("Enter some country name from the list above: ")
if prompt in countries:
    print(countries.index(prompt) + 1)
