import numpy as np

with open("input_data/input_problem06", "r") as file:
    input_data = np.array([int(i) for i in file.read().split(",")])

def let_fish_mate(init_fish, maxdays):
    day = 0
    counts = np.bincount(input_data, minlength=9)
    while day < maxdays:
        zero_fish = counts[0]
        counts[0] = counts[1]
        counts[1] = counts[2]
        counts[2] = counts[3]
        counts[3] = counts[4]
        counts[4] = counts[5]
        counts[5] = counts[6]
        counts[6] = counts[7]
        counts[7] = counts[8]
        counts[8] = zero_fish
        counts[6] += zero_fish

        day += 1
    return counts

answer1 = let_fish_mate(init_fish=input_data, maxdays=80).sum()
print(f"Answer to problem 6 part 1: {answer1}")

answer2 = let_fish_mate(init_fish=input_data, maxdays=256).sum()
print(f"Answer to problem 6 part 2: {answer2}")