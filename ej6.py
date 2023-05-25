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

print("n-PokéBolas\tSoluciones distintas\tTodas las soluciones\tUna solución")
for n in range(1, 16):
    num_solutions, num_all_solutions, random_solution = solve_n_pokeballs(n)
    print(f"{n}\t\t{num_solutions}\t\t\t{num_all_solutions}\t\t\t\t{random_solution}")