# Disemvowel Trolls

def disemvowel(string_):
    for i in "aeiouAEIOU":
        string_ = string_.replace(i, '')
    return string_

# Тест для локального запуска
test = "This website is for losers LOL!"
print('Тестируем: ', test)
print('Результат: ', disemvowel(test))
print('Правильно: ', "Ths wbst s fr lsrs LL!")
input()

# Лучший вариант:
# def disemvowel(string):
#    return string.translate(None, 'aeiouAEIOU')