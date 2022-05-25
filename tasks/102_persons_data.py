# Предложите пользователю ввести имя, возраст и размер обуви для четырех человек. Запросите имя одного из них в списке и выведите значения его возраста и размера обуви.

print('Please, provide data about 4 persons.')
dict = {}
for i in range(0, 4):
    print(f'{i + 1} person:')
    name = input("Please, enter a person's name: ").title()
    age = int(input("Please, enter a person's age: "))
    shoes_size = int(input("Please, enter a person's shoes size: "))
    dict[name] = {"Age": age, "Shoes Size": shoes_size}
print(f'Dictionary:\n {dict}')

name = input("\nPlease, pick a name from the dictionary: ")
print(f"{name}'s data:\n {dict[name]}")
