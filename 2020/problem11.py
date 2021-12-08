import numpy as np
import matplotlib.pyplot as plt

with open("input_data/input_problem11", "r") as file:
    input_data = np.array([list(line) for line in file.read().split("\n")])

input_data = np.select([input_data == '#', input_data == 'L', input_data == '.'], [2, 1, 0])


class WaitingRoom:
    def __init__(self, layout):
        self.layout = layout
        self.change = True
        self.occupied_seats = 0
        self.old_layout = None
        self.bounds = None
        self.counter = 0
        self.unit_vector = None
        self.adjacent_y = None
        self.adjacent_x = None

    def update_layout_part1(self):
        self.old_layout = np.copy(self.layout)
        self.bounds = np.shape(self.old_layout)

        for y, x in np.ndindex(self.old_layout.shape):
            if self.old_layout[y, x] == 1:
                self.layout[y, x] = 2
                for self.adjacent_y, self.adjacent_x in [(i, j) for i in [y-1, y, y+1] for j in [x-1, x, x+1]]:
                    if 0 <= self.adjacent_y < self.bounds[0]:
                        if 0 <= self.adjacent_x < self.bounds[1]:
                            if not (self.adjacent_y == y and self.adjacent_x == x):
                                if self.old_layout[self.adjacent_y, self.adjacent_x] == 2:
                                    self.layout[y, x] = 1

            if self.old_layout[y, x] == 2:
                self.counter = 0
                for self.adjacent_y, self.adjacent_x in [(i, j) for i in [y-1, y, y+1] for j in [x-1, x, x+1]]:
                    if 0 <= self.adjacent_y < self.bounds[0]:
                        if 0 <= self.adjacent_x < self.bounds[1]:
                            if not (self.adjacent_y == y and self.adjacent_x == x):

                                if self.old_layout[self.adjacent_y, self.adjacent_x] == 2:
                                    self.counter += 1
                                if self.counter == 4:
                                    self.layout[y, x] = 1
                                    break

        if np.all(self.old_layout == self.layout):
            self.change = False

        self.n_occupied()

        return

    def update_layout_part2(self):
        self.old_layout = np.copy(self.layout)
        self.bounds = np.shape(self.old_layout)

        for y, x in np.ndindex(self.old_layout.shape):
            if self.old_layout[y, x] == 1:
                self.layout[y, x] = 2
                for self.adjacent_y, self.adjacent_x in [(i, j) for i in [y-1, y, y+1] for j in [x-1, x, x+1]]:
                    if not (self.adjacent_y == y and self.adjacent_x == x):
                        self.unit_vector = np.array([self.adjacent_y, self.adjacent_x]) - np.array([y, x])

                        while 0 <= self.adjacent_y < self.bounds[0] and 0 <= self.adjacent_x < self.bounds[1]:
                            if self.old_layout[self.adjacent_y, self.adjacent_x] == 2:
                                self.layout[y, x] = 1
                                break
                            elif self.old_layout[self.adjacent_y, self.adjacent_x] == 1:
                                break
                            elif self.old_layout[self.adjacent_y, self.adjacent_x] == 0:
                                self.adjacent_y += self.unit_vector[0]
                                self.adjacent_x += self.unit_vector[1]

            if self.old_layout[y, x] == 2:
                self.counter = 0
                for self.adjacent_y, self.adjacent_x in [(i, j) for i in [y-1, y, y+1] for j in [x-1, x, x+1]]:
                    if not (self.adjacent_y == y and self.adjacent_x == x):
                        self.unit_vector = np.array([self.adjacent_y, self.adjacent_x]) - np.array([y, x])
                        while 0 <= self.adjacent_y < self.bounds[0] and 0 <= self.adjacent_x < self.bounds[1]:
                            if self.old_layout[self.adjacent_y, self.adjacent_x] == 2:
                                self.counter += 1
                                break
                            elif self.old_layout[self.adjacent_y, self.adjacent_x] == 1:
                                break
                            elif self.old_layout[self.adjacent_y, self.adjacent_x] == 0:
                                self.adjacent_y += self.unit_vector[0]
                                self.adjacent_x += self.unit_vector[1]
                        if self.counter == 5:
                            self.layout[y, x] = 1
                            break
        if np.all(self.old_layout == self.layout):
            self.change = False

        self.n_occupied()

        return

    def n_occupied(self):
        self.occupied_seats = (self.layout == 2).sum()
        return

# copy array else the both objects will share the array :( Took me way too long to find this bug. Remember that
# functions and objects all share the same namespace so be careful with this stuff.
seating_part1 = WaitingRoom(np.copy(input_data))
seating_part2 = WaitingRoom(np.copy(input_data))

while seating_part1.change:
    seating_part1.update_layout_part1()
answer1 = seating_part1.occupied_seats
print(f"Answer to problem 11 part 1: {answer1}")

while seating_part2.change:
    seating_part2.update_layout_part2()
answer2 = seating_part2.occupied_seats
print(f"Answer to problem 11 part 2: {answer2}")



