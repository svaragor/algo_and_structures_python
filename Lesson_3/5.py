#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
import random
a = []
n = 30
max = 0
for i in range(n):
    d = random.randint(-100,100)
    a.append(d)
for i in range(len(a)):
    if a[i]<0 and max == 0:
        max = a[i]
    if a[i]<0 and a[i]>max:
        print(a[i])
        max = a[i]
print('начальный массив: ' + str(a))
print('минимальное отрифательное: {}'.format(max))