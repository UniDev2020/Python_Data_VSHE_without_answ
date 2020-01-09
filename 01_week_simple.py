M = -82372642987463918269721
H = 60
D = 24
print('A = ', M % H )

A = int(input())
B = int(input())
D = int(input())
print((A*B)//(D*1) + 1)

A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = A*2*C+B*2*C
print((P - 1) // D + 1)
print((14 - 1) // 5 + 1)

A = int(input())
B = int(input())
C = int(input())
D = int(input())
x = int(input())
storeOpen = A <= x <= B and not(C <= x <= D)
print(storeOpen)

A = int(input())
B = int(input())
if A > B:
    print(A)
else:
    print(B)

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('YES')
else:
    print('NO')

N = int(input())
x = 1
print(x, sep = ' ', end=' ')
while (x) <= N:
    if x % 2 == 0:
        print(x, sep= ' ', end=' ')
    x = x * 2

sumseq = 0
now = int(input())
while now != 0:
    sumseq += now
    now = int(input())
print(sumseq)

now = int(input())
maxNum = now
cntMax = 1
while now != 0:
    if maxNum < now:
        maxNum = now
        cntMax = 1
    elif now == maxNum:
        cntMax += 1
    now = int(input())
print(cntMax)

newV = int(input())
lastV = newV
cntMax = 0
while newV != 0:
    if lastV < newV:
        cntMax += 1
    newV = int(input())
print(cntMax)

newV = int(input())
maxV = newV
cntMax = 0
while newV != 0:
    if newV == maxV:
        cntMax += 1
    if newV > maxV:
        maxV = newV
        cntMax = 1
    newV = int(input())
print(cntMax)

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()

N = int(input())
i = 0
while i < N:
    i += 1
    for i in range(1, i + 1):
        print(i, sep='', end='')
    print()

A = int(input())
B = int(input())
i = A
while i <= B:
    i += 1
    print(A, sep=' ', end=' ')
    A += 1

x = float(input())
y = float(input())
print(x/y)

from math import floor
from math import ceil
x = float(input())
y = floor(x)
answer = x - y
if round(answer, 2) >= 0.5:
    print(ceil(x))
else:
    print(floor(x))

import math
A = float(input())
answer = abs(math.floor(A) - A)
print(round(answer, 2))

print(round((A - round(A)), 2))

import math
A = float(input())
if abs(A - math.ceil(A)) == 0.5:
    print(math.ceil(A))
else:
    print(round(A))

import math
P = int(input())
X = int(input())
Y = int(input())
S = (X * 100) + Y
G = S + ((S * P)/100)
print(int(float(G // 100)), end=' ')
print(int(float(G % 100)))

print(G)
print(int(G // 100))
if round(G/100)*100 > round(G):
    print(math.floor((G)/100), end =' ')
    print(abs(round(G / 100) * 100 - (round(G)+100)))
else:
    print(round(G/100), end=' ')
    print(round(G) - round(G/100)*100)

import math
A = float(input())
answer = (A - math.floor(A))
print(round(answer, 10))

s = input()
print(s[2])         #1
print(s[-2])        #2
print(s[:5])        #3
print(s[:-2])       #4
print(s[::2])       #5
print(s[1::2])      #6
print(s[::-1])      #7
print(s[-1::-2])    #8
print(len(s))       #9

s = input()
subs = input()
print(subs in s)

s = input()
subs = 'f'
pos = s.find(subs)
posfirst = s.find(subs)
poslast = s.rfind(subs)
cnt = 0
while pos != -1:
    s = s[pos + len(subs):]
    pos = s.find(subs)
    cnt += 1
if cnt == 1 and cnt != 0:
    print(posfirst)
elif cnt >= 2:
    print(posfirst, sep='', end=' ')
    print(poslast)

pos = s.find(subs)
while pos != -1:
    print(pos)
    s = s[pos + len(subs):]
    pos = s.find(subs)

s = input()
if s.count(' ') == 1 and s.count(' ') !=0:
    print(2)
else:
    print(s.count(' ') + 1)

a = 'i love python'
print(a[:4])
print(a[0:4])
print(a[0:4:1])
print()
print('%.4s'%a)
print()
print('{:.4}'.format(a))
print('{:1.4}'.format(a))

a=(5,)
print(a, 'the type a is = ', type(a))
a=(5)
print(a, 'the type a is = ', type(a))
a=tuple(5)
print(a, 'the type a is = ', type(a))
a=tuple(5,)
print(a, 'the type a is = ', type(a))
a = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a, 'the type a is = ', type(a))
print(a[::-1])
print(a[-1:0:])
import re
p = re.compile(r'(exe|py|htm|html)')
p.sub('files','i can use exe')


p=re.compile(r'(exe|py|htm|html)')
a = p.sub('files','i can run exe py html',count=0)
print(a)

s = input()
subs = input()
pos = s.find(subs)
start = s[:pos]
print(start)
finish = s[pos + len(subs):]
print(finish)
news = start + 'Petya' + finish
print(news)

import re
s = input()
p = re.compile(r'AB')
print(p)
a = p.sub(s, 'BA')
print(a)
firstStep = s.replace('A', 'B')
print(firstStep)
secondStep = s.replace('B', 'A')
print(secondStep)
news = firstStep.replace('B', 'A')
# print(news)
s = input()
i = 0
news = ''
for i in s:
    if i == 'A':
        i = i.replace('A', 'B')
    elif i == 'B':
        i = i.replace('B', 'A')
    news += i
print(news)

s = input()
firsth = s.find('h')
secondh = s[::-1].find('h')
subs = s[firsth+1:]
repls = subs[:-secondh-1].replace('h','H')
start = s[:firsth+1]
finish = s[-secondh-1:]
news = start + repls + finish
print(news)


print(start)
subs = s.replace('h','H')
print(subs)

s = str(input())
news = ''
if s[0] == '8':
    news = s[:1].replace('8', '+7') + s[1:]
elif len(s) == 9:
    news = '+7' + s
else:
    news = s
print(news)




