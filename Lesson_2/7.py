"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""
#рекурсия
def math_series (x, n):
    if x == n:
        return (x)
    return x + math_series(x+1, n)




n =int(input('введите число'))
res_formula = n*(n+1)/2
res_cicl = 0
for i in range(n):
    res_cicl = res_cicl+i+1
if res_cicl == res_formula:
    print('гипотеза подтверждена')
else:
    print('гипотеза опровергнута')

#запуск рекурсии
res_recurtion = math_series(1, n)
if res_recurtion == res_formula:
    print('гипотеза подтверждена')
else:
    print('гипотеза опровергнута')