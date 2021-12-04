import math
import numpy as np

def binary_search(ticket, total_seats):
    seat_coordinate = None
    min, max = 0, total_seats

    for b in ticket:
        if max-min == 1:
            seat_coordinate = (max if b else min)
            break
        if b:
            min = math.ceil(min + (max - min)/2)
        else:
            max = max - math.ceil((max - min)/2)

    return seat_coordinate


with open("input_data/input_problem5", "r") as file:
    input_data = file.read().split("\n")

# Part 1
seats = list()
for ticket in input_data:
    ticket_row = list(ticket[0:7])
    ticket_row = [True if i == 'B' else False for i in ticket_row]
    ticket_column = list(ticket[7:])
    ticket_column = [True if i == 'R' else False for i in ticket_column]
    seat_row = binary_search(ticket_row, total_seats=127)
    seat_column = binary_search(ticket_column, total_seats=7)
    seat_id = seat_row*8 + seat_column
    seats.append(seat_id)
answer1 = max(seats)
print(f"Answer to problem 5 part 1: {answer1}")
seats.sort()

# Part 2
all_seats = {i for i in range(min(seats), max(seats))}
answer2 = int(list(all_seats.difference(set(seats)))[0])
print(f"Answer to problem 5 part 2: {answer2}")
