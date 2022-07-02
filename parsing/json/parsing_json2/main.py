import json
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\json\\parsing_json2')

with open('file.json', 'r') as file:
    data = json.load(file)
    
widget_dict = data['widget']

names = []
for i in widget_dict:
    try:
        names.append(widget_dict[i]['name'])
    except TypeError:
        pass

print(names)