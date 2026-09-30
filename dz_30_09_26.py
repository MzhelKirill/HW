import random
col, ro = 0, 0
rows, colms = 10, 10

matrix = [["0" for c in range(colms)]for r in range(rows)]


x = random.randint(3, rows - 4)
y = random.randint(3, colms - 4)

matrix[x][y] = "*"
if x + 1 < rows - 4:
    matrix[x+1][y] = "*"
if x - 1 > rows - 4:
    matrix[x-1][y] = "*"
if y + 1 < colms - 4:
    matrix[x][y+1] = "*"
if y - 1 > colms - 4:
    matrix[x][y-1] = "*"

print(x, y)

for row in matrix:
    for item in row:
        print(item, end = " ")
    print()




