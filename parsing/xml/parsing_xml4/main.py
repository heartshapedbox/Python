from xml.dom import minidom
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\xml\\parsing_xml4\\')

data = minidom.parse('file.xml')
parents = data.getElementsByTagName('book')
titles = data.getElementsByTagName('title')
authors = data.getElementsByTagName('author')

parents_list, titles_list, authors_list = [], [], []

for i in range(0, len(parents)):
    parents_list.append(parents[i].attributes['id'].value)
    titles_list.append(titles[i].firstChild.data)
    authors_list.append(authors[i].firstChild.data)
    

list = []
for i in range(0, len(parents_list)):
    list.append(
        {
            parents_list[i]: f'{titles_list[i]}; by {authors_list[i]}'
        }
    )

print(list)
