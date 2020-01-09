#                                  Загрузка и обработка Web страниц
from urllib.request import urlopen                                      #библиотека позволяющая получать страницы html
from bs4 import BeautifulSoup                                           #библиотека поиска в html файле
import ssl

context = ssl._create_unverified_context()
##1
'''
response = urlopen('https://en.wikipedia.org/wiki/Higher_School_of_Economics', context=context)
html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
exc = set(['/wiki/Wikipedia:Citation_needed','/wiki/File:','/wiki/Category:','/wiki/Special:', '/wiki/Help:',
           '/wiki/Portal:',
           '/wiki/Wikipedia'])    #множество искл из представления
for link in soup.find_all('a'):                                          # позволяет найти все теги на странице
    if link.has_attr('href'):                                            # проверяет есть ли такой атрибут у тега
        s = link.get('href')                                             # достать по имени атрибута
        if s.startswith('/wiki/'):                                       # str начинается с /wiki
            flag = True
            for line in exc:                                             # проверка на искл из множ-ва
                if s.startswith(line):
                    flag = False                                         # не печатать ссылку
            if flag:
                print(link.get('href'))
'''
##2

# response = urlopen('https://en.wikipedia.org/wiki/Higher_School_of_Economics', context=context)
# html = response.read().decode('utf-8')
# soup = BeautifulSoup(html, 'html.parser')
#
# for link in soup.find_all('a'):
#     if link.has_attr('href'):                                            # проверка наличия атрибута
#         s = link.get('href')                                             # достать по имени атрибута
#         if s.startswith('/wiki/') and ':' not in s:                      # str начинается с /wiki
#                 print(link.get('href'))
#
# file = open('week07_ex02.html', 'w')
# print('<html>', '<body>', '<table>', sep='\n', file=file)
# for i in range(1,11):
#     print('<tr>', end='', file=file)
#     for j in range(1, 11):
#         print('<td>', i * j, '</td>', sep='', end='', file=file)
#     print('</tr>', file=file)
# print('</table>', '</body>', '</html>', sep='\n', file=file)

##3

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
links = getUrls('/wiki/Higher_School_of_Economics')
links2 = getUrls('/wiki/Moscow_State_University')
print(len(links & links2))                                                 # поиск общих ссылок
for now in links:
    print(now)
    nowlinks = getUrls(now)
    print(len(nowlinks))
file = open('week07_ex03.html', 'w')
print('<html>', '<body>', '<table>', sep='\n', file=file)
for i in range(1,11):
    print('<tr>', end='', file=file)
    for j in range(1, 11):
        result = i * j
        input_row = '<a href=http://' + str(result) + '.ru>' + str(result) + '</a>'
        print('<td>', input_row, '</td>', sep='', end='', file=file)
    print('</tr>', file=file)
print('</table>', '</body>', '</html>', sep='\n', file=file)

