import unittest
from app import Connect4

class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.game = Connect4(root=None)

    def test_make_move_successful_when_wanted_column_is_not_full(self):
        result = self.game.make_move(3, 1) # pelaaja tekee siirron keskimmäiseen sarakkeeseen

        wanted_board = [[0 for col in range(self.game.cols)]
                      for row in range(self.game.rows)]
        wanted_board[5][3] = 1

        self.assertEqual(result, (True, (5,3)))
        self.assertEqual(self.game.board, wanted_board)

    def test_make_move_unsuccessful_when_wanted_column_is_full(self):
        self.game.make_move(3, 1)
        self.game.make_move(3, 5)
        self.game.make_move(3, 1)
        self.game.make_move(3, 5)
        self.game.make_move(3, 1)
        self.game.make_move(3, 5) # keskikolumni on nyt täynnä
        result = self.game.make_move(3, 1)

        wanted_board = [[0 for col in range(self.game.cols)]
                      for row in range(self.game.rows)]
        wanted_board[5][3] = 1
        wanted_board[4][3] = 5
        wanted_board[3][3] = 1
        wanted_board[2][3] = 5
        wanted_board[1][3] = 1
        wanted_board[0][3] = 5

        self.assertEqual(result, (False, None))
        self.assertEqual(self.game.board, wanted_board)
    
    def test_full_board_returns_true_if_board_is_full(self):
        self.game.board = [[1 for col in range(self.game.cols)]
                           for row in range(self.game.rows)]
        
        result = self.game.full_board()

        self.assertEqual(result, True)

    def test_full_board_returns_false_if_board_is_not_full(self):
        self.game.board[5][3] = 1

        result = self.game.full_board()

        self.assertEqual(result, False)
