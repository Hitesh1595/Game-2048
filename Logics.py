import random
# create a grid of 4x4 for 2048 game
# 0 represent empty space in a grid
def start_game():
    mat = [[0] * 4 for i in range(4)]
    return mat


# add 2 in a 2048
def add_new_2(mat):
    # generate a ramdom place in a grid for 2
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    # if place is not empty
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    # add 2 to a new empty place
    mat[r][c] = random.choice([2,4])


def get_current_state(mat):
    # any where 2048 present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    # any where empty space is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
                
    # for every row and column except last row and last column
    # two same value in row or col
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i + 1][j]:
                return 'GAME NOT OVER'
    
    # for last row
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
             return 'GAME NOT OVER'
    
    # for last column
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
             return 'GAME NOT OVER'

    return 'LOST'


# for compress, all same value came at one side of a grid
def compress(mat):
    # for check if change occur or not
    changed = False
    new_mat = [[0] * 4 for i in range(4)]

    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                # insert in a new matrix(new_mat),row wise
                new_mat[i][pos] = mat[i][j]
                # if any position can not changed........
                if j != pos:
                    changed = True
                pos += 1
    return new_mat,changed

def merge(mat):
    # check if change occur or not
    changed = False
    for i in range(4):
        # column -1 
        for j in range(4-1):
            # if two row value same then change occur 
            # as well as these value add.......
            if mat[i][j] == mat[i][j + 1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                changed = True
    return mat,changed

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4 - j - 1])
            
    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])

    return new_mat

# base case all logic are acc to left
def move_left(grid):
    new_grid,changed1 = compress(grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,_ = compress(new_grid)
    return new_grid,changed

def move_right(grid):
    reversed_grid = reverse(grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,_ = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid,changed

                
def move_up(grid):
    transpose_grid = transpose(grid)
    new_grid,changed1 = compress(transpose_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,_ = compress(new_grid)
    final_grid = transpose(new_grid)
    return final_grid,changed

def move_down(grid):
    transpose_grid = transpose(grid)
    reversed_grid = reverse(transpose_grid)
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,_ = compress(new_grid)
    final_reversed_grid = reverse(new_grid)
    final_grid = transpose(final_reversed_grid)
    return final_grid,changed

