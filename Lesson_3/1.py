# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

def kratnost (x, y):
    if x%y == 0:
        return True
    else:
        return False

a = [0 for i in range(2, 10)]
b = [j for j in range(2, 10)]
for i in range (2, 100):
    for j in range (0, len(a)):
        if kratnost(i, j+2):
            a[j] = a[j] +1
for i in range(0, len(a)):
    print ('кратных {} -  вдиапазоне (2-99) {} чисел'.format(b[i], a[i]))
