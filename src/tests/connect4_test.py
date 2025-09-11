import unittest
from app import Connect4

class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_make_move_successful_when_wanted_column_is_not_full(self):
        result = self.game.make_move(3, 1) # pelaaja tekee siirron keskimmäiseen sarakkeeseen

        wanted_board = [[0 for col in range(self.game.cols)]
                      for row in range(self.game.rows)]
        wanted_board[5][3] = 1

        self.assertEqual(result, True)
        self.assertEqual(self.game.board, wanted_board)

    def test_make_move_unsuccessful_when_wanted_column_is_full(self):
        self.game.make_move(3, 1)
        self.game.make_move(3, 2)
        self.game.make_move(3, 1)
        self.game.make_move(3, 2)
        self.game.make_move(3, 1)
        self.game.make_move(3, 2) # keskikolumni on nyt täynnä
        result = self.game.make_move(3, 1)

        wanted_board = [[0 for col in range(self.game.cols)]
                      for row in range(self.game.rows)]
        wanted_board[5][3] = 1
        wanted_board[4][3] = 2
        wanted_board[3][3] = 1
        wanted_board[2][3] = 2
        wanted_board[1][3] = 1
        wanted_board[0][3] = 2

        self.assertEqual(result, False)
        self.assertEqual(self.game.board, wanted_board)