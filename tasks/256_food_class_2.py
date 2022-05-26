import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

food_list = ['Fruits','Vegetable','Pastry','Dairy']
header = ["Food class" for i in range(0, len(food_list))]

with open("food_class.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow(food_list)

with open('food_class.csv', 'r', newline = "") as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)
