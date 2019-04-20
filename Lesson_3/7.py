"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
import random
a = []
n = 15
for i in range(n):
    d = random.randint(1,100)
    a.append(d)
if a[0]<a[1]:
    min_1 = a[0]
    min_2 = a[1]
else:
    min_1 = a[1]
    min_2 = a[0]
for i in range(2, len(a)):
    if a[i]<=min_1:
        min_2 = min_1
        min_1 = a[i]
    elif a[i]<min_2:
        min_2 = a[i]
print('начальный массив: ' + str(a))
print('минимум 1 = {}, минимум 2 = {}'.format(min_1, min_2))