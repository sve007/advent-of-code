with open("input_data/input_problem04.txt") as f:
    input = f.read().split('\n')

pairs = []
for pair in input:
    pair = pair.split(',')
    pair = [pair[0].split('-'), pair[1].split('-')]
    pairs.append(pair)

tot1 = 0
for pair in pairs:
    range1 = range(int(pair[0][0]), int(pair[0][1])+1)
    range2 = range(int(pair[1][0]), int(pair[1][1])+1)
    if set(list(range1)).issubset(set(list(range2))):
        tot1 += 1
    elif set(list(range2)).issubset(set(list(range1))):
        tot1 += 1

print(f"Solution to problem 4 part 1: {tot1}")

# part 2

tot2 = 0
for pair in pairs:
    range1 = range(int(pair[0][0]), int(pair[0][1])+1)
    range2 = range(int(pair[1][0]), int(pair[1][1])+1)
    if set(list(range1)).intersection(set(list(range2))):
        tot2 += 1
    elif set(list(range2)).intersection(set(list(range1))):
        tot2 += 1

print(f"Solution to problem 4 part 2: {tot2}")
