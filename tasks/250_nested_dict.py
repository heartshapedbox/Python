# Создайте следующий набор данных, представляющий
# объемы продаж по регионам, в виде двумерного словаря:
#          N    S    E    W
# John   3056 8463 8441 2694
# Tom    4832 6786 4737 3612
# Anna   5239 4802 5820 1859
# Fiona  3904 3645 8821 2451

managers = ['John','Tom','Anna','Fiona']
region = ['N','S','E','W']
data = [[3056,8463,8441,2694],[4832,6786,4737,3612],[5239,4802,5820,1859],[3904,3645,8821,2451]]

temp_dict1, temp_dict2, temp_dict3, temp_dict4 = {}, {}, {}, {}
dict1, dict2, dict3, dict4 = {}, {}, {}, {}
dict = {}
length = 4

for i in range(0, length):
    temp_dict1[region[i]] = data[0][i]
    dict1[managers[0]] = temp_dict1

for i in range(0, length):
    temp_dict2[region[i]] = data[1][i]
    dict2[managers[1]] = temp_dict2

for i in range(0, length):
    temp_dict3[region[i]] = data[2][i]
    dict3[managers[2]] = temp_dict3

for i in range(0, length):
    temp_dict4[region[i]] = data[3][i]
    dict4[managers[3]] = temp_dict4

for i in (dict1, dict2, dict3, dict4):
    dict.update(i)

print(dict)
