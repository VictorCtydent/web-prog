#1.	Считать из параметров командной строки одномерный массив, состоящий из N целочисленных элементов.
#2.	Вывести в консоль сумму элементов с четными номерами
#3.	Вывести в консоль произведение элементов с нечетными номерами.
#4.	Поменять местами минимальный и максимальный элементы. Вывести результат в консоль.
from math import prod

A=[]
A = [ int(input('Введите число для массива:')) for i in range(5) ]
print('Одномерный массив:', A)
even_nums = []
i: int
for i in A:
    if i % 2 == 0:
        even_nums.append(i)
summ = sum(even_nums)
even_nums_1 = []
i: int
for i in A:
    if i % 2 != 0:
        even_nums_1.append(i)
proizv = prod(even_nums_1)
print('Сумма элементов с четными номерами:', summ)
print('Произведение элементов с нечетными номерами:', proizv)
Smena = A
tMax = Smena.index(max(Smena))
tMin = Smena.index(min(Smena))
Smena[tMax], Smena[tMin] = Smena[tMin], Smena[tMax]
print('Поменять местами минимальный и максимальный элементы:', Smena)
