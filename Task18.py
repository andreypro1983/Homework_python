# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
n = int(input('Введите количество элементов в массиве: '))
x = int(input('Введите искомое значение x: '))
list1 = [randint(1, n) for i in range(n)]
print(*list1)
number = None
dif = max(list1)
for i in list1:
    if dif > abs(x-i):
        dif = abs(x-i)
        number = i
print(number)
