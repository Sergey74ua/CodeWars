# Range Extraction
def solution(args):
    s = ''
    arr = []
    for i in args:
        if len(arr) < 1 or i == arr[-1] + 1:
            arr.append(i)
            continue
        elif len(arr) == 1:
            s = s + str(arr[0])
        elif len(arr) == 2:
            s = s + str(arr[0]) + ',' + str(arr[1])
        else:
            s = s + str(arr[0]) + '-' + str(arr[-1])
        s += ','
        arr = [i]
    if len(arr) == 1:
        s = s + str(arr[0])
    elif len(arr) == 2:
        s = s + str(arr[0]) + ',' + str(arr[1])
    else:
        s = s + str(arr[0]) + '-' + str(arr[-1])
    return s

# тест для локального запуска
test = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]
print("Тестовый массив:")
print(test)
print("\nРезультат:")
print(solution(test))
print("Правильно:\n-10--8,-6,-3-1,3-5,7-11,14,15,17-20")
input()

# Данные для теста:
# [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]  -  -10--8,-6,-3-1,3-5,7-11,14,15,17-20
# [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]  -  -6,-3-1,3-5,7-11,14,15,17-20
# [-3,-2,-1,2,10,15,16,18,19,20]  -  -3--1,2,10,15,16,18-20

# Лучшие решения:
# def solution(args):
#    output = ''
#    for n in args:
#        if n == max(args): output += str(n)
#        elif n+1 not in args or (n-1 not in args and n+2 not in args): output += str(n) + ','
#        elif n-1 not in args: output += str(n) + '-'
#    return output