import random

def initialize_board_4x4():
    row = []
    row0 = [i for i in range(1,10)]
    for i in range(0,9):
        #row[i] = [n for n in range(1,10)]
        #for n in range(1, 10):
            
        row.append(row0)
    row1 = []
    random.shuffle(row0)
    row1 = row0[2:4] + row0[0:2]
    row2 = [row0[1], row0[0], row0[3], row0[2]]
    row3 = row2[2:4] + row2[0:2]
    return [row0, row1, row2, row3]

def gogo():
    row = []
    row0 = [i for i in range(1,10)]
    for i in range(0,9):
        row[i] = [n for n in range(1,10)]
    return row

def shuffle_ribbons(board):
    top = board[:2]
    bottom = board[2:]
    random.shuffle(top)
    random.shuffle(bottom)
    return top + bottom

def transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])

    return transposed

def create_solution_board_4x4():
    return transpose(shuffle_ribbons(transpose(shuffle_ribbons(initialize_board_4x4()))))

#bb = initialize_board_4x4()
print(create_solution_board_4x4())
print(gogo())
#print(transpose(bb))