# CSV
'''
fin = open('test.csv', 'r+', encoding='utf-8')
vals = []
for line in fin:
    now = line.split(',')
    vals.extend(list(map(int, now)))
print(vals)
print(vals[len(vals) // 2], sum(vals) / len(vals))          # медианное значение и среднее значение
fin.close()
'''
