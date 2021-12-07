import numpy as np

with open("input_data/input_problem07", "r") as file:
    input_crabs = np.array([int(i) for i in file.read().split(",")])


def totfuel_part1(crabs):
    totfuel_old = np.inf

    for i, _ in enumerate(crabs):
        centroid = abs(crabs - i)
        totfuel = sum(centroid)
        if totfuel > totfuel_old:
            break
        totfuel_old = totfuel

    return totfuel


def totfuel_part2(crabs):
    totfuel_old = np.inf

    for i, _ in enumerate(crabs):
        centroid = abs(crabs - i)
        totfuel = sum(centroid*(centroid + 1)/2)
        if totfuel > totfuel_old:
            break
        totfuel_old = totfuel

    return int(totfuel)


if __name__ == "__main__":

    answer1 = totfuel_part1(input_crabs)
    answer2 = totfuel_part2(input_crabs)
    print(f"Answer to problem 7 part 1: {answer1}")
    print(f"Answer to problem 7 part 2: {answer2}")
