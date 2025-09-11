import unittest
from ai import AI

class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI()

    def test_get_moves_with_empty_board(self):
        gameboard = [[0 for col in range(self.ai.cols)]
                      for row in range(self.ai.rows)]
    
        possible_moves = self.ai.get_moves(gameboard)

        correct_moves = [0, 1, 2, 3, 4, 5, 6]

        self.assertEqual(possible_moves, correct_moves)

    def test_get_moves_with_partially_filled_board(self):
        gameboard = [[0 for col in range(self.ai.cols)]
                      for row in range(self.ai.rows)]
        gameboard[5][3] = 1
        gameboard[5][2] = 2
        gameboard[4][3] = 1
        gameboard[3][3] = 2
    
        possible_moves = self.ai.get_moves(gameboard)

        correct_moves = [0, 1, 2, 3, 4, 5, 6]

        self.assertEqual(possible_moves, correct_moves)

    def test_get_moves_with_full_board(self):
        gameboard = [[1 for col in range(self.ai.cols)]
                      for row in range(self.ai.rows)]
    
        possible_moves = self.ai.get_moves(gameboard)

        correct_moves = []

        self.assertEqual(possible_moves, correct_moves)

    def test_simulate_move_with_partially_filled_board(self):
        gameboard = [[0 for col in range(self.ai.cols)]
                     for row in range(self.ai.rows)]
        gameboard[5][3] = 1
        gameboard[5][2] = 2
        gameboard[4][3] = 1
        gameboard[3][3] = 2

        new_board = self.ai.simulate_move(gameboard, 2, False)

        correct_board = gameboard
        correct_board[4][2] = 1

        self.assertEqual(new_board, correct_board)


## TO DO johonkin valmiiksi empty board, partially filled board 
# ja full board, nii ei tarvi tehä aina testin alussa