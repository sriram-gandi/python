def isvalid(puzzle,guess,row,col):
    for i in range(0,9):
        if guess == puzzle[row][i]:
            return False
    for i in range(0,9):
        if guess == puzzle[i][col]:
            return False
    begin_row = (row//3)*3
    begin_col = (col//3)*3
    for i in range(begin_row, begin_row+3):
        for j in range(begin_col, begin_col+3):
            if guess == puzzle[i][j]:
                return False
    return True
    
def next_empty(puzzle):
    for i in range(0,9):
        for j in range(0,9):
            if puzzle[i][j]==0:
                return i,j
    return -1,-1

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
    
puzzle = [[4,0,0,0,0,8,0,0,0],[0,0,0,0,9,1,0,8,0],[0,8,6,5,0,2,0,3,0],[0,2,0,4,0,0,9,0,0],[0,1,0,2,0,0,0,0,6],[3,6,7,0,5,9,0,0,0],[0,0,0,0,0,5,0,0,0],[7,0,0,8,0,0,0,2,4],[2,0,0,9,3,0,0,7,0]]
            
    
print(sudoku_solver(puzzle))
