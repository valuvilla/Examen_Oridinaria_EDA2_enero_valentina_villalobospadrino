import random

class Nodo:
    def __init__(self, valor, fila):
        self.valor = valor
        self.fila = fila
        self.siguiente = None

def solve_n_pokeballs(n):
    solutions = []
    all_solutions = []
    board = [None] * n

    def is_safe(row, col):
        nodo_actual = board[row]
        while nodo_actual is not None:
            if (
                nodo_actual.valor == col
                or nodo_actual.valor - nodo_actual.fila == col - row
                or nodo_actual.valor + nodo_actual.fila == col + row
            ):
                return False
            nodo_actual = nodo_actual.siguiente
        return True

    def backtrack(row):
        if row == n:
            solution = []
            nodo_actual = board[0]
            while nodo_actual is not None:
                solution.append(nodo_actual.valor)
                nodo_actual = nodo_actual.siguiente
            solutions.append(solution)
            all_solutions.append(solution)
        else:
            for col in range(n):
                if is_safe(row, col):
                    nodo = Nodo(col, row)
                    if board[row] is None:
                        board[row] = nodo
                    else:
                        nodo_actual = board[row]
                        while nodo_actual.siguiente is not None:
                            nodo_actual = nodo_actual.siguiente
                        nodo_actual.siguiente = nodo
                    backtrack(row + 1)
                    if board[row] == nodo:
                        board[row] = None
                    else:
                        nodo_actual = board[row]
                        while nodo_actual.siguiente != nodo:
                            nodo_actual = nodo_actual.siguiente
                        nodo_actual.siguiente = None

    backtrack(0)

    num_solutions = len(solutions)
    num_all_solutions = len(all_solutions)

    if num_solutions > 0:
        random_solution = random.choice(solutions)
    else:
        random_solution = []

    return num_solutions, num_all_solutions, random_solution

print("n-PokéBolas\tSoluciones distintas\tTodas las soluciones\tUna solución")
for n in range(1, 16):
    num_solutions, num_all_solutions, random_solution = solve_n_pokeballs(n)
    print(f"{n}\t\t{num_solutions}\t\t\t{num_all_solutions}\t\t\t\t{random_solution}")
