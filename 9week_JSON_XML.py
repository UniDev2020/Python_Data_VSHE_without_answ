#                                                    JSON
#                      read JSON from file
'''import json

fin = open('outage.json', 'r', encoding='utf-8')
text = fin.read()
lst = json.loads(text)
s = input()
# print(lst)
for row in lst:
    cells = row['Cells']
    addr = cells['Address']
    periods = cells['Periods']
    period = periods[0]
    begin = period['OutageBegin']
    end = period['OutageEnd']
    # print(addr, begin, end)
    if s in addr:
        print(addr, begin, end)'''

#                                    Parsing XML,            XMLtoDict
import xmltodict

fin = open('map.osm', 'r', encoding='utf-8')
dct = xmltodict.parse(fin.read())                                           #переводим xml to dict
# print(dct['osm']['node'][0])
for node in dct['osm']['node']:                                             #выводим все кооординаты
    # print(node['@lat'], node['@lon'])
    flag = False
    if 'tag' in node and isinstance(node['tag'], list):                     # и я вляется ли списком
        # print(node['tag'])
        for tag in node['tag']:
            if tag['@k'] == 'addr:street':
                street = tag['@v']
            if tag['@k'] == 'addr:housenumber':
                housenumber = tag['@v']
    if flag:
        print(street, housenumber, node['@lat'], node['@lon'])


