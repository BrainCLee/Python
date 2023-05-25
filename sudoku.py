import random


def Initialize_board():
    row = []
    for i in range(0,9):
        row.append([i for i in range(1,10)])
    for i in range(1,9):
        for n in range(0,9):
            if(i < 3):
                if(row[i][n] + row[i-1][0] + 2 < 10):
                    row[i][n] = row[i][n] + row[i-1][0] + 2
            
                else:
                    row[i][n] = row[i][n] + row[i-1][0] + 2 - 9
            else:
                if(row[i-3][n] + 1 < 10):
                    row[i][n] = row[i-3][n] + 1
            
                else:
                    row[i][n] = row[i-3][n] + 1 - 9

    return row

def Shuffle_ribbons(board):
    top = board[:3]
    mid = board[3:6]
    bottom = board[6:]
    random.shuffle(top)
    random.shuffle(mid)
    random.shuffle(bottom)
    return top + mid + bottom


def Transpose(board):
    transposed = []
    size = len(board)
    for _ in range(size):
        transposed.append([])
    
    for row in board:
        for i in range(size):
            transposed[i].append(row[i])

    return transposed

def Create_solution_board():
    board = Initialize_board()
    board = Shuffle_ribbons(board)
    board = Transpose(board)
    board = Shuffle_ribbons(board)
    board = Transpose(board)
    return board

def Copy_board(board):
    board_clone = []
    for row in board :
        board_clone.append(row[:])
    return board_clone

def Get_level():
    print("Enter Your Level.")
    level = input("Beginner=1, Intermediate=2, Bachelor=3, Master=4, Doctor=5: ")
    while level not in ("1","2","3","4","5"):
        level = input("Beginner=1, Intermediate=2, Bachelor=3, Master=4, Doctor=5: ")
    if level == "1":
        return 36
    elif level == "2":
        return 43
    elif level == "3":
        return 51
    elif level == "4":
        return 58
    else:
        return 64

def Make_holes(board, no_of_holes):
    while no_of_holes > 0:
        i = random.randint(0,8)
        j = random.randint(0,8)
        if board[i][j] != 0:
            board[i][j] = 0
            no_of_holes -= 1
    return board

def Show_board(board):
    print("r/c 1 2 3 4 5 6 7 8 9", end = "\n\n")
    nprintColumn = 0
    for row in board:
        print(str(nprintColumn+1), end = "   ")
        nprintColumn += 1
        for entry in row:
            if entry == 0:
                print('.', end=' ')
            else:
                print(entry, end=' ')
        print()

def Get_integer(message,i,j):
    digit = input(message)
    while not (digit.isdigit() and i <= int(digit) <= j):
        digit = input(message)
    return int(digit)

def Sudoku():
    solution_board = Create_solution_board()
    puzzle_board = Copy_board(solution_board)
    no_of_holes = Get_level()
    puzzle_board = Make_holes(puzzle_board, no_of_holes)
    Show_board(puzzle_board)
    while no_of_holes > 0:
        i = Get_integer("Row#(1 ~ 9): ",1,9) - 1
        j = Get_integer("Column#(1 ~ 9): ",1,9) - 1
        if puzzle_board[i][j] != 0:
            print("Not empty!")
            continue
        n = Get_integer("Number(1 ~ 9): ",1,9)
        if n == solution_board[i][j]:
            puzzle_board[i][j] = solution_board[i][j]
            Show_board(puzzle_board)
            no_of_holes -= 1
        else:
            print(n,": Wrong number! Try again.")
    print("Well done! Come again.")

Sudoku()