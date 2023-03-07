# Задача 32: Определить индексы элементов массива (списка), значения которых
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
number = int(input('Введите длину массива: '))
min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальное число: '))
list1 = []
for i in range(number+1):
    i = random.randint(1,10)
    list1.append(i)
print(list1)
for i in range(len(list1)):
    if min_number <= list1[i] <= max_number:
        print(f'Число которое входят в диапозон равно {list1[i]}. Индекс числа равен {i}')
