"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
a = int(input ('введите натуральное число '))
b = a
switch_num = ''
while a>0:
	digit = a%10
	a=a//10
	switch_num = switch_num + str(digit) 
print(switch_num)

#Рекурсия
def switchNum (x, x_str):
	if x==0:
		print(x_str)
		return
	digit = x%10
	x_str = x_str + str(digit)
	switchNum(x//10, x_str)

switchNum(b, '')