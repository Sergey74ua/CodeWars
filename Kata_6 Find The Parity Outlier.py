# Find The Parity Outlier
def find_outlier(integers):
    if integers[0]%2+integers[1]%2+integers[2]%2>1:
        x=0
    else:
        x=1
    for i in integers:
        if i%2==x:
            return i


# тест для локального запуска
test = [2, 4, 6, 8, 10, 3]
print("Тестовый массив:")
print(test)
print("\nРезультат:")
print(find_outlier(test))
input()

# Данные для теста:
# [2, 4, 6, 8, 10, 3] - 3
# [2, 4, 0, 100, 4, 11, 2602, 36] - 11
# [160, 3, 1719, 19, 11, 13, -21] - 160

# Лучшие решения:
#    odds = [x for x in int if x%2!=0]
#    evens= [x for x in int if x%2==0]
#    return odds[0] if len(odds)<len(evens) else evens[0]