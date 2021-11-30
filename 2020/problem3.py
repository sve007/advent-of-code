import numpy as np
import math

with open("input_problem3", "r") as file:
    input_data_tile = file.readlines()
# Base field
input_data_tile = [list(i.rstrip()) for i in input_data_tile]
def traverse_field(vx, vy):
    # Increase field in x direction
    ncopies = math.ceil(vx*np.shape(input_data_tile)[0]/np.shape(input_data_tile)[1])+1
    input_data = np.tile(input_data_tile, ncopies)

    # Trees are True, so True
    input_data_bool = np.where(input_data == '.', False, True)
    x, y = 0, 0
    ntrees = 0

    # Traverse the field
    while y < np.shape(input_data_tile)[0]:
        if input_data_bool[y,x] == True:
            # We hit a tree
            ntrees = ntrees + 1
        y = y + vy
        x = x + vx
    return ntrees

if __name__ == "__main__":
    answer1 = traverse_field(3,1)
    print(f"Answer to problem 3 part 1: {answer1}")

    v = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    answer_list = []
    for vs in v:
        answer_list.append(traverse_field(vs[0], vs[1]))
    answer2 = np.prod(answer_list)
    print(f"Answer to problem 3 part 2: {answer2}")
