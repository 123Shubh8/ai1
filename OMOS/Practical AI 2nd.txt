def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        
    i, j = row -1, col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1    
    
    i, j = row - 1, col + 1    
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1
        
    return True
    
    
def solution_queen(board, row):
    if row >= len(board):
        return True
    
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            if solution_queen(board, row + 1):
                return True
            board[row] = -1
        
    return False


def print_solution(board):
    for row in board:
        link = ['Q' if i == row else '.' for i in range(len(board))]
        print(' '.join(link))
        
def eight_queen():
    n = 8
    board = [-1] * n
    
    if solution_queen(board, 0):
        print_solution(board)
    else:
        print(False)
        
eight_queen()


