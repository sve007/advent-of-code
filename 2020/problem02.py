# https://adventofcode.com/2020/day/2#part2
import re

# part 1
def convert_to_regex(string):
    string = string.split()
    nchar = "{"+string[0].replace("-",",")+'}'
    char = string[1]
    regexstr = f"^[^{char}]*(?:{char}[^{char}]*){nchar}$"
    return(regexstr)

def validate_passwd(passwd,regex):
    valid = re.fullmatch(pattern=regex, string=passwd)
    return(valid)

# part 2
def validate_passwd2(indices, char,passwd):

    min = int(indices[0])-1
    max = int(indices[1])-1

    if (passwd[min] == char) ^ (passwd[max] == char):
        return True
    return False

def find_indices(string):
    indices = re.findall(pattern="(\d+)", string=string)
    return(indices)

with open("input_data/input_problem2", "r") as file:
    input_data = file.readlines()

# part 1
input_data = [line.rstrip('\n') for line in input_data]
input_data = [i.split(": ") for i in input_data]
valid = [validate_passwd(i[1], convert_to_regex(i[0])) for i in input_data]
answer = sum([x is not None for x in valid])
print(f"Answer to problem 2 part 1: {answer}")

valid2 = [validate_passwd2(find_indices(i[0]), i[0][-1], i[1]) for i in input_data]
answer2 = sum(valid2)
print(f"Answer to problem 2 part 2: {answer2}")

