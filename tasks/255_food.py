import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

food = ['Fruits','Vegetables','Dairy','Pastry']
with open('food.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(food)

food_dict = []
with open('food.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    for i in reader:
        tmp = i
    for i in tmp:
        food_dict.append({
            f"Food class {tmp.index(i) + 1}": i
        })

print(food_dict)

with open('new_food.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(food_dict)

with open('new_food.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    for i in reader:
        print(', '.join(i))
