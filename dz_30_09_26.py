import random


try:
    rows, colms = int(input("размеры поля шир (больше 10)")), int(input("размеры поля выс (больше 10)"))

    cef = int(input("плотность от 1 до 10"))

    islands_count = random.randint(round((rows * colms) * cef / 200), round((rows * colms) * cef / 200) + 2)
except ValueError:
    rows, colms, cef, islands_count = 0, 0, 0, 0
    print("ValueError")

del_point, add_point, main_point, island_borders, add_point_all_islands = [], [], [], [], []

matrix = [["0" for c in range(colms)]for r in range(rows)]



def remove_double(lst):
    res_list = []
    for item in lst:
        if item not in res_list:
            res_list.append(item)
    return res_list


def is_water(x, y):
    if matrix[y][x] == "0":
        return True
    else:
        return False

def is_ground(x, y):
    if matrix[y][x] == "*":
        return True
    else:
        return False


def water(x, y):
    matrix[y][x] = "0"


def ground(x, y):
    global matrix, rows, colms

    if x in [i for i in range(3, rows-3)] and y in [i for i in range(3, rows-3)]:
        matrix[y][x] = "*"
        add_point.append([x, y])
        add_point_all_islands.append([x, y])

    else:
        del_point.append([x, y])

def piece_of_island_gen(x, y):
    global matrix, rows, colms
    ground(x, y)
    main_point.append([x, y])

    ground(x+1, y)
    ground(x-1, y)
    ground(x, y+1)
    ground(x, y-1)

def island_gen():
    global matrix, rows, colms, del_point, add_point, main_point, island_borders, add_point_all_islands

    del_point, add_point = [], []

    count = 0

    while True:
        cords = [random.randint(3, colms - 4), random.randint(3, rows - 4)]
        if not(cords in add_point_all_islands):
            add_point.append(cords)

            break
        elif count > 100:
            add_point.append(add_point_all_islands[-1])
            break

        count += 1



    for i in range(random.randint(2, 10)):
        if len(add_point) > 3:
            new_main_point = random.randint(-4, -1)
        else:
            new_main_point = random.randint(0, len(add_point)-1)

        piece_of_island_gen(add_point[new_main_point][0], add_point[new_main_point][1])

    add_point = remove_double(add_point)

    for j in add_point:
        if is_water(j[0]+1, j[1]):
            island_borders.append([j[0]+1, j[1]])
        if is_water(j[0]-1, j[1]):
            island_borders.append([j[0]-1, j[1]])
        if is_water(j[0], j[1]+1):
            island_borders.append([j[0], j[1]+1])
        if is_water(j[0], j[1]-1):
            island_borders.append([j[0], j[1]-1])
        if is_water(j[0]+1, j[1]-1):
            island_borders.append([j[0]+1, j[1]-1])
        if is_water(j[0]+1, j[1]+1):
            island_borders.append([j[0]+1, j[1]+1])
        if is_water(j[0]-1, j[1]-1):
            island_borders.append([j[0]-1, j[1]-1])
        if is_water(j[0]-1, j[1]+1):
            island_borders.append([j[0]-1, j[1]+1])




    add_point_all_islands = remove_double(add_point_all_islands)
    island_borders = remove_double(island_borders)




    main_point.append("|")


if islands_count > 0 and rows > 10 and colms > 10:
    for i in range(islands_count):
        island_gen()

    for i in island_borders:
        water(i[0], i[1])
else:
    print("недостаточно места для генерации")





print(island_borders, add_point, add_point_all_islands, main_point, sep='\n')

for row in matrix:
    for item in row:
        print(item, end = " ")
    print()

print(islands_count)

