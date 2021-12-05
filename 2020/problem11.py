import numpy as np

with open("input_data/input_problem11", "r") as file:
    input_data = np.array([list(line) for line in file.read().split("\n")])

class WaitingRoom:
    def __init__(self, layout):
        self.layout = layout
        self.change = True

    def update_layout_part1(self):
        self.change = True
        old_layout = np.copy(self.layout)
        bounds = np.shape(old_layout)

        for y, x in np.ndindex(old_layout.shape):
            if old_layout[y, x] == "L":
                self.layout[y, x] = '#'
                for adjacent_y in [y-1, y, y+1]:
                    if 0 <= adjacent_y < bounds[0]:
                        for adjacent_x in [x-1, x, x+1]:
                            if 0 <= adjacent_x < bounds[1]:
                                if not (adjacent_y == y and adjacent_x == x):
                                    if old_layout[adjacent_y, adjacent_x] == "#":
                                        self.layout[y, x] = "L"

            if old_layout[y, x] == "#":
                counter = 0
                for adjacent_y in [y-1, y, y+1]:
                    if 0 <= adjacent_y < bounds[0]:
                        for adjacent_x in [x-1, x, x+1]:
                            if 0 <= adjacent_x < bounds[1]:
                                if not (adjacent_y == y and adjacent_x == x):
                                    if old_layout[adjacent_y, adjacent_x] == "#":
                                        # print(f"Adding 1 for: {y, x} because of # in {adjacent_y, adjacent_x}")
                                        counter += 1
                                        # print(counter)
                                    if counter == 4:
                                        # print("Quitting because I found 4 occupied seats.")
                                        self.layout[y, x] = "L"
                                        break

        if (old_layout == self.layout).all():
            self.change = False

        self.n_occupied()

        return

    def update_layout_part2(self):
        self.change = True
        old_layout = np.copy(self.layout)
        bounds = np.shape(old_layout)

        for y, x in np.ndindex(old_layout.shape):
            if old_layout[y, x] == "L":
                self.layout[y, x] = '#'
                for adjacent_y in [y-1, y, y+1]:
                    if 0 <= adjacent_y < bounds[0]:
                        for adjacent_x in [x-1, x, x+1]:
                            if 0 <= adjacent_x < bounds[1]:
                                if not (adjacent_y == y and adjacent_x == x):
                                    if old_layout[adjacent_y, adjacent_x] == "#":
                                        self.layout[y, x] = "L"

            if old_layout[y, x] == "#":
                counter = 0
                for adjacent_y in [y-1, y, y+1]:
                    if 0 <= adjacent_y < bounds[0]:
                        for adjacent_x in [x-1, x, x+1]:
                            if 0 <= adjacent_x < bounds[1]:
                                if not (adjacent_y == y and adjacent_x == x):
                                    if old_layout[adjacent_y, adjacent_x] == "#":
                                        # print(f"Adding 1 for: {y, x} because of # in {adjacent_y, adjacent_x}")
                                        counter += 1
                                        # print(counter)
                                    if counter == 4:
                                        # print("Quitting because I found 4 occupied seats.")
                                        self.layout[y, x] = "L"
                                        break

        if (old_layout == self.layout).all():
            self.change = False

        self.n_occupied()

        return

    def n_occupied(self):
        self.occupied_seats = (self.layout == "#").sum()
        return


seating = WaitingRoom(input_data)

while seating.change:
    seating.update_layout()

answer1 = seating.occupied_seats

print(f"Answer to problem 11 part 1: {answer1}")




