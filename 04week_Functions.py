#Functions
def printList(myList):             #functions printList with param myList
    print(', '.join(tuple(map(str, myList))))
a = [1, 2, 3]
printList(a)

print('#---')
# def factorial
def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans
print(factorial(4))
print('#---')
#def max
def max2(a, b):
    if a > b:
        return a
    else:
        return b
c, d = map(int, input().split())
print(max2(c, d))
def xor                                    #Xor
def xorfunction(a, b):
    if a == b:
        return 0
    return 1
c = input()
d = input()
print(xorfunction(c, d))

def isPointInSquare(x, y):                #Coordinates
    return -1 <= x <= 1 and -1 <= y <= 1

x = float(input())
y = float(input())

if isPointInSquare(x,y):
    print('YES')
else:
    print('NO')


def sort3(a, b, c):                        #Sort
    d = [a, b, c]
    d.sort()
    e = list(d)
    return e
x = int(input())
y = int(input())
z = int(input())
print(*sort3(x, y, z))

