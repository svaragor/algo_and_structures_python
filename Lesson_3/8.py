"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
import random
a = []
n = 5
m = 4
for i in range(m):
    a.append([])
    summ = 0
    for j in range (n-1):
        d = random.randint(2,100)
        summ += d
        a[i].append(d)
    a[i].append(summ)
for i in range(m):
    print(str(a[i]))