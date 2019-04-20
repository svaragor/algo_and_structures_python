# 4.	Определить, какое число в массиве встречается чаще всего.
import random
a = []
#a =[70, 33, 44, 54, 76, 23, 7, 59, 73, 20, 60, 100, 7, 95, 23]
n = 15
b = {}
for i in range(n):
    d = random.randint(2,100)
    a.append(d)
    #d = a[i]
    if b.get(str(d)):
        c = b[str(d)]
        b[str(d)] = c+1
    else:
        b[str(d)] = 1
print('начальный массив: ' + str(a))
#print(b)
max =1
key_max = 'все числа встречаются по одному разу'
for key in b:
    if max<b[key]:
        max=b[key]
        key_max = key
print('чаще всего встречается: {}'.format(key_max))
#можно конечно отработать и случай когда с одинаоквой статистикой включается несколько чисел, но как-нибудь на досуге