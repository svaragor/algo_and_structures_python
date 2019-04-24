"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""
import timeit

#рекурсия
def math_series (x, n):
    if x == n:
        return (x)
    return x + math_series(x+1, n)


#нерекурсивная функция
def math_series_circl (n):
    res_cicl = 0
    for i in range(n):
        res_cicl = res_cicl + i + 1
    return (res_cicl)

n = int(input('введите число '))

res_formula = n * (n + 1) / 2
res_func = math_series_circl(n)

if res_formula == res_func:
    print('гипотеза подтверждена')
else:
    print('гипотеза опровергнута')

#запуск рекурсии
x = 1
res_func = math_series(x, n)

if res_formula == res_func:
    print('гипотеза подтверждена')
else:
    print('гипотеза опровергнута')

print (timeit.timeit("math_series_circl (n)", setup="from __main__ import math_series_circl, n", number=1000))
print (timeit.timeit("math_series(x, n)", setup="from __main__ import math_series, x, n", number=1000))


"""
Очень странные результаты при тесте с одинаковыми начальными условиями.
Например в некоторых случаях рекурсия быстрее, но при тесте не подтверждается закономерность например при n=99


введите число 45
гипотеза подтверждена
гипотеза подтверждена
0.0036798159999307245
0.006589961005374789

введите число 45
гипотеза подтверждена
гипотеза подтверждена
0.009817404003115371
0.01766610099002719

введите число 45
гипотеза подтверждена
гипотеза подтверждена
0.014498735996312462
0.015543367000645958

введите число 45
гипотеза подтверждена
гипотеза подтверждена
0.003972670005168766
0.005886804996407591

введите число 99
гипотеза подтверждена
гипотеза подтверждена
0.025029292999533936
0.020293979003326967

введите число 99
гипотеза подтверждена
гипотеза подтверждена
0.006792561005568132
0.016658132008160464

"""