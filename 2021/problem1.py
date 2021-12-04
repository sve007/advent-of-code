with open("input_data/input_problem1", "r") as file:
    input_data = file.readlines()
input_data = [int(i.rstrip('\n')) for i in input_data]

increases1 = [(True if (d > input_data[i-1]) else False) for i, d in enumerate(input_data)]
increases1[0] = False
answer1 = sum(increases1)

print(f"The answer to problem 1 part 1 is: {answer1}")
increases2 = [(True if sum((input_data[i:i+3])) > sum(input_data[i-1:i+2]) else False) for i in range(len(input_data))]
increases2[0] = False
# print(input_data)
# print(increases)
answer2 = sum(increases2)

print(f"The answer to problem 1 part 2 is: {answer2}")