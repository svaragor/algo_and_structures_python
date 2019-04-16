"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
counter = int (input('введите количество элементов'))
a = 1.0
summ_row = 0.0
for i in range(counter):
    if i%2 != 0:
        summ_row -= a
    else:
        summ_row += a
    a=a/2
print('summ = %f' % summ_row)