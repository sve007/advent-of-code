with open("input_problem6", "r") as file:
    input_data = file.read().split("\n\n")

input_data1 = [i.replace("\n", "") for i in input_data]

answer1 = 0
for form in input_data1:
    unique_answers = len(set(list(form)))
    answer1 = answer1 + unique_answers

print(f"Answer to problem 6 part 1: {answer1}")

answer2 = 0
for form in input_data:
    form = form.split("\n")
    # print(form)
    sets = [set(list(i)) for i in form]
    # print(sets)
    q = set.intersection(*sets)
    # print(q)
    answer2 = answer2 + len(q)

print(f"Answer to problem 6 part 2: {answer2}")
