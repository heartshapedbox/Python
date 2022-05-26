import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

data = '123'
with open('data.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(data)
file.close()

data2 = '456'
with open('data.csv', 'a', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(data2)
file.close()

with open('data.csv', 'r', newline = '') as file:
    reader = csv.reader(file)
    for i in reader:
        print(list(i))
