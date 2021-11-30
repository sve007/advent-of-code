import numpy as np

with open("input_problem1", "r") as file:
    input_data = file.readlines()
numbers = [int(i) for i in input_data]

def check_two_numbers(numbers, goal=2020):
    numbers = np.array(numbers)
    for i, n in enumerate(numbers):
        check = numbers + n
        check = np.where(check == goal)
        if any(check):
            return(n, int(numbers[check]), n*int(numbers[check]))
        else:
            continue

def check_three_numbers(numbers, goal=2020):
    numbers = np.array(numbers)
    for i, n in enumerate(numbers):
        for j, m in enumerate(numbers):
            if i != j:
                check = numbers + n + m
                check = np.where(check == goal)
                if any(check):
                    return(n, m, int(numbers[check]), n*m*int(numbers[check]))
                else:
                    continue

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer_full1 = check_two_numbers(numbers)
    answer_full2 = check_three_numbers(numbers)
    answer1 = answer_full1[2]
    answer2 = answer_full2[3]
    print(f"Answer to problem 1 part 1: {answer1}")
    print(f"Answer to problem 1 part 2: {answer2}")