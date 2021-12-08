def find_uniques(digits):
    for i in digits:
        if len(i) == 2:
            one = i
        elif len(i) == 3:
            seven = i
        elif len(i) == 4:
            four = i
        elif len(i) == 7:
            eight = i
        else:
            continue
    return one, four, seven, eight


def find_three(digits, seven):
    for i in digits:
        if len(i) == 5:
            overlap = set(i).difference(set(seven))
            if len(overlap) == 2:
                three = i
        # if len(i) == 6:
        #     overlap = set(i).difference(set(seven))
        #     if len(overlap) == 3:
        #         zero = i
    return three


def find_zero_six_nine(digits, four, seven):
    zero = six = nine = None
    for d in digits:
        if len(d) == 6:
            diff4 = list(set(four).difference(set(d)))
            diff7 = list(set(seven).difference(set(d)))
            if len(diff4) == 0:
                nine = d
            elif len(diff7) == 0:
                zero = d
            else:
                six = d

    return zero, six, nine


def find_two_five(digits, three, six):
    two = five = None
    for d in digits:
        if len(d) == 5:
            diff = list(set(six).difference(set(d)))
            if len(diff) == 1:
                five = d
            elif len(diff) == 2 and d != three:
                two = d
    return two, five


with open("input_data/input_problem08") as f:
    input_data = [i.split(" | ") for i in f.read().split('\n')]

for i, element in enumerate(input_data):
    input_data[i][0] = element[0].split(" ")
    input_data[i][1] = element[1].split(" ")


# Part 1
n = 0
for output in input_data:
    for i in output[1]:
        if len(i) in [2, 3, 4, 7]:
            n += 1
answer1 = n

# part 2
results = []
for line in input_data:
    one, four, seven, eight = find_uniques(line[0])
    three = find_three(line[0], seven)
    zero, six, nine = find_zero_six_nine(line[0], four, seven)
    two, five = find_two_five(line[0], three, six)
    numbers_ = zero, one, two, three, four, five, six, seven, eight, nine
    translation = [[i, number] for i, number in enumerate(numbers_)]

    tot = ""
    for n in line[1]:
        for i, number in translation:
            if set(n) == set(number):
                tot += str(i)
    results.append(tot)

answer2 = sum([int(i) for i in results])

print(f"Answer to problem 8 part 1: {answer1}")
print(f"Answer to problem 8 part 2: {answer2}")