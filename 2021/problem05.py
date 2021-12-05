import numpy as np

with open("input_data/input_problem05", "r") as file:
    input_data = file.read().split("\n")

input_data = [line.split(" -> ") for line in input_data]
max_x = 0
max_y = 0

for i, l in enumerate(input_data):
    for j, t in enumerate(l):
        input_data[i][j] = [int(j) for j in t.split(",")]

input_data = np.array(input_data)
max_x = np.max(np.array(input_data)[:, 0])
max_y = np.max(np.array(input_data)[:, 1])
grid1 = np.zeros((max_x+3, max_y+3))

for line in input_data:

    x0 = line[0][0]
    x1 = line[1][0]
    y0 = line[0][1]
    y1 = line[1][1]

    if x0 == x1:
        y0, y1 = min(y0, y1), max(y0, y1)
        coords = np.arange(y0, y1+1)
        for y in coords:
            grid1[y][x0] += 1

    elif y0 == y1:
        x0, x1 = min(x0, x1), max(x0, x1)
        coords = np.arange(x0, x1+1)
        for x in coords:
            grid1[y0][x] += 1

answer1 = (grid1 > 1).sum()
print(f"Answer to problem 5 part 1: {answer1}")


grid2 = np.zeros((max_x+3, max_y+3))

for line in input_data:

    x0 = line[0][0]
    x1 = line[1][0]
    y0 = line[0][1]
    y1 = line[1][1]

    if x0 == x1:
        y0, y1 = min(y0, y1), max(y0, y1)
        coords = np.arange(y0, y1+1)
        for y in coords:
            grid2[y][x0] += 1

    elif y0 == y1:
        x0, x1 = min(x0, x1), max(x0, x1)
        coords = np.arange(x0, x1+1)
        for x in coords:
            grid2[y0][x] += 1

    elif abs(x1-x0) == abs(y1-y0):

        if x1 < x0:
            coordsx = reversed(range(x1, x0+1))
        else:
            coordsx = range(x0, x1+1)
        if y1 < y0:
            coordsy = reversed(range(y1, y0+1))
        else:
            coordsy = range(y0, y1+1)
        for x, y in zip(coordsx, coordsy):
            grid2[y][x] += 1

answer2 = (grid2 > 1).sum()
print(f"Answer to problem 5 part 2: {answer2}")