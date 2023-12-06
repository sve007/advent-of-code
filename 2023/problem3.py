import regex
import numpy as np


def check_parts_indicator(ind: str) -> bool:
    if ind != "." and ind != "":
        return True
    return False


def check_vertical(upper=None, lower=None) -> bool:
    if upper:
        if any(char != "." for char in upper):
            return True
    if lower:
        if any(char != "." for char in lower):
            return True
    return False
#


with open("input_data/input_problem03.txt") as f:
    data = f.read().split("\n")

# Create dummy '.' characters all around the input data
data = ["." + d + "." for d in data]
length = len(data[0])
data = [length*"."] + data + [length*"."]

parts = []
part_re = regex.compile(r"([\D])(\d+)([\D])")
for i, line in enumerate(data):
    iterator = regex.finditer(part_re, line, overlapped=True)
    for it in iterator:
        if check_parts_indicator(it.group(1)) or check_parts_indicator(it.group(3)):
            parts.append(int(it.group(2)))
        else:
            if check_vertical(lower=data[i+1][it.start():it.end()],
                              upper=data[i-1][it.start():it.end()]):
                parts.append(int(it.group(2)))

answer1 = sum(parts)
print(f"Answer to part 1: {answer1}")

answer2 = 0
for i, line in enumerate(data):
    for gear in regex.finditer(r"\*", line):
        numbers = []
        horizontal_gears = regex.search(r"(\d*)\*(\d*)", line[gear.start()-3:gear.start()+4]).group(1, 2)
        numbers.append(horizontal_gears[0])
        numbers.append(horizontal_gears[1])
        # lines above and below gear
        for g in regex.finditer(r"(\d+)", data[i-1][gear.start()-3:gear.start()+4]):
            if 2 <= g.start() < 5:
                numbers.append(g.group())
            elif 2 <= g.end()-1 < 5:
                numbers.append(g.group())
        for g in regex.finditer(r"(\d+)", data[i+1][gear.start()-3:gear.start()+4]):
            if 2 <= g.start() < 5:
                numbers.append(g.group())
            elif 2 <= g.end()-1 < 5:
                numbers.append(g.group())
        numbers = [int(n) for n in numbers if n != ""]
        if len(numbers) == 2:
            answer2 += np.product(numbers)

print(f"Answer to part 2: {answer2}")
