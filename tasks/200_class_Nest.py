# Создайте следующий набор данных, представляющий
# объемы продаж по регионам, в виде двумерного словаря:
#          N    S    E    W
# John   3056 8463 8441 2694
# Tom    4832 6786 4737 3612
# Anna   5239 4802 5820 1859
# Fiona  3904 3645 8821 2451

class Nest:
    def __init__ (self, managers_list, region, data):
        self.managers_list = managers_list
        self.region = region
        self.data = data

    def get_nested_list(self):
        nested_dict = {}
        step = 0
        for i in range(0, len(self.data)):
            for i in range(0, len(self.data)):
                sub_dict = {}
                sub_dict[self.region[step]] = self.data[i][step]
                nested_dict[self.managers_list[i]] = sub_dict
            step += 1
            print(nested_dict)

dict1 = Nest(['John','Tom','Anna','Fiona'],['N','S','E','W'],[[3056,8463,8441,2694],[4832,6786,4737,3612],[5239,4802,5820,1859],[3904,3645,8821,2451]])
dict1.get_nested_list()

print("\n")

dict2 = Nest(['Mike','Jack','Steve','Jake'],['N','S','E','W'],[[1048,8578,5628,3245],[8945,2594,1243,5842],[9851,1346,7845,9584],[2145,1158,3985,4521]])
dict2.get_nested_list()
