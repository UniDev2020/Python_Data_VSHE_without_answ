# Sorting
'''lst = (list(map(int, input().split())))                      # read list from input
sortedList = sorted(lst)                                     # use it if you need an original list later
sortedListRev = sorted(lst, reverse=True)                    # reverse the sorted list
lst.sort()
print(*sortedList)
print(*lst)
print(*sortedListRev)
print('#---')
sortedList1 = sorted('bcdhgs')                               # sorted a sylabls
print(sortedList1)'''

# Sorting tuple
'''def mykey(x):                                                # sorting for second index
    return x[1]

tup = (('Ivanov', 180), ('Petrov', 190), ('Sidorov', 175), ('abc', 180))
sortedTup = sorted(tup, key=mykey, reverse=True)
print(sortedTup)'''

# Set and operations with set
'''myset = {2, 3, 5, 7, 11}
x = int(input())
print(x in myset)
myset.add(x)                                                   # add element
print(x in myset)
myset.remove(x)                                                # remove, delete with errors
print(x in myset)
myset.discard(x)                                               # remove without errors
print(x in myset)

myset1 = set(map(int, input().split()))                        # read set from input with spaces
print(myset1)
print(*myset1)
for now in sorted(myset1):                                     # output with operation with elements in sorted set
    print(now**2, end=' ')

myset1 = set(map(int, input().split()))
myset2 = set(map(int, input().split()))
myset3 = myset1 | myset2                                         # обьединение
myset4 = myset1 & myset2                                         # пересечение
myset5 = myset1 - myset2                                         # вычитание
myset6 = myset1 ^ myset2                                         # семметрическая разность'''

#Dictionary

'''dct = {'a': 1, 'b': 2, 'c': 3}                                     # создание словаря
dct['d'] = 4                                                       # добавление элемента
print('a' in dct)                                                  # печать значения элемента из словаря
del dct['a']                                                       # удаление элемента из словаря
for key in sorted(dct):                                            # проход по словарю и вывод значений
    print(key, dct[key])
print(dct)
print('#---')
dct1 = {'aces': 12, 'cese': 34, 'base': 78}
dct2 = {}
for key in sorted(dct1):
    dct2[dct1[key]] = key                                          # меняем метами ключи и значения
print(dct1, dct2, sep='\n')'''

# Difficult examples
'''
3
apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa
'''
# def parse(s):
#     english = s[:s.find(' - ')]
#     latinss = s[s.find(' - ') + 3:]
#     latins = latinss.split(',')
#     for i in range(len(latins)):
#         latins[i] = latins[i].strip()
#     return english, latins
#
#
# n = int(input())
# latinEng = {}
# for i in range(n):
#     s = input()
#     english, latins = parse(s)                                       # принимает str и возвращает список англ и лат сл
#     for latin in latins:
#         if latin not in latinEng:
#             latinEng[latin] = []
#         latinEng[latin].append(english)
# print(len(latinEng))
# for latin in sorted(latinEng):
#     print(latin, end=' - ')
#     print(', '.join(sorted(latinEng[latin])))                        # обьединим список слов в одну строку исп ','

