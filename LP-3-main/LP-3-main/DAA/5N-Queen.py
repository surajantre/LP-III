def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(board, row, n):
    if row == n:
        # All queens are placed, add the board to solutions
        solutions.append([row[:] for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0

def print_solution(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

if __name__ == "__main__":
    n = 8  # Change this to the desired board size
    solutions = []
    
    # Initialize the board
    board = [[0] * n for _ in range(n)]
    
    # Place the first queen in the first row (you can change the position if desired)
    board[0][0] = 1
    
    # Start the recursive backtracking to place the remaining queens
    solve_nqueens(board, 1, n)
    
    if solutions:
        print(f"Solutions for {n}-Queens:")
        for solution in solutions:
            print_solution(solution)
    else:
        print(f"No solution found for {n}-Queens.")
