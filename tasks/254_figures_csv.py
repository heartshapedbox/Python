import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

figs = 'triangle, square, circle'
with open('figures.csv', 'w', newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(figs)

with open('figures.csv', 'r', newline = "") as file:
    reader = csv.reader(file)
    for i in reader:
        print(''.join(i))

with open('new_figures.csv', 'w', newline = "") as file:
    new_figs = figs.split(",")
    writer = csv.writer(file)
    writer.writerow(new_figs)

with open('new_figures.csv', 'r', newline = "") as file:
    reader = csv.reader(file)
    for i in reader:
        print(','.join(i))
