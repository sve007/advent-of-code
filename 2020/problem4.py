# Read and clean data
import numpy as np
import re

with open("input_problem4", "r") as file:
    input_data = file.read().split("\n\n")

input_data = [i.replace("\n", " ") for i in input_data]
input_data = [i.split(" ") for i in input_data]

for i, passport in enumerate(input_data):
    input_data[i] = [j.split(":") for j in passport]
input_data = [dict(i) for i in input_data]

optional_code = "cid"
required_codes = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid_pp = list()
for p in input_data:
    key_set = set(p.keys())
    valid = required_codes.issubset(key_set)
    valid_pp.append(valid)
answer1 = sum(valid_pp)
print(f"Answer to problem 4 part 1: {answer1}")

# Part 2
byr = [1920, 2002]
iyr = [2010, 2020]
eyr = [2020, 2030]
hgt_cm = [150, 193]
hgt_in = [59, 76]
hcl = r"^#[0-9a-f]{6}$"
ecl = ["amb", "blu", "brn", 'gry', "grn", "hzl", "oth"]
pid = r"^\d{9}$"

input_data2 = np.array(input_data)[valid_pp]
valid_pp2 = list()
for pp in input_data2:
    checks = list()
    checks.append(byr[0] <= int(pp.get("byr")) <= byr[1])
    checks.append(iyr[0] <= int(pp.get("iyr")) <= iyr[1])
    checks.append(eyr[0] <= int(pp.get("eyr")) <= eyr[1])
    checks.append(re.match(pattern=hcl, string=p.get("hcl")))
    checks.append(re.match(pattern=pid, string=p.get("pid")))
    checks.append(pp.get("ecl") in ecl)
    if re.match(pattern=r"\d+[(cm)(in)]", string = pp.get("hgt")):
        if re.findall(pattern=r"cm$", string=pp.get("hgt")):
            # print('cm!')
            # print(re.findall(pattern = "\d+", string = pp.get("hgt"))[0])
            checks.append(hgt_cm[0] < int(re.findall(pattern=r"\d+", string=pp.get("hgt"))[0]) < hgt_cm[1])
        elif re.findall(pattern="in$", string=pp.get("hgt")):
            checks.append(hgt_in[0] < int(re.findall(pattern=r"\d+", string=pp.get("hgt"))[0]) < hgt_in[1])
        else:
            checks.append(False)
    else:
        checks.append(False)
    valid_pp2.append(all(checks))

answer2 = sum(valid_pp2)
print(f"Answer to problem 4 part 2: {answer2}")

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
