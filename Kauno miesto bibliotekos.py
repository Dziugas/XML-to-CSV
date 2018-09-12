import xml.etree.ElementTree as ET
import csv

outputFile = open('Kauno miesto bibliotekos.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

row_names = ['id', 'padalinys', 'x', 'y', 'vadovas', 'adresas', 'telefonas', 'el. paštas', 'darbo laikas', 'darbo laikas vasarą']
#
outputWriter.writerow(row_names)

with open('Kauno miesto bibliotekos.xml', 'r', encoding='utf-8') as xml_file:
    tree = ET.parse(xml_file)
print(tree)
root = tree.getroot()

empty_list = []
full_list = []

markers = root.findall('marker')
for object in markers:
    id = object.find('id').text
    print(id)
    empty_list.append(id)

    title = object.find('title').text
    print(title)
    empty_list.append(title)

    coord_x = object.find('coord_x').text
    print(coord_x)
    empty_list.append(coord_x)

    coord_y = object.find('coord_y').text
    print(coord_y)
    empty_list.append(coord_y)

    description = object.find('description')
    p = description.find('p')
    p = ";".join(p.itertext())
    descriptions = p.split(';')
    desc_new = [item.replace('Vedėja ', '') for item in descriptions]
    print(desc_new)

    full_list = empty_list+desc_new

    outputWriter.writerow(full_list)
    empty_list = []

outputFile.close()

