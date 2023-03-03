# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов
# второго множества. Затем пользователь вводит сами элементы множеств.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
    less = [i for i in arr[1:] if i <=pivot]
    greater = [i for i in arr[1:] if i >pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
list1 = input('Введите элеменеты первого множества: ').split()
list2 = input('Введите элеменеты второго множества: ').split()
listNew1 = []
listNew2 = []
listEnd = []
for i in set(list1):
    listNew1.append(i)
for i in set(list2):
    listNew2.append(i)
listNew1 = quick_sort(listNew1)
listNew2 = quick_sort(listNew2)
for i in range(len(listNew1)):
    for j in range(len(listNew2)):
        if listNew1[i] == listNew2[j]:
            listEnd.append(listNew1[i])
print(listNew1)
print(listNew2)
print(quick_sort(listEnd))
