import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Game state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        # Create the game board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(
                    self.window, text="", font=("Helvetica", 24), height=2, width=5,
                    command=lambda r=row, c=col: self.make_move(r, c)
                )
                self.buttons[row][col].grid(row=row, column=col)

        # Reset button
        self.reset_button = tk.Button(
            self.window, text="Restart", font=("Helvetica", 14),
            command=self.reset_game
        )
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == "":  # If the cell is empty.
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                # Switch player turn
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_game(self):
        # Reset board state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        # Reset button texts
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    TicTacToe().run()
