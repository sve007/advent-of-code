import numpy as np

with open("input_problem3", "r") as file:
    input_data = file.read().split("\n")

data = np.array([np.array(list(i)) for i in input_data])


def find_most_common(data):

    data_transposed = np.transpose(data)
    data_transposed = data_transposed.astype(int)
    data_transposed = np.where(data_transposed == 0, -1, 1)
    most_common = np.where(np.sum(data_transposed, 1) >= 0, 1, 0)

    return most_common


# Part 1
most_common = find_most_common(data)
gamma = int("".join(most_common.astype(str)), 2)
epsilon = int("".join(np.where(most_common == 1, 0, 1).astype(str)), 2)
answer1 = gamma * epsilon

print(f"Answer to problem 3 part 1: {answer1}")

# Part 2
data_scrubber_oxygen = data_scrubber_carbon = data
i = 0

while np.shape(data_scrubber_oxygen)[0] != 1:
    mc = find_most_common(data_scrubber_oxygen)[i]
    valid = np.where(data_scrubber_oxygen[:, i] == str(mc), True, False)
    data_scrubber_oxygen = data_scrubber_oxygen[np.where(valid)]
    i += 1

oxygen = int("".join(data_scrubber_oxygen[0]), 2)

i = 0
while np.shape(data_scrubber_carbon)[0] != 1:
    mc = 1 if find_most_common(data_scrubber_carbon)[i] == 0 else 0
    valid = np.where(data_scrubber_carbon[:, i] == str(mc), True, False)
    data_scrubber_carbon = data_scrubber_carbon[np.where(valid)]
    i += 1

carbon = int("".join(data_scrubber_carbon[0]), 2)
answer2 = oxygen * carbon
print(f"Answer to problem 3 part 2: {answer2}")
