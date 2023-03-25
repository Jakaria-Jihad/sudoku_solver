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
# puzzle = input_sudoku()
# # Solve the puzzle
# solution = solve_sudoku(puzzle)

# # Print the solution
# for row in solution:
#     print(row)
import tkinter as tk

class SudokuSolverApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Sudoku Solver")

        # Create the Sudoku input grid
        self.grid_entries = []
        for row in range(9):
            row_entries = []
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=("Arial", 16))
                entry.grid(row=row, column=col)
                row_entries.append(entry)
            self.grid_entries.append(row_entries)

        # Create the "Solve" button
        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=4)

        # Create the solution grid
        self.solution_entries = []
        for row in range(9):
            row_entries = []
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=("Arial", 16), state="readonly")
                entry.grid(row=row+10, column=col)
                row_entries.append(entry)
            self.solution_entries.append(row_entries)

    def solve(self):
        # Get the input grid values
        grid_values = []
        for row_entries in self.grid_entries:
            row_values = []
            for entry in row_entries:
                value = entry.get()
                if value == "":
                    row_values.append(0)
                else:
                    row_values.append(int(value))
            grid_values.append(row_values)

        # Solve the Sudoku puzzle
        solution = solve_sudoku(grid_values)

        # Display the solution grid
        for row, row_entries in enumerate(self.solution_entries):
            for col, entry in enumerate(row_entries):
                entry.configure(state="normal")
                entry.delete(0, tk.END)
                entry.insert(0, str(solution[row][col]))
                entry.configure(state="readonly")

    def run(self):
        self.root.mainloop()

# Create and run the Sudoku Solver app
app = SudokuSolverApp()
app.run()
