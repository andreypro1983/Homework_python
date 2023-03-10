# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую
#  неотрицательную степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# Вариант 1:
def num_power(number, power):
    if power == 0:
        return 1
    else:
        return number*num_power(number, power-1)


a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
print(num_power(a, b))

# Вариант 2 (можно указывать отрицательную степень)


def num_all_power(number, power):
    if power == 0:
        return 1
    else:
        if power >= 0:
            return number*num_all_power(number, power-1)
        else:
            return 1/(number*num_all_power(number, -power-1))


a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
print(num_all_power(a, b))
