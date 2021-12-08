import numpy as np

with open("input_data/input_problem10", "r") as file:
    input_data = file.read().split("\n")
input_data = [int(i) for i in input_data]
input_data.sort()
input_data = [0] + input_data + [input_data[-1]+3]
joltage_diff = [a - input_data[i] for i, a in enumerate(input_data[1:])]

tot1 = 0
tot3 = 0

for j in joltage_diff:
    if j == 1:
        tot1 += 1
    elif j == 3:
        tot3 += 1

answer1 = tot1 * tot3
print(f"Answer to problem 10 part 1: {answer1}")

# Part 2


def ncombinations(n):
    tot = 1
    i = 1
    if n <= 2:
        yield tot
    while i <= n:
        if i > 5:
            tot = tot * 2
        elif i == 5:
            tot = 7
        elif i == 4:
            tot = 4
        elif i == 3:
            tot = 2

        yield tot
        i += 1


counter = 0
oneseq = []

for i in joltage_diff:
    if i == 1:
        counter += 1
    else:
        oneseq.append(counter)
        counter = 0

result = []
for o in oneseq:
    ncomb = list(ncombinations(o+1))[-1]
    result.append(ncomb)

answer2 = np.product([i for i in result if i > 0])
print(f"Answer to problem 10 part 2: {answer2}")
