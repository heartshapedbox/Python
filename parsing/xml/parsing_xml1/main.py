import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\python\\parsing\\xml\\')
import xml.etree.ElementTree as ET

myfile = ET.parse('file.xml')
myroot = myfile.getroot()

for i in myroot.iter('food'):
    element = ET.Element('delivery')
    i.append(element)
    description = 'Yes'
    element.text = str(description)

ET.indent(myroot, space = '     ')
myfile.write('updated_file.xml')



    