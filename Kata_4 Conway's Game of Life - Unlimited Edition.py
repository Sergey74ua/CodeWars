# Conway's Game of Life - Unlimited Edition

def get_generation(cells, generations):
    cellsSet = set()
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                cellsSet.add((i, j))
    from itertools import product
    for n in range(generations):
        cellsNew = set()
        cells = set()
        for (i, j) in cellsSet:
            for (ni, nj) in product((-1, 0, 1), (-1, 0, 1)):
                cellsNew.add((i + ni, j + nj))
        for (i, j) in cellsNew:
            x = 0
            for (ni, nj) in product((-1, 0, 1), (-1, 0, 1)):
                if (i + ni, j + nj) in cellsSet and (ni, nj) != (0, 0):
                    x += 1
            if x == 3:
                cells.add((i, j))
            elif x == 2 and (i, j) in cellsSet:
                cells.add((i, j))
        cellsSet = cells
    if not cellsSet:
        mi = mj = ni = nj = 0
    else:
        min_i = min(map(lambda x: x[0], cellsSet))
        min_j = min(map(lambda x: x[1], cellsSet))
        max_i = max(map(lambda x: x[0], cellsSet))
        max_j = max(map(lambda x: x[1], cellsSet))
    ri = max_i - min_i + 1
    rj = max_j - min_j + 1
    cells = [[0 for j in range(rj)] for i in range(ri)]
    for (i, j) in cellsSet:
        cells[i - min_i][j - min_j] = 1
    return cells

# тест для локального запуска
test = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
print("Тестовые данные:")
print(test)
print("\nРезультат:")
print(get_generation(test, 1))
print("Правильно:\n[[0, 1, 0], [0, 0, 1], [1, 1, 1]]")
input()

# Лучшие решения:
# def get_neighbours(x, y):
#    return {(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2)}
#
#def get_generation(cells, generations):
#    if not cells: return cells
#    xm, ym, xM, yM = 0, 0, len(cells[0]) - 1, len(cells) - 1
#    cells = {(x, y) for y, l in enumerate(cells) for x, c in enumerate(l) if c}
#    for _ in range(generations):
#        cells = {(x, y) for x in range(xm - 1, xM + 2) for y in range(ym - 1, yM + 2)
#                    if 2 < len(cells & get_neighbours(x, y)) < 4 + ((x, y) in cells)}
#        xm, ym = min(x for x, y in cells), min(y for x, y in cells)
#        xM, yM = max(x for x, y in cells), max(y for x, y in cells)
#    return [[int((x, y) in cells) for x in range(xm, xM + 1)] for y in range(ym, yM + 1)]