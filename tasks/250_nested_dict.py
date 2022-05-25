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

length = len(data)
temp_dict1, temp_dict2, temp_dict3, temp_dict4 = {}, {}, {}, {}
dict1, dict2, dict3, dict4 = {}, {}, {}, {}
dict = {}
step = 0

for i in range(0, length):
    temp_dict1[region[i]] = data[step][i]
    dict1[managers[step]] = temp_dict1
    step += 1

    temp_dict2[region[i]] = data[step][i]
    dict2[managers[step]] = temp_dict2
    step += 1

    temp_dict3[region[i]] = data[step][i]
    dict3[managers[step]] = temp_dict3
    step += 1

    temp_dict4[region[i]] = data[step][i]
    dict4[managers[step]] = temp_dict4
    step = 0

for i in (dict1, dict2, dict3, dict4):
    dict.update(i)
print(dict)
