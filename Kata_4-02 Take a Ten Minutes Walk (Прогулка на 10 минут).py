# Take a Ten Minutes Walk
def is_valid_walk(walk):
    if len(walk)==10 and walk.count('n')==walk.count('s') and walk.count('e')==walk.count('w'):
        return True
    else:
        return False

# тест для локального запуска
test = ['n','s','n','s','n','s','n','s','n','s']
print("Тестовый маршрут:")
print(test)
print("\nРезультат:")
print(is_valid_walk(test))
input()

# Данные для теста:
# ['n','s','n','s','n','s','n','s','n','s'] - True
# ['w','e','w','e','w','e','w','e','w','e','w','e'] - False
# ['w'] - False
# ['n','n','n','s','n','s','n','s','n','s']) - False

# Лучшие решения:
#    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')