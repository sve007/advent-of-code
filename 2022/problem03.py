with open("input_data/input_problem03.txt") as f:
    input = f.read().split("\n")

def char_to_int(char: str) -> int:
    if char.islower():
        val = ord(char) - 96
    else:
        val = ord(char) - 64 + 26
    return val

tot_val1 = 0
for b in input:
    b = [b[:int(len(b)/2)], b[int(len(b)/2):]]
    item = list(set(list(b[0])).intersection(set(list(b[1]))))[0]
    tot_val1 += char_to_int(item)

print(f"Answer to problem 3 part 1: {tot_val1}")

#part 2
groups = [input[i: i+3] for i in range(0, len(input), 3)]

tot_val2 = 0
for g in groups:
    item = list(set(list(g[0])).intersection(set(list(g[1])), set(list(g[2]))))[0]
    tot_val2 += char_to_int(item)

print(f"Answer to problem 3 part 2: {tot_val2}")
