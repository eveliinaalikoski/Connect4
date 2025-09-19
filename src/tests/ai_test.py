import unittest
from ai import AI

class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI()

        self.empty_board = [[0 for col in range(self.ai.cols)]
                       for row in range(self.ai.rows)]

    def test_winning_move_with_no_win(self):
        gameboard = self.empty_board
        gameboard[5][2] = 1
        result = self.ai.winning_move(gameboard, 5, 2)

        self.assertEqual(result, False)

    def test_winning_move_horizontal_win(self):
        gameboard = self.empty_board
        gameboard[5][2] = 1
        gameboard[4][2] = 5
        gameboard[5][3] = 1
        gameboard[5][1] = 5
        gameboard[5][4] = 1
        gameboard[4][3] = 5
        gameboard[5][5] = 1

        result = self.ai.winning_move(gameboard, 5, 6)

        self.assertEqual(result, True)

    def test_winning_move_vertical_win(self):
        gameboard = self.empty_board
        gameboard[5][0] = 1
        gameboard[5][3] = 5
        gameboard[4][0] = 1
        gameboard[5][2] = 5
        gameboard[3][0] = 1
        gameboard[5][3] = 5
        gameboard[2][0] = 1

        result = self.ai.winning_move(gameboard, 2, 0)

        self.assertEqual(result, True)

    def test_heuristic_value_with_one_move(self):
        gameboard = self.empty_board
        gameboard[5][3] = 1
        
        score = self.ai.heuristic_value(gameboard)

        self.assertEqual(score, -70)

    def test_get_moves_with_empty_board(self):
        possible_moves = self.ai.get_moves(self.empty_board)

        correct_moves = [3, 2, 4, 1, 5, 0, 6]

        self.assertEqual(possible_moves, correct_moves)

    def test_get_moves_with_partially_filled_board(self):
        gameboard = self.empty_board
        gameboard[5][3] = 1
        gameboard[5][2] = 5
        gameboard[4][3] = 1
        gameboard[3][3] = 5
    
        possible_moves = self.ai.get_moves(gameboard)

        correct_moves = [3, 2, 4, 1, 5, 0, 6]

        self.assertEqual(possible_moves, correct_moves)

    def test_get_moves_with_full_board(self):
        gameboard = [[1 for col in range(self.ai.cols)]
                      for row in range(self.ai.rows)]
    
        possible_moves = self.ai.get_moves(gameboard)

        correct_moves = []

        self.assertEqual(possible_moves, correct_moves)

    def test_simulate_move_with_partially_filled_board(self):
        gameboard = self.empty_board
        gameboard[5][3] = 1
        gameboard[5][2] = 5
        gameboard[4][3] = 1
        gameboard[3][3] = 5

        new_board = self.ai.simulate_move(gameboard, 2, False)

        correct_board = gameboard
        correct_board[4][2] = 1

        self.assertEqual(new_board, (correct_board, (4, 2)))


## TO DO johonkin valmiiksi empty board, partially filled board 
# ja full board, nii ei tarvi tehä aina testin alussa