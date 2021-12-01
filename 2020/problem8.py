import copy


def run_program(program_code, i=0, a=0):
    passed_indices = []
    executed = False
    while i not in passed_indices:
        if i == len(program_code):
            executed = True
            print('Program completed!')
            return a, executed
        passed_indices.append(i)
        line = program_code[i]
        if line[0] == 'nop':
            i = i + 1
        elif line[0] == 'acc':
            a = a + int(line[1])
            i = i + 1
        elif line[0] == 'jmp':
            i = i + int(line[1])
    return a, executed


with open("input_problem8", "r") as file:
    input_data = file.read().split("\n")
input_data = [i.split(" ") for i in input_data]

# Part 1
answer1 = run_program(input_data)
print(f"Answer to problem 8 part 1: {answer1}")

# Part 2
for i, l in enumerate(input_data):
    input_data_variant = copy.deepcopy(input_data)
    if l[0] == 'nop':
        input_data_variant[i][0] = 'jmp'
    elif l[0] == 'jmp':
        input_data_variant[i][0] = 'nop'
    answer2 = run_program(input_data_variant)
    if answer2[1]:
        break
print(f"Answer to problem 8 part 2: {answer2}")


