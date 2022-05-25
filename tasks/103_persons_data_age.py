# Предложите пользователю ввести имя, возраст и размер обуви для четырех человек. Выведите имя и возраст для всех людей в списке, но не их размер обуви.

print('Please, provide data about 4 persons.')
dict = {}
for i in range(0, 4):
    print(f'{i + 1} person:')
    name = input("Please, enter a person's name: ").title()
    age = int(input("Please, enter a person's age: "))
    shoes_size = int(input("Please, enter a person's shoes size: "))
    dict[name] = {"Age": age, "Shoes Size": shoes_size}
print(f'Dictionary:\n {dict}')

for i in dict:
    print(i, dict[i]["Age"])
