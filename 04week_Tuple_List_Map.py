#Tuple
testTuple = (1, 2, 3)
testTuple2 = (4, 5, 6)
print(testTuple, type(testTuple))
print(testTuple + testTuple2)
print(testTuple[1:2])                            #tuple with one element
a = 1
b = 2
(a, b) = (b, a)
print((a, b))

#range and for
a = tuple(range(1, 101))
print(a)
# ---
for color in ('red','yellow','grey'):
    print(color, 'apple')
print('#---')
for i in range(1, 11):
    for j in range(1, 11):
        if i * j < 10:
            print(end=' ')
        print(i * j, end = ' ')
    print()
print('#---')
#list
a = [1, 2, 3]
b = a
c = a[:]
a[0] = 5
print(a, b, c)
print('#---')
a = []
x = int(input())
while x != 0:
    a.append(x)
    x = int(input())
print(a[::-1])

split
print('#---')
str = input()
l = str.split(' ')
for i in l:
    print(i, end='\n')

join
subs = input()
str =  input()
l = str.split(' ')
res = subs.join(l)
print(res)

#map                                           Most important!!!
a = list(map(int, input().split()))                              # split the str and change type to int
print(*a[::-1])                                                  # show list with spaces without []
print(', '.join(list(map(str, a))))                              # show str with ',' as a splitter

Ex-1
a = list(map(int, input().split()))
res = a[::2]
print(', '.join(list(map(str, res))))
Ex-2
a = list(map(int, input().split()))
for i in a:
    if i % 2 == 0:
        print(i, end=' ')
Ex-3
a = list(map(int, input().split()))
pr = a[0]
for i in a:
    if i > pr:
        pr = i
b = a.index(pr)
print(pr, b)
Ex-4
a = list(map(int, input().split()))
max = a[0]
pr = a[0]
for i in a:
    if i > max:
        max = i
        print(i, end= ' ')
    elif i > pr:
        print(i, end=' ')
    pr = i
Ex-5
a = list(map(int, input().split()))
cnt = 0
for i in range(1,len(a)-1):
     if a[i-1] < a[i] > a[i+1]:
         cnt += 1
print(cnt)
Ex-6
a = list(map(int, input().split()))
b = []
for i in a:
    if i > 0:
       b.append(i)
minV = min(b)
print(minV)
Ex-7
a = list(map(int, input().split()))
maxEl = max(a)
minEl = min(a)

maxInd = a.index(maxEl)
minInd = a.index(minEl)

a[maxInd] = minEl
a[minInd] = maxEl

print(', '.join(list(map(str, a))))
