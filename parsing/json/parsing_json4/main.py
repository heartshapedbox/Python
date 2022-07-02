import json
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\json\\parsing_json4\\')

with open('file.json', 'r') as file:
    data = json.load(file)


menu_keys = data.values()
menu_values = ''
for i in menu_keys:
    menu_values = i.values()


menuitems_values = ''
for i in menu_values:
    try:
        menuitems_values = i.values()
    except AttributeError:
        pass


for i in menuitems_values:
    menuitems_list = i


functions_list = []
for i in menuitems_list:
    functions_list.append(i['onclick'])


print(functions_list)