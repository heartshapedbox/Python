import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\xml\\parsing_xml3\\')
import xml.etree.ElementTree as ET

myfile = ET.parse('file.xml')
myroot = myfile.getroot()

books_list = []
for i in myroot.iter('book'):
    id = i.attrib['id']
    title = i.find('title').text
    author = i.find('author').text
    
    books_list.append(
        {
            id: f'{title}; by {author}'
        }
    )
    

print(books_list)``