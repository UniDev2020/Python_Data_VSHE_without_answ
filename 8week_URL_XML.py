#                                                      URL --> XML
#                                                         -=1=-
'''from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import ssl
context = ssl._create_unverified_context()
#
cnt = 0
names = {}

#Москва
minLat = 55.5671                                                          # минимальная широта
minLon = 37.3611                                                          # минимальная долгота
maxLat = 55.9107                                                         # макс широта
maxLon = 37.8638                                                          # макс долгота

#                                            Скрипт нарезающий на квадраты
dlat = (maxLat - minLat)/100                                  # разница на 100
dlon = (maxLon - minLon)/100
for i in range(100):
    for j in range(100):
        nMinLat = minLat + dlat * i
        nMaxLat = minLat + dlat * (i+1)
        nMinLon = minLon + dlat * j
        nMaxLon = minLon + dlat * (j+1)

        # response = urlopen('https://www.openstreetmap.org/api/0.6/map?bbox=' + str(nMinLon)+'%2C'+ str(nMinLat) +'%2C' + str(nMaxLon) + '%2C' + str(nMaxLat), context=context)
        # xml = response.read().decode('utf-8')
        url = 'https://www.openstreetmap.org/api/0.6/map?bbox=' + str(nMinLon)+'%2C'+ str(nMinLat) +'%2C' + str(nMaxLon) + '%2C' + str(nMaxLat)

        urlretrieve(url, 'osm/map.osm')

        xml = open('osm/map.osm', 'r', encoding='utf-8')
        soup = BeautifulSoup(xml, 'lxml')
        for node in soup.find_all('node'):
            flag = False
            name = 'NoneName'                                                             #пустое имя supermarketa
            for tag in node('tag'):
                if tag['k'] == 'shop' and tag['v'] == 'supermarket':              #если найден supermaret
                    flag = True
                    cnt += 1
                if tag['k'] == 'name':                                            #сохраняем его имя
                    name = tag['v']
                if flag:
                    if name not in names:
                        names[name] = 0
                    names[name] += 1
        supermarkets = list(names.items())
        supermarkets.sort(key=lambda x: (x[-1], x[0]))
        print('Sector:', i,j)
        for market in supermarkets:
            print(*market)'''

#                                                         -=2=-
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import math

def dist(coord1, coord2):
    dlat = abs(coord1[0] - coord2[0])
    dlon = abs(coord1[1] - coord2[1])
    d = math.sqrt((dlat * 111.11) ** 2 + (dlon * 111.11 * math.sin(coord1[0] / 180 * math.pi)) ** 2)
    return d

cnt = 0

#Москва
minLat = 55.5671                                                          # минимальная широта
minLon = 37.3611                                                          # минимальная долгота
maxLat = 55.9107                                                         # макс широта
maxLon = 37.8638                                                          # макс долгота

#                                            Скрипт нарезающий на квадраты
dlat = (maxLat - minLat)/100                                  # разница на 100
dlon = (maxLon - minLon)/100
for i in range(100):
    for j in range(100):
        roads = {}
        nMinLat = minLat + dlat * i
        nMaxLat = minLat + dlat * (i+1)
        nMinLon = minLon + dlat * j
        nMaxLon = minLon + dlat * (j+1)

        # response = urlopen('https://www.openstreetmap.org/api/0.6/map?bbox=' + str(nMinLon)+'%2C'+ str(nMinLat) +'%2C' + str(nMaxLon) + '%2C' + str(nMaxLat), context=context)
        # xml = response.read().decode('utf-8')
        url = 'https://www.openstreetmap.org/api/0.6/map?bbox=' + str(nMinLon)+'%2C'+ str(nMinLat) +'%2C' + str(nMaxLon) + '%2C' + str(nMaxLat)

        urlretrieve(url, 'osm/map.osm')

        xml = open('osm/map.osm', 'r', encoding='utf-8')
        soup = BeautifulSoup(xml, 'lxml')
        nodes ={}

        for node in soup.find_all('node'):
            lat = float(node['lat'])
            lon = float(node['lon'])
            id = int(node['id'])
            nodes[id] = (lat, lon)
        flag = False
        for way in soup.find_all('way'):
            for tag in way('tag'):
                if tag['k'] == 'highway':              #если найден supermaret
                    rtype = tag['v']
                    flag = True
            if flag:
                rnodes = []
                for nd in way('nd'):
                    ref = int(nd['ref'])
                    rnodes.append(ref)
                for k in range(len(rnodes) -1):
                    coord1 = nodes[rnodes[k]]
                    coord2 = nodes[rnodes[k+1]]
                    if rtype not in roads:
                        roads[rtype] = 0                                               # суммарная длина дорог
                    roads[rtype] += dist(coord1, coord2)
        print('Sector', i, j)
        for now in roads:
            print(now, roads[now])
'''
#