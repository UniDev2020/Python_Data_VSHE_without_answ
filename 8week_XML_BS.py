#                                               XML
'''from bs4 import BeautifulSoup

cnt=0
names = {}

xml = open('map.osm', 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'lxml')
# print(soup)
for node in soup.find_all('node'):
    flag = False
    name = ''                                                             #пустое имя supermarketa
    # print(node)
    for tag in node('tag'):
        # print(tag)
        if tag['k'] == 'shop' and tag['v'] == 'supermarket':              #если найден supermaret
            flag = True
            cnt += 1
        if tag['k'] == 'name':                                            #сохраняем его имя
            name = tag['v']
        if flag:
            if name not in names:
                names[name] = 0
            names[name] += 1
# print(names)
supermarkets = list(names.items())
supermarkets.sort(key=lambda x: (x[-1], x[0]))
# print(supermarkets)
for market in supermarkets:
    print(*market)'''
