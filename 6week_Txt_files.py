#                                                 Work with files
'''
fin = open('test.txt', 'r', encoding='utf8')                                # Read the file
s = sum(map(int, fin.readline().split()))                                   # sum the int's
s2 = sum(map(int, fin.readline().split()))                                  # sum the second string
fin.close()                                                                 # Close the file
print(s, s2)

print('#---')

fin = open('test2.txt', 'r', encoding='utf8')
cnt = 0
for line in fin:                                                            # How many 'abc' in the file
    if 'abc' in line:
        cnt += 1
fin.close()
print(cnt)
print('#---')

fin = open('input-3.txt', 'r', encoding='utf8')
s = fin.read().split()                                                      # split spaces and /n
fin = open('input-3.txt', 'r', encoding='utf8')
fout = open('output-3.txt', 'w', encoding='utf8')
s1 = fin.readlines()
sSum = sum(map(int, s))
print(s, sSum, sep='\n')
print('#---')
print(''.join(s1[::-1]), file = fout, end='')                               # write to file in reverse mode
fout.close()
'''
