#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
import random
a = []
n = 15
for i in range(n):
    d = random.randint(2,100)
    a.append(d)
print('начальный массив: ' + str(a))
min = a[0]
index_min = 0
max = a[0]
index_max = 0
for i in range(n):
    if a[i]<min:
        min = a[i]
        index_min = i
    if a[i]>max:
        max=a[i]
        index_max = i
a[index_min],a[index_max]=a[index_max],a[index_min]
print(min, end=' ')
print(index_min)
print(max, end=' ')
print(index_max)
print('конечный  массив: ' + str(a))