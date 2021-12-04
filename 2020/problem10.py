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