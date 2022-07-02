import json
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\json\\parsing_json3')

with open('file.json', 'r') as file:
    data = json.load(file)


widget_dict = data['widget']


dicts_list = []
for i in widget_dict:
    try:
        dicts_list.append(widget_dict[i])
    except AttributeError:
        pass


keys = ''
values = ''
keys_list = []
values_list = []

for i in dicts_list:
    try:
        keys = i.keys()
        string = i.values()
        
        for i in keys:
            keys_list.append(i)
        
        for i in string:
            values_list.append(i)
    except AttributeError:
        pass


print(keys_list)
print(values_list)





    

