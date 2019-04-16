"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
def occurrence_search (x, y):
    counter = 0
    while x>0:
        if x%10 == y:
            counter +=1
        x = x//10
    return counter


a = int(input('введите количество вводиимых цифр'))
b = int(input('введите цифру для поиска'))
counter_loc = 0
for i in range(a):
    c = int(input('число: '))
    counter_loc += occurrence_search(c, b)
print('число вхождений = %d' % counter_loc)