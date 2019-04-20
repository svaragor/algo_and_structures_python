# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
a = []
min = []
n = 5
m = 5
for i in range(m):
    a.append([])
    for j in range (n):
        d = random.randint(2,100)
        a[i].append(d)
for j in range(n):
    min_loc = a[0][j]
    for i in range(1, m):
        if a[i][j]<min_loc:
            min_loc = a[i][j]
    min.append(min_loc)
max_loc = min[0]
for i in range(len(min)):
    if max_loc<min[i]:
        max_loc = min[i]
print('маирица')
for i in range(m):
    print(str(a[i]))
print('массив минимумов строк: ' + str(min))
print('максимум среди минимумов = {}'.format(max_loc))