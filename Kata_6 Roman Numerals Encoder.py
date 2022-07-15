# Roman Numerals Encoder

def unique_in_order(iterable):
    arr = []
    for i in iterable:
        if len(arr) == 0 or i != arr[-1]:
            arr.append(i)
    return arr

# Тест для локального запуска
test = 'AAAABBBCCDAABBB'
print('Тестируем: ', test)
print('Результат: ', unique_in_order(test))
print('Правильно: ', ['A','B','C','D','A','B'])
input()

# Лучший вариант:
# unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]
