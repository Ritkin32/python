# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
import random
number = int(input('Введите длину массива:' ))
desNumber = int(input('Введите число:' ))
index = 0
list = []
for i in range(1,number+1):
    i = random.randint(1,number)
    list.append(i)
print(list)
min = abs(desNumber - list[0])
for j in range(1, number):
    count = abs(desNumber - list[j])
    if count < min:
        min = count
        index = j
print(f'Число {list[index]} наиболее близкий эллемент к числу {desNumber}, их разница составляет {abs(desNumber - list[index])}')