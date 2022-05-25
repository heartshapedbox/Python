# Предложите пользователю ввести имя, возраст и размер обуви для четырех человек. Запросите у пользователя имя человека для удаления из списка. Удалите
# эту строку и выведите остальные данные с разбивкой по строкам.

print('Please, provide data about 4 persons.')
dict = {}
for i in range(0, 4):
    print(f"\n{i + 1} person's data:")
    name = input(f"Please, enter person's name: ").title()
    age = int(input(f"Please, enter person's age: "))
    shoes_size = int(input(f"Please, enter person's shoes size: "))
    dict[name] = {"Age": age, "Shoes size": shoes_size}
print(f'\nComplex persons data: {dict}')

prompt_name = input("\nPlease, pick a person for removing from the list: ").title()

del dict [prompt_name]
for i in dict:
    print(f'Name: {i}, Age: {dict[i]["Age"]}, Shoes size: {dict[i]["Shoes size"]}')
