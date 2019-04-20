"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
import random
a = []
n = 15
summ = 0
for i in range(n):
    d = random.randint(2,100)
    a.append(d)
    summ += d
    if i ==0:
        min = d
        max = d
    if d<min:
        min = d
    if d>max:
        max = d
print('начальный массив: ' + str(a))
print('summ = {}, min = {}, max = {}'.format(summ,min, max))
print('сумма элементов за минусом максимального и менимального = {}'.format(summ-max-min))