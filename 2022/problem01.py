with open("input_data/input_problem01.txt", "r") as file:
    input_data = file.read().split("\n")

elves_cals = [[]]

j = 0

for i in input_data:
    if i == "":
        j += 1
        elves_cals.append([])
    else:
        elves_cals[j].append(int(i))

elves_cals_tot = [sum(e) for e in elves_cals]

answer1 = max(elves_cals_tot)

print(f"Answer to problem 1 part 1: {answer1}")

k = 0
answer2 = 0
while k < 3:
    max_val = max(elves_cals_tot)
    elves_cals_tot.pop(elves_cals_tot.index(max_val))
    answer2 += max_val
    k += 1

print(f"Answer to problem 1 part 2: {answer2}")
