import re

with open("input_data/input_problem04.txt") as f:
    data = f.read().split("\n")

# print(*data, sep="\n")
scores = []
for i, card in enumerate(data, start=1):
    numbers = re.search(r"\:\s+(\d.*)\|(.*)$", card)
    winning_numbers = numbers.group(1).split()
    card_numbers = numbers.group(2).split()
    foo = set.intersection(set(card_numbers), set(winning_numbers))
    if len(foo) > 0:
        scores.append(2**(len(foo)-1))

print(f"Answer to problem 4 part 1: {sum(scores)}")


# part 2

cards_multiple = [1]*len(data)
for i, card in enumerate(data):
    numbers = re.search(r"\:\s+(\d.*)\|(.*)$", card)
    winning_numbers = numbers.group(1).split()
    card_numbers = numbers.group(2).split()
    foo = set.intersection(set(card_numbers), set(winning_numbers))
    for j in range(1, len(foo)+1):
        try:
            cards_multiple[i+j] += 1*cards_multiple[i]
        except IndexError as e:
            continue

print(f"Answer to problem 4 part 1: {sum(cards_multiple)}")
