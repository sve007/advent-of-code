with open("input_data/input_problem02.txt", "r") as file:
    input_data = file.read().split("\n")

# print(input_data)

def calc_score(tactic: str) -> int:
    moves_order = ['X', 'Y', 'Z']
    translation = {'A': 'X', 'B': 'Y', 'C': 'Z'}

    opponent_move = translation[tactic[0]]
    my_move = tactic[-1]

    score = moves_order.index(my_move) + 1

    if my_move == opponent_move:
        score += 3
    elif (moves_order.index(my_move) > moves_order.index(opponent_move)
          and (moves_order[moves_order.index(opponent_move) - 1] != my_move)) \
            or (moves_order[moves_order.index(my_move) - 1] == opponent_move):
        score += 6


    return score

tot_score = 0

for i in input_data:
    tot_score += calc_score(i)

print(f"Answer to problem 02 part 1: {tot_score}")

# part 2
moves_order = ['X', 'Y', 'Z']
translation = {'A': 'X', 'B': 'Y', 'C': 'Z'}
tot_score = 0
for i in input_data:
    if i[-1] == 'Y':
        move = i[:-1] + translation[i[0]]
    elif i[-1] == 'X':
        move = i[:-1] + moves_order[moves_order.index(translation[i[0]])-1]
    elif i[-1] == 'Z':
        try:
            move = i[:-1] + moves_order[moves_order.index(translation[i[0]])+1]
        except IndexError:
            move = i[:-1] + moves_order[0]
    tot_score += calc_score(move)

print(f"Answer to problem 02 part 2: {tot_score}")

