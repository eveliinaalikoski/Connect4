import unittest
from app import Connect4
from unittest.mock import MagicMock
from types import SimpleNamespace


class TestConnect4(unittest.TestCase):
    def setUp(self):
        self.game = Connect4(root=None)
        self.game.ui = MagicMock()
        self.game.ai = MagicMock()

    def test_make_move_successful_when_wanted_column_is_not_full(self):
        # pelaaja tekee siirron keskimmäiseen sarakkeeseen
        result = self.game.make_move(3, 1)

        wanted_board = [[0 for _ in range(self.game.cols)]
                        for _ in range(self.game.rows)]
        wanted_board[5][3] = 1

        self.assertEqual(result, (True, (5, 3)))
        self.assertEqual(self.game.board, wanted_board)

    def test_make_move_unsuccessful_when_wanted_column_is_full(self):
        self.game.make_move(3, 1)
        self.game.make_move(3, 5)
        self.game.make_move(3, 1)
        self.game.make_move(3, 5)
        self.game.make_move(3, 1)
        self.game.make_move(3, 5)  # keskikolumni on nyt täynnä
        result = self.game.make_move(3, 1)

        wanted_board = [[0 for _ in range(self.game.cols)]
                        for _ in range(self.game.rows)]
        wanted_board[5][3] = 1
        wanted_board[4][3] = 5
        wanted_board[3][3] = 1
        wanted_board[2][3] = 5
        wanted_board[1][3] = 1
        wanted_board[0][3] = 5

        self.assertEqual(result, (False, None))
        self.assertEqual(self.game.board, wanted_board)

    def test_full_board_returns_true_if_board_is_full(self):
        self.game.board = [[1 for _ in range(self.game.cols)]
                           for _ in range(self.game.rows)]

        result = self.game.full_board()

        self.assertEqual(result, True)

    def test_full_board_returns_false_if_board_is_not_full(self):
        self.game.board[5][3] = 1

        result = self.game.full_board()

        self.assertEqual(result, False)

    def test_handle_click_with_empty_board(self):
        # annetaan mockatulle winning_movelle palautusarvo ja mockataan muut tarvittavat
        self.game.ai.winning_move.return_value = False
        self.game.ai_turn = MagicMock()
        self.game.root = MagicMock()
        event = SimpleNamespace(x=240)

        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(self.game.game_over, False)

        self.game.handle_click(event)

        self.game.ui.draw_board.assert_called_once()
        self.assertEqual(self.game.game_over, False)
        self.game.ui.toplabel.config.assert_not_called()
        self.assertEqual(self.game.current_player, 5)
        self.game.ai_turn.assert_called_once()

    def test_handle_click_with_player_win(self):
        self.game.ai.winning_move.return_value = True
        self.game.root = MagicMock()
        event = SimpleNamespace(x=320)

        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(self.game.game_over, False)

        self.game.handle_click(event)

        self.game.ui.draw_board.assert_called_once()
        self.assertEqual(self.game.game_over, True)
        self.game.ui.toplabel.config.assert_called_once()
        self.game.ui.toplabel.config.assert_called_with(text="You win!")

    def test_handle_click_with_full_board(self):
        self.game.ai.winning_move.return_value = False
        self.game.root = MagicMock()
        event = SimpleNamespace(x=170)

        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(self.game.game_over, False)

        self.game.board = [[5, 1, 0, 5, 1, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5],
                           [1, 5, 1, 5, 1, 5, 1],
                           [1, 5, 1, 5, 1, 5, 1],
                           [5, 1, 5, 1, 5, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5]]

        self.game.handle_click(event)

        self.game.ui.draw_board.assert_called_once()
        self.assertEqual(self.game.game_over, True)
        self.game.ui.toplabel.config.assert_called_once()
        self.game.ui.toplabel.config.assert_called_with(text="No more moves!")

    def test_handle_click_when_not_players_turn(self):
        self.game.current_player = 5
        event = SimpleNamespace(x=40)

        self.game.handle_click(event)

        self.assertEqual(self.game.current_player, 5)
        self.game.ui.draw_board.assert_not_called()

    def test_handle_click_when_clicked_a_full_column(self):
        event = SimpleNamespace(x=280)

        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(self.game.game_over, False)

        self.game.board = [[5, 1, 0, 1, 1, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5],
                           [1, 5, 1, 5, 1, 5, 1],
                           [1, 5, 1, 5, 1, 5, 1],
                           [5, 1, 5, 1, 5, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5]]

        self.game.handle_click(event)

        self.assertEqual(self.game.game_over, False)
        self.game.ui.draw_board.assert_not_called()

    def test_ai_turn_with_the_first_ai_move(self):
        # annetaan mockatuille ai funktioille palautusarvot
        self.game.ai.minimax.return_value = (3, 100)
        self.game.ai.winning_move.return_value = False

        self.game.ai_turn()

        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(self.game.game_over, False)
        self.game.ui.draw_board.assert_called_once()
        self.game.ui.toplabel.assert_not_called()

    def test_ai_turn_with_ai_win(self):
        self.game.ai.minimax.return_value = (3, 100000)
        self.game.ai.winning_move.return_value = True

        self.game.ai_turn()

        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(self.game.game_over, True)
        self.game.ui.draw_board.assert_called_once()
        self.game.ui.toplabel.config.assert_called_once()
        self.game.ui.toplabel.config.assert_called_with(text="AI wins!")

    def test_ai_turn_with_full_board(self):
        self.game.ai.minimax.return_value = (4, 0)
        self.game.ai.winning_move.return_value = False

        self.game.board = [[5, 1, 1, 1, 0, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5],
                           [1, 5, 1, 5, 1, 5, 1],
                           [1, 5, 1, 5, 1, 5, 1],
                           [5, 1, 5, 1, 5, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5]]

        self.game.ai_turn()

        self.assertEqual(self.game.current_player, 1)
        self.assertEqual(self.game.game_over, True)
        self.game.ui.draw_board.assert_called_once()
        self.game.ui.toplabel.config.assert_called_once()
        self.game.ui.toplabel.config.assert_called_with(text="No more moves!")

    def test_ai_turn_not_success(self):
        self.game.ai.minimax.return_value = (0, 0)

        self.game.board = [[5, 1, 1, 1, 0, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5],
                           [1, 5, 1, 5, 1, 5, 1],
                           [1, 5, 1, 5, 1, 5, 1],
                           [5, 1, 5, 1, 5, 1, 5],
                           [5, 1, 5, 1, 5, 1, 5]]

        self.game.ai_turn()

        self.assertEqual(self.game.game_over, False)
        self.game.ui.draw_board.assert_not_called()
