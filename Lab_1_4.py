#4. Считать с клавиатуры непустую произвольную последовательность целых чисел. Найти:
#i. Сумму всех чисел последовательности (решить задачу используя циклическую конструкцию while)
print('Введите числа и дважды нажмите ENTER')
a = int(input('-->> '))
list = []
b = 10
while True:
    try:
        list.append(a)
        b = b + a
        a = int(input('-->> '))
    except:
        break;
print(b)

#ii. Количество всех чисел последовательности (решить задачу используя циклическую конструкцию while)
print('Введите числа и дважды нажмите ENTER')
n = int(input())
count = 0
counter = 0
while n > 0:
    count += n
    n = int(input())
    if n == 0:
        print('Сумма чисел:', count)
    counter = counter + 1
print('Количество чисел:', counter)

