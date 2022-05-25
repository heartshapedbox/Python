# Создайте следующий набор данных, представляющий
# объемы продаж по регионам, в виде двумерного словаря:
#          N    S    E    W
# John   3056 8463 8441 2694
# Tom    4832 6786 4737 3612
# Anna   5239 4802 5820 1859
# Fiona  3904 3645 8821 2451

class Table():
    def __init__(self, managers, region, values):
        self.name = managers
        self.reg = region
        self.val = values

    def get_dict(self):
        length = len(self.val)
        temp_dict1, temp_dict2, temp_dict3, temp_dict4 = {}, {}, {}, {}
        dict1, dict2, dict3, dict4 = {}, {}, {}, {}
        dict = {}

        step = 0
        for i in range(0, length):
            temp_dict1[self.reg[i]] = self.val[step][i]
            dict1[self.name[step]] = temp_dict1
            step += 1

            temp_dict2[self.reg[i]] = self.val[step][i]
            dict2[self.name[step]] = temp_dict2
            step += 1

            temp_dict3[self.reg[i]] = self.val[step][i]
            dict3[self.name[step]] = temp_dict3
            step += 1

            temp_dict4[self.reg[i]] = self.val[step][i]
            dict4[self.name[step]] = temp_dict4
            step = 0

        for i in (dict1, dict2, dict3, dict4):
            dict.update(i)
        print(dict)

data = Table(['John','Tom','Anna','Fiona'], ['N','S','E','W'], [[3056,8463,8441,2694],[4832,6786,4737,3612],[5239,4802,5820,1859],[3904,3645,8821,2451]])
data.get_dict()
