import re

def contains_colour(target, rules, searched_colours=None):
    if searched_colours is None:
        searched_colours = []
    searched_colours.append(target)
    # print(f"Searching {target}")
    tot_colour = 0
    for bag in rules.keys():
        if bag not in searched_colours:
            for b in rules[bag]:
                if b[1] == target:
                    tot_colour = tot_colour + 1
                    tot_colour = tot_colour + contains_colour(target=bag, rules=rules, searched_colours=searched_colours)

    # if tot_colour == 0:
        # print(f"{target} not in bag rules.")
    # print(f"Total different colors that can contain {target}: {tot_colour}")
    return tot_colour

def count_bags(target, rules):
    tot = 1
    for bag in rules.get(target):
        tot = tot + int(bag[0]) * count_bags(bag[1], rules)
    # print(f"{target} contains a total of {tot} bags.")
    return tot


# Process data
with open("input_data/input_problem7", "r") as file:
    input_data = file.read().split("\n")

input_data = [i.replace(" bags", "").replace(" bag", "").replace(" contain", "").replace(".", "").replace(",", "").replace(" ", "").replace("noother", "") for i in input_data]
regex_key = r"^(\D+)"
regex_conditions = r"(\d+)(\D+)"
rules = dict()
for bag in input_data:
    key = re.findall(pattern=regex_key, string=bag)
    rule = re.findall(pattern=regex_conditions, string=bag)
    rules.update([(key[0], rule)])

# Part 1
target_colour = "shinygold"
answer1 = contains_colour(target_colour, rules)
print(f"Answer to problem 7 part 1: {answer1}")
# Part 2
bag_values = dict()

answer2 = count_bags(target_colour, rules) - 1 # Don't count the shiny gold bag itself!
print(f"Answer to problem 7 part 2: {answer2}")
