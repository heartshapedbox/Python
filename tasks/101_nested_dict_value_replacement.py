# Создайте следующий набор данных, представляющий
# объемы продаж по регионам, в виде двумерного словаря:
#          N    S    E    W
# John    3056 8463 8441 2694
# Tom     4832 6786 4737 3612
# Anna    5239 4802 5820 1859
# Fiona   3904 3645 8821 2451
#
# Запросите у пользователя имя и регион. Выведите соответствующие данные. Запросите у пользователя имя и регион того значения, которое он хочет изменить, и позвольте скорректировать объем продаж. Выведите объемы продаж по всем регионам для имени, выбранного пользователем.

nested_dict = {
'John': {'N': 3056,'S': 8463,'E': 8441,'W': 2694},
'Tom': {'N': 4832,'S': 6786,'E': 4737,'W': 3612},
'Anna': {'N': 5239,'S': 4802,'E': 5820,'W': 1859},
'Fiona': {'N': 3904,'S': 3645,'E': 8821,'W': 2451}
}
print(nested_dict)

manager = input('\nPlease, enter a manager name: ').title()
region = input('Please, enter a region: ').upper()
print(f'Data from {manager} (Region {region}): {nested_dict[manager][region]}')

manager = input('\nPlease, enter a manager name you would like to correct data of: ').title()
region = input('Please, enter a region you would like to correct data of: ').title()
new_data = int(input("Please, enter a new data: "))

nested_dict[manager][region] = new_data
print(f'Data from {manager} by regions: {nested_dict[manager]}')
