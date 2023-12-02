import re


def replace_str(s, reverse=False):
    s = s.group()
    if reverse:
        s = s[::-1]
    digits_int = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                  "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    try:
        d = int(s)
    except ValueError:
        d = digits_int.get(s)
    return d


def first_and_last(line: str, part1: bool = True) -> str:
    if part1:
        f = re.search(r"\d", line).group()
        l = re.search(r"\d", line[::-1]).group()

    else:
        digits_str = re.compile("one|two|three|four|five|six|seven|eight|nine")
        digits_str_reversed = re.compile("one|two|three|four|five|six|seven|eight|nine"[::-1])

        first = re.sub(digits_str, replace_str, line, count=1)
        last = re.sub(digits_str_reversed, lambda x: replace_str(x, reverse=True), line[::-1], count=1)[::-1]

        f = re.search(r"\d", first).group()
        l = re.search(r"\d", last[::-1]).group()

    answer = f + l

    return answer


with open("input_data/input_problem01.txt") as f:
    data = f.read().split("\n")


answer1 = 0
for line in data:
    answer1 += int(first_and_last(line, part1=True))
print(f"Answer to part 1: {answer1}")

answer2 = 0
for line in data:
    answer2 += int(first_and_last(line, part1=False))
print(f"Answer to part 2: {answer2}")
