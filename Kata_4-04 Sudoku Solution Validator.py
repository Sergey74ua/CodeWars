# Sudoku Solution Validator
def valid_solution(board):
    col = [[0 for i in range(9)] for j in range(9)]
    cub = [[[] for j in range(3)] for n in range(3)]
    for y in range(9):
        if len(set(board[y])) < 9:
            return False
        for x in range(9):
            if board[y][x] == 0:
                return False
            col[x][y] = board[y][x]
            cub[y//3][x//3].append(board[y][x])
    for i in col:
        if len(set(i)) < 9:
            return False
    for i in cub:
        for j in i:
            if len(set(j)) < 9:
                return False
    return True

# тест для локального запуска (true):
test = [
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]
print("Тестовый массив:")
print(test)
print("\nРезультат:")
print(valid_solution(test))
input()

# Еще данные для теста (false):
# [
#  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#  [6, 7, 2, 1, 9, 0, 3, 4, 8],
#  [1, 0, 0, 3, 4, 2, 5, 6, 0],
#  [8, 5, 9, 7, 6, 1, 0, 2, 0],
#  [4, 2, 6, 8, 5, 3, 7, 9, 1],
#  [7, 1, 3, 9, 2, 4, 8, 5, 6],
#  [9, 0, 1, 5, 3, 7, 2, 1, 4],
#  [2, 8, 7, 4, 1, 9, 6, 3, 5],
#  [3, 0, 0, 4, 8, 1, 1, 7, 9]
#]

# Лучшие решения:
# valid_solution=lambda b,f=lambda e:{*e}=={*range(1,10)}:all(map(f,b))and all(map(f,zip(*b)))and 9==len({*b[0][0:3],*b[1][0:3],*b[2][0:3]})
