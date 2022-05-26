import csv
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\tasks')

men = ['Noah',"John","Henry",'James']
with open("persons.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(men)
file.close()

women = ['Anna','Sophia','Emma','Olivia']
with open("persons.csv", "a", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(women)
file.close()

with open('persons.csv', 'r', newline = "") as file:
    reader = csv.reader(file)
    for i in reader:
        print(', '.join(i))
file.close()

with open('persons.csv', 'r', newline = "") as file:
    reader = csv.reader(file)
    row = list(reader)
    print(row[1])
file.close()
