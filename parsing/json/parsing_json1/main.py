import json
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\json\\parsing_json1')

with open('file.json') as file:
    data = json.load(file)

data_list = data['books']
book_list = []
for value in data_list:
    book_list.append(f"{value['title']}, {value['author']}, {value['year']}")

print(book_list)