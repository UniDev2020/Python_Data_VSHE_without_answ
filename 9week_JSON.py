#                                                       JSON
'''
https://apidata.mos.ru/v1/datasets?api_key=444bf4b4cafedfb90f61067c43347dd0&$skip=1&$top=1&$inlinecount=allpages
https://apidata.mos.ru/v1/datasets/658?api_key=444bf4b4cafedfb90f61067c43347dd0
https://apidata.mos.ru/v1/datasets/1248?api_key=444bf4b4cafedfb90f61067c43347dd0

https://apidata.mos.ru/v1/datasets/658/rows?api_key=444bf4b4cafedfb90f61067c43347dd0&$top=10
https://apidata.mos.ru/v1/datasets/658/rows?api_key=444bf4b4cafedfb90f61067c43347dd0&$top=5&$skip=10
'''

from urllib.request import urlopen
import json

total = 1000 #66411
i = 0
alllst = []
while i < total:                                                                           #получение данных порциями
    response = urlopen(
        'https://apidata.mos.ru/v1/datasets/1401/rows?api_key=444bf4b4cafedfb90f61067c43347dd0&$top=500&$skip=' + str(
            i))
    respData = response.read().decode('utf-8')                                       # получаем JSON список
    lst = json.loads(respData)                                                       # получаем Python список
    alllst.extend(lst)
    i += 500
    print(i)
fout = open('outage.json', 'w', encoding='utf-8')
json.dump(alllst, fout)
fout.close()
print(len(alllst))

'''
    for row in lst:
        cells = row['Cells']
        # print(row)
        addr = cells['Address']
        periods = cells['Periods']
        period = periods[0]
        begin = period['OutageBegin']
        end = period['OutageEnd']
        print(addr, begin, end)
'''




    # print(lst[0]['Cells']['Address'])
