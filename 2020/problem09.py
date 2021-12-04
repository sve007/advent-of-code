def valid_number(n, options):
    valid = False
    for i in options:
        for j in options:
            if i != j:
                if i + j == n:
                    # print(i, j, n)
                    valid = True
                    return valid
    return valid


with open("input_data/input_problem9", "r") as file:
    input_data = file.read().split("\n")
input_data = [int(i) for i in input_data]

# Part 1
first_invalid_index = 0
preamble = 25
for i, number in enumerate(input_data[preamble:]):
    # print(i, number)
    # print(input_data[i:i + 25])
    valid_ = valid_number(number, input_data[i:i+preamble])
    if not valid_:
        first_invalid_index = i + preamble
        break
answer1 = input_data[first_invalid_index]
print(f"Answer to problem 9 part 1: {answer1}")

# Part 2
for i, number in enumerate(input_data):
    tot = 0
    if number != answer1:
        j = i
        while tot < answer1:
            tot += input_data[j]
            j += 1
        if tot == answer1:
            break

contiguous_set = input_data[i:j]
answer2 = min(contiguous_set) + max(contiguous_set)
print(f"Answer to problem 9 part 2: {answer2}")