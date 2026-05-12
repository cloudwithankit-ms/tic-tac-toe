import unittest

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        # Sample game state for tests
        self.empty_board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.winning_board_row = [["X", "X", "X"], ["", "", ""], ["O", "O", ""]]
        self.winning_board_col = [["X", "O", ""], ["X", "O", ""], ["X", "", ""]]
        self.winning_board_diag = [["X", "O", ""], ["", "X", "O"], ["", "", "X"]]
        self.draw_board = [["X", "O", "X"], ["X", "O", "O"], ["O", "X", "X"]]

    def check_winner(self, board):
        # Logic copied from the original game to test
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != "":
                return row[0]
        # Check columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
                return board[0][i]
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            return board[0][2]
        return None

    def test_winner_row(self):
        self.assertEqual(self.check_winner(self.winning_board_row), "X")

    def test_winner_col(self):
        self.assertEqual(self.check_winner(self.winning_board_col), "X")

    def test_winner_diag(self):
        self.assertEqual(self.check_winner(self.winning_board_diag), "X")

    def test_draw(self):
        self.assertIsNone(self.check_winner(self.draw_board))

    def test_empty_board(self):
        self.assertIsNone(self.check_winner(self.empty_board))

if __name__ == "__main__":
    unittest.main()