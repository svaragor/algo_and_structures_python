"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
def occurrence_search (x):
    counter = 0
    while x>0:
        counter +=x%10
        x = x//10
    return counter


counter_loc = 0
max = 0
while 1:
    c = int(input('число или 0-для окончания: '))
    if c==0:
        break
    counter_loc = occurrence_search(c)
    if max<counter_loc:
        max = counter_loc
        d = c
print('максимальная сумма цифр = %d в числе %d' % (max, d))