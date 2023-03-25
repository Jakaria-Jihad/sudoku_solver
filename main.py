def solve_sudoku(board):
    """
    Solves the given Sudoku puzzle using a recursive backtracking algorithm.
    """
    def is_valid(row, col, num):
        """
        Returns True if the given number can be placed in the given cell,
        False otherwise.
        """
        for i in range(9):
            # Check row and column for conflicts
            if board[row][i] == num or board[i][col] == num:
                return False
            # Check 3x3 box for conflicts
            box_row, box_col = 3 * (row // 3) + i // 3, 3 * (col // 3) + i % 3
            if board[box_row][box_col] == num:
                return False
        return True

    def backtrack():
        """
        Recursive function that tries to solve the Sudoku puzzle by guessing
        numbers and backtracking if necessary.
        """
        nonlocal solved
        if solved:
            return
        row, col = next_empty()
        if row is None:
            solved = True
            return
        for num in range(1, 10):
            if is_valid(row, col, num):
                board[row][col] = num
                backtrack()
                if solved:
                    return
                board[row][col] = 0

    def next_empty():
        """
        Returns the next empty cell in row-major order, or (None, None) if
        there are no more empty cells.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None, None

    solved = False
    backtrack()
    return board
def input_sudoku():
    """
    Prompts the user to enter a Sudoku puzzle as a 9x9 matrix.
    """
    board = []
    print("Enter the Sudoku puzzle as a 9x9 matrix, with empty cells represented by 0:")
    for row in range(9):
        while True:
            row_input = input(f"Enter row {row+1}: ")
            row_values = [int(c) for c in row_input if c.isdigit()]
            if len(row_values) == 9:
                board.append(row_values)
                break
            else:
                print("Invalid input. Please enter exactly 9 digits (0-9) for each row.")
    return board

# Example Sudoku puzzle
# puzzle = [
#     [0, 2, 0, 6, 0, 8, 0, 0, 0],
#     [5, 8, 0, 0, 0, 9, 7, 0, 0],
#     [0, 0, 0, 0, 4, 0, 0, 0, 0],
#     [3, 7, 0, 0, 0, 0, 5, 0, 0],
#     [6, 0, 0, 0, 0, 0, 0, 0, 4],
#     [0, 0, 8, 0, 0, 0, 0, 1, 3],
#     [0, 0, 0, 0, 2, 0, 0, 0, 0],
#     [0, 0, 9, 8, 0, 0, 0, 3, 6],
#     [0, 0, 0, 3, 0, 6, 0, 9, 0]
# ]
puzzle = input_sudoku()
# Solve the puzzle
solution = solve_sudoku(puzzle)

# Print the solution
for row in solution:
    print(row)
