import time
#this function checks the guess number valid or not 
def isvalid(puzzle,guess,row,col):
    #checking the column for guess number
    #if the number is found returns false
    for i in range(0,9):
        if guess == puzzle[row][i]:
            return False
    #checking the row for guess number
    #if the number is found returns false
    for i in range(0,9):
        if guess == puzzle[i][col]:
            return False
    begin_row = (row//3)*3
    begin_col = (col//3)*3
    #checking the block for guess number
    #if the number is found returns false
    for i in range(begin_row, begin_row+3):
        for j in range(begin_col, begin_col+3):
            if guess == puzzle[i][j]:
                return False
    return True
#next_empty returns the coordinates of the next empty block

#the sudoku_solver solves sudoku from starting element

#this function returns the next element to be solved 
def next_empty(puzzle):
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j]==0:
                return i,j
    return -1,-1

#sudoku_solver function calls recursively itself
#it solves the sudoku by using back_tracking
def sudoku_solver(puzzle):
    row,col = next_empty(puzzle)
    if row == -1:
        return True
    for guess in range(1,10):
        if isvalid(puzzle,guess,row,col):
            puzzle[row][col] = guess
            if sudoku_solver(puzzle):
                return True,puzzle
    puzzle[row][col] = 0
    return False
    
def read_sudoku():
    
    puzzle = []
    print("Enter the values in the sudoku")
    time.sleep(3)
    print("Enter '0' for empty values")
    time.sleep(3)
    for i in range(9):
        p = []
        
        print("Enter the",i+1,"row")
        for i in range(9):
            
            p.append(int(input()))
        puzzle.append(p)
    print(sudoku_solver(puzzle))
read_sudoku()
