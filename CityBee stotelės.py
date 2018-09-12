import xml.etree.ElementTree as ET
import csv

outputFile = open('CityBee stotelės.csv', 'w', newline='', encoding='utf-8')
outputWriter = csv.writer(outputFile)

xml_tree = open('CityBee stotelės.kml', 'r', encoding='utf-8')
tree = ET.parse(xml_tree)
root = tree.getroot()

klmns = '{http://www.opengis.net/kml/2.2}'

#prints out all tags to see the paths
for elemtn in root.iter():
    print(elemtn)

places = tree.findall('.//{http://www.opengis.net/kml/2.2}Placemark')

empty_list = []
for place in places:
    name = place.find('.//{http://www.opengis.net/kml/2.2}name')
    pavadinimas = name.text
    print(pavadinimas)
    empty_list.append(pavadinimas)

    coordinate = place.find('.//{http://www.opengis.net/kml/2.2}coordinates')
    koordinates = coordinate.text
    print(koordinates)
    empty_list.append(koordinates)

    if place.find('.//{http://www.opengis.net/kml/2.2}description') is not None:
        description_raw = place.find('.//{http://www.opengis.net/kml/2.2}description')
        description = description_raw.text
        print(description)
        empty_list.append(description)
    else:
        pass

    styleUrl = place.find('.//{http://www.opengis.net/kml/2.2}styleUrl')
    kodas = styleUrl.text
    print(kodas)
    empty_list.append(kodas)

    outputWriter.writerow(empty_list)
    empty_list = []

outputFile.close()

