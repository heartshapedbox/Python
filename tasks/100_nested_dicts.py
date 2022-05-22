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

nested_dict = {}
step = 0
for i in range(0, len(data)):
    for i in range(0, len(data)):
        sub_dict = {}
        sub_dict[region[step]] = data[i][step]
        nested_dict[managers[i]] = sub_dict
    step += 1
    print(nested_dict)
