import random

def solve_n_pokeballs(n):
    solutions = []
    all_solutions = []
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            if (
                board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row
            ):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
        
    backtrack(0)


    for solution in solutions:
        all_solutions.append(solution)

    return all_solutions


