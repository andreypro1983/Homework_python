# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран получившийся кортеж.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))


# Вариант 1:
# 'house=дом car=машина men=человек tree=дерево'
string = input('Введите строку: ').split()
result = []
for i in string:
    result.append(tuple(i.split(sep='=')))
print(tuple(result))


# Вариант 2:
# 'house=дом car=машина men=человек tree=дерево'
string = input('Введите строку: ')
result = tuple(map(lambda x: tuple(x.split(sep='=')), string.split()))
print(result)
