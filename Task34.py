# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко
# он их придумывает, Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой
# фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

# Вариант1:

vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
sing = 'пара-ра-рам рам-пам-папам па-ра-па-да'
sing = list(sing.split())
list1 = []
for word in sing:
    count = 0
    for j in range(len(word)):
        if word[j] in vowel:
            count += 1
    list1.append(count)
    # print(list1)
if len(set(list1)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')


# Вариант2


def same_by(characteristic, objects):
    objects = list(map(characteristic, objects.split()))
    if len(set(objects)) == 1:
        return ('Парам пам-пам')
    else:
        return ('Пам парам')


def count_vowel(word):
    count = 0
    for j in range(len(word)):
        if word[j] in vowel:
            count += 1
    return count


vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
# 'пара-ра-рам рам-пам-папам па-ра-па-да'
sing = input('Введите песню: ')
print(same_by(lambda x: count_vowel(x), sing))