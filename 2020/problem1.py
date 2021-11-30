import numpy as np

with open("/Users/sebastiaan/Documents/code_projects/advent-of-code/2020/input_problem1", "r") as file:
    input_data = file.readlines()
numbers = [int(i) for i in input_data]

def check_two_numbers(numbers, goal=2020):
    numbers = np.array(numbers)
    for i, n in enumerate(numbers):
        print(i)
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
    print(check_three_numbers(numbers))