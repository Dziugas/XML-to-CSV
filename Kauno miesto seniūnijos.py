import xml.etree.ElementTree as ET
import csv

outputFile = open('Kauno miesto seniūnijos.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

xml_tree = open('Kauno miesto seniūnijos.kml', 'r', encoding='utf-8')
tree = ET.parse(xml_tree)
root = tree.getroot()

klmns = '{http://www.opengis.net/kml/2.2}'

#prints out all tags to see the paths
for elemtn in root.iter():
    print(elemtn)

#looks for all elements with <name> tag
names = tree.findall('.//{http://www.opengis.net/kml/2.2}name')

#puts the text from all the <name> elements to the list
all_names = [name.text for name in names]

#recreates the list withour the first 2 instances which are broader categories we don't need
seniuniju_pav = []
for name in all_names[2:]:
    seniuniju_pav.append(name)
# print(seniuniju_pav)

#looks for all elements with <coordinates> tag
coords = tree.findall('.//{http://www.opengis.net/kml/2.2}coordinates')
#puts the text from all the <coordinates> elements to the list
coordinates = [coord.text for coord in coords]
# for c in coordinates:
#     print(c)

#zip two lists
bendras = dict(zip(seniuniju_pav, coordinates))
# print(bendras)

empty_list = []
for sen, coo in bendras.items():
    # print (sen, coo)
    empty_list.append(sen)
    empty_list.append(coo)
    print(empty_list)
    outputWriter.writerow(empty_list)
    empty_list=[]

outputFile.close()
