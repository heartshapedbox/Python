import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\xml\\parsing_xml2\\')
import xml.etree.ElementTree as ET

myfile = ET.parse('file.xml')
myroot = myfile.getroot()

food_list = []
for i in myroot.iter('food'):
    item = i.find('item').text
    price = i.find('price').text
    
    food_list.append(
        {
            item: price
        }
    )


print(food_list)