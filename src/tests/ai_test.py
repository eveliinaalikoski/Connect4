import unittest
from ai import AI
from app import Connect4
from math import inf


class TestAI(unittest.TestCase):
    def setUp(self):
        self.ai = AI()
        self.game = Connect4(root=None)

        self.empty_board = [[0 for col in range(self.ai.cols)]
                            for row in range(self.ai.rows)]

    def test_winning_move_with_empty_board(self):
        gameboard = self.empty_board
        
        result = self.ai.winning_move(gameboard, 5, 3)

        self.assertEqual(result, False)
    
    def test_winning_move_with_no_win(self):
        gameboard = self.empty_board
        gameboard[5][2] = 1
        result = self.ai.winning_move(gameboard, 5, 2)

        self.assertEqual(result, False)

    def test_winning_move_with_horizontal_win(self):
        gameboard = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 5, 5, 0, 0, 0],
                     [0, 5, 1, 1, 1, 1, 0]]

        result = self.ai.winning_move(gameboard, 5, 5)

        self.assertEqual(result, True)

    def test_winning_move_with_vertical_win(self):
        gameboard = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 5, 0, 0, 0],
                     [1, 0, 5, 5, 0, 0, 0]]

        result = self.ai.winning_move(gameboard, 2, 0)

        self.assertEqual(result, True)

    def test_winning_move_with_up_diagonal_win(self):
        gameboard = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 5, 0],
                     [0, 0, 0, 0, 5, 1, 0],
                     [0, 0, 0, 5, 1, 1, 0],
                     [0, 0, 5, 5, 1, 1, 0]]

        result = self.ai.winning_move(gameboard, 2, 5)

        self.assertEqual(result, True)

    def test_winning_move_with_down_diagonal_win(self):
        gameboard = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 5, 1, 0, 0, 0],
                     [0, 0, 5, 5, 1, 0, 0],
                     [0, 5, 1, 1, 5, 1, 0]]

        result = self.ai.winning_move(gameboard, 2, 2)

        self.assertEqual(result, True)

    def test_heuristic_value_with_one_move(self):
        gameboard = self.empty_board
        gameboard[5][3] = 1

        summa = -10-10-10-10-10-10-10

        score = self.ai.heuristic_value(gameboard)

        self.assertEqual(score, summa)
    
    def test_heuristic_value_with_partially_filled_board_pt1(self):
        gameboard = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 5, 0, 0, 0],
                     [0, 0, 0, 5, 5, 0, 0],
                     [0, 0, 0, 1, 5, 0, 0],
                     [0, 0, 1, 5, 1, 1, 0],
                     [0, 0, 1, 1, 5, 1, 5]]
                
        summa = 10+10+10+10+10+30+30+30-10-30 # vaaka
        summa += -30-10+30-30-10+10 # pysty
        summa += 10+10+10+10+10+30-30 # yläviisto
        summa += 30+30+30-50-30-10+30+10-30 # alaviisto

        score = self.ai.heuristic_value(gameboard)

        self.assertEqual(score, summa)
    
    def test_heuristic_value_with_partially_filled_board_pt2(self):
        gameboard = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 5, 0, 1, 0, 0],
                     [0, 0, 1, 0, 5, 0, 0],
                     [0, 0, 1, 0, 5, 0, 0],
                     [0, 1, 5, 1, 5, 0, 5]]
        
        summa = -10-10-10+10-10-10+10-10+10 # vaaka
        summa += -10-10+10 # pysty
        summa += -10+10+10-10-10-10-50-30-10+30+10 # yläviisto
        summa += -10-10+30+30+30+10-10-30 # alaviisto

        score = self.ai.heuristic_value(gameboard)

        self.assertEqual(score, summa)
    
    def test_heuristic_value_with_partially_filled_board_pt3(self):
        gameboard = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 5, 5, 0, 0, 0],
                     [0, 1, 5, 5, 0, 0, 0],
                     [1, 5, 1, 1, 1, 5, 0]]

        summa = -10-10-10-10-40+30+30+30+10+30+10 # vaaka
        summa += -10-10+30+10-10+10 # pysty
        summa += -10-10+50+30+10+10-10 # yläviisto
        summa += -10-10-10-10-10+10+10+30+30 # alaviisto

        score = self.ai.heuristic_value(gameboard)

        self.assertEqual(score, summa)

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

    def test_minimax_with_a_win_in_exactly_five_moves(self):
        # valitaan pelitilanne, mistä löytyy varma voitto 5 siirrolla
        self.game.board = [[0, 0, 0, 0, 0, 0, 0],
                           [0, 5, 0, 5, 0, 0, 0],
                           [0, 1, 0, 1, 0, 0, 0],
                           [1, 5, 5, 5, 0, 0, 0],
                           [1, 1, 1, 5, 0, 0, 0],
                           [5, 1, 1, 1, 5, 0, 0]]

        last_move = None
        current_player = 5
        for __ in range(5):
            maximizing_player = True if current_player == 5 else False
            col, value = self.ai.minimax(
                self.game.board, 5, -inf, inf, maximizing_player, last_move)
            self.assertEqual(value, 100000)
            success, last_move = self.game.make_move(col, current_player)
            self.assertEqual(success, True)

            current_player = 1 if current_player == 5 else 5

        win = self.ai.winning_move(self.game.board, last_move[0], last_move[1])
        self.assertEqual(win, True)

    def test_minimax_with_a_draw(self):
        self.game.board = [[5, 1, 1, 1, 0, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5],
                           [1, 5, 1, 5, 1, 5, 1],
                           [1, 5, 1, 5, 1, 5, 1],
                           [5, 1, 5, 1, 5, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5]]
        __, value = self.ai.minimax(self.game.board, 1, -inf, inf, True, None)
        self.assertEqual(value, 0)
