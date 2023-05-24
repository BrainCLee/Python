import random


def Initialize_board_9x9():
    row = []
    for i in range(0,9):
        row.append([i for i in range(1,10)])
    for i in range(1,9):
        for n in range(0,9):
            if(row[i][n] + row[i-1][0] < 10):
                row[i][n] = row[i][n] + row[i-1][0]
            
            else:
                row[i][n] = row[i][n] + row[i-1][0] - 9

    return row

def Shuffle_ribbons_9x9(board):
    top = board[:3]
    mid = board[3:6]
    bottom = board[6:]
    random.shuffle(top)
    random.shuffle(mid)
    random.shuffle(bottom)
    return top + mid + bottom


def Transpose_9x9(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])

    return transposed

def Create_solution_board_9x9():
    board = Initialize_board_9x9()
    board = Shuffle_ribbons_9x9(board)
    board = Transpose_9x9(board)
    board = Shuffle_ribbons_9x9(board)
    board = Transpose_9x9(board)
    return board

def copy_board(board):
    board_clone = []
    for row in board :
        board_clone.append(row[:])
    return board_clone

def get_level():
    print("Enter Your Level.")
    level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    while level not in ("1","2","3"):
        level = input("Beginner=1, Intermediate=2, Advanced=3: ")
    if level == "1":
        return 51
    elif level == "2":
        return 58
    else:
        return 64

def make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,8)
        j = random.randint(0,8)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
    return board

def show_board(board):
    for row in board:
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

def get_integer(message,i,j):
    digit = input(message)
    while not (digit.isdigit() and i <= int(digit) <= j):
        digit = input(message)
    return int(digit)

def sudoku_mini():
    solution_board = Create_solution_board_9x9()
    puzzle_board = copy_board(solution_board)
    no_of_holes = get_level()
    puzzle_board = make_holes(puzzle_board, no_of_holes)
    show_board(puzzle_board)
    while no_of_holes > 0:
        i = get_integer("Row#(1,2,3,4,5,6,7,8,9): ",1,9) - 1
        j = get_integer("Column#(1,2,3,4,5,6,7,8,9): ",1,9) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = get_integer("Number(1,2,3,4,5,6,7,8,9): ",1,9)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n,": Wrong number! Try again.")
    print("Well done! Come again.")

sudoku_mini()