with open("input_data/input_problem2", "r") as file:
    input_data = file.read().split("\n")
input_data = [i.split(" ") for i in input_data]

z = 0
x = 0

# Part 1
for l in input_data:
    if l[0] == "forward":
        x += int(l[1])
    elif l[0] == "down":
        z += int(l[1])
    elif l[0] == "up":
        z -= int(l[1])
print(x,z)
print(f"Answer to problem 2 part 1: {x*z}")

# Part 2
z = 0
x = 0
aim = 0
for l in input_data:
    if l[0] == "forward":
        x += int(l[1])
        z += int(l[1])*aim
    elif l[0] == "down":
        aim += int(l[1])
    elif l[0] == "up":
        aim -= int(l[1])

print(x, z)
print(f"Answer to problem 2 part 2: {x * z}")