import re

with open("input_data/input_problem02.txt") as f:
    data = f.read().split("\n")

limits = [12, 13, 14]
red = re.compile(r"(\d+)(?=\sred)")
green = re.compile(r"(\d+)(?=\sgreen)")
blue = re.compile(r"(\d+)(?=\sblue)")
color_counts = [red, green, blue]
answer1 = 0

game_number = re.compile(r"\d+")
# Part 1
for d in data:
    check = True
    n = re.search(game_number, d).group()
    for i, c in enumerate(color_counts):
        count = [int(x) for x in re.findall(c, d)]
        if any(x>limits[i] for x in count):
            check = False
            break
    if check:
        answer1 += int(n)

print(f"Answer to part 1: {answer1}")

# Part 2
answer2 = 0
for d in data:
    check = True
    answer2_ = 1
    n = re.search(game_number, d).group()
    for i, c in enumerate(color_counts):
        count = [int(x) for x in re.findall(c, d)]
        answer2_ = max(count)*answer2_
    answer2 += answer2_

print(f"Answer to part 2: {answer2}")
