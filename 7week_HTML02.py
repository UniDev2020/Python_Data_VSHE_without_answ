#                                           Обработка Web страниц

from urllib.request import urlopen                                      #библиотека позволяющая получать страницы html
from bs4 import BeautifulSoup                                           #библиотека поиска в html файле
import ssl
import csv

'''
def getUrls(url):
    context = ssl._create_unverified_context()
    response = urlopen('https://en.wikipedia.org' + url, context=context)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    ourSet = set()

    for link in soup.find_all('a'):
        if link.has_attr('href'):                                          # проверка наличия атрибута
            s = link.get('href')                                           # достать по имени атрибута
            if s.startswith('/wiki/') and ':' not in s:                    # str начинается с /wiki
                ourSet.add(link.get('href'))
    return ourSet
allUnivs = list(getUrls('/wiki/Category:Universities_in_Moscow'))[:5]
linkUnivs = {}
for univ in allUnivs:
    linkUnivs[univ] = getUrls(univ)                                 #загружать в множество все ссылки с страницы univ
    print(univ, len(linkUnivs[univ]))                               #выводить ссылку на univ и кол-во страниц по ссылке
fout = open('univs.html', 'w', encoding='utf-8')
print('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table>
<tr>
''', file = fout)
allUnivs = sorted(allUnivs)

print('<td></td><td>', '</td><td>'.join(allUnivs), sep='\t', end='</td></tr>', file=fout) #вывод названию всех университетов через tab
for univ1 in allUnivs:
    print('<tr><td>', univ1[6:].replace('_', ' '), '</td>', file=fout)
    for univ2 in allUnivs:
        print('<td>', len(linkUnivs[univ1] & linkUnivs[univ2]), end='</td>', file=fout)         #два университета и кол-во общих статей
    print('</tr>', file=fout)        # на которые они ссылаются
print('''
</table>
</body>
</html>''', file=fout)'''
