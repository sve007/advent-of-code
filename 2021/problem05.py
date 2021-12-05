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


class GeiserMap:

    def __init__(self, xsize, ysize):
        self.grid = np.zeros((xsize+1, ysize+1))
        self.ndangers = 0

    def add_geisers(self, start_coord: tuple, end_coord: tuple, diagonals=False):
        #  if vertical line
        if start_coord[0] == end_coord[0]:
            ycoords = np.arange(min(start_coord[1], end_coord[1]), max(start_coord[1], end_coord[1])+1)
            for y in ycoords:
                self.grid[y][start_coord[0]] += 1

        #  if horizontal line
        elif start_coord[1] == end_coord[1]:
            xcoords = np.arange(min(start_coord[0], end_coord[0]), max(start_coord[0], end_coord[0])+1)
            for x in xcoords:
                self.grid[start_coord[1]][x] += 1

        elif diagonals:
            #  if diagonal of slope 1, i.e. dx/dy = 1 i.e. dx=dy
            if abs(end_coord[0]-start_coord[0]) == abs(end_coord[1]-start_coord[1]):
                xcoords = range(start_coord[0], end_coord[0]+1) if end_coord[0] > start_coord[0] \
                        else reversed(range(end_coord[0], start_coord[0]+1))
                ycoords = range(start_coord[1], end_coord[1]+1) if end_coord[1] > start_coord[1] \
                        else reversed(range(end_coord[1], start_coord[1]+1))

                for x, y in zip(xcoords, ycoords):
                    self.grid[y][x] += 1

        self.ndangers = (self.grid > 1).sum()


gridsize = np.max(input_data)
map1 = GeiserMap(xsize=gridsize, ysize=gridsize)  # Map for part 1
map2 = GeiserMap(xsize=gridsize, ysize=gridsize)  # Map for part 2

for line in input_data:
    xcoord, ycoord = tuple(line[0]), tuple(line[1])
    map1.add_geisers(xcoord, ycoord)
    map2.add_geisers(xcoord, ycoord, diagonals=True)

print(f"Answer to problem 5 part 1: {map1.ndangers}")
print(f"Answer to problem 5 part 2: {map2.ndangers}"
      )