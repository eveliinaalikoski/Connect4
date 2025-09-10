from math import inf
from copy import deepcopy

class AI:
    def __init__(self):
        self.cols = 7
        self.rows = 6

    def minimax(self, board, depth, alpha, beta, maximizing_player):
        """minimax-algoritmi alfa-beta karsinnalla,
        arvioi parasta siirtoa maksivoivan pelaajan (tekoälyn) kannalta

        Args:
            board (matrix): 6x7 pelilauta
            depth (int): syvyys eli kuinka monta pelisiirtoa eteenpäin tutkitaan
            alpha (int): alfa-arvo, maksimoitavan solmun arvon alaraja,
                aluksi miinus ääretön
            beta (int): beta-arvo, minimoitavan arvon yläraja,
                aluksi ääretön
            maximizing_player (boolean): true jos tekoälyn (maksimoiva) vuoro,
                false jos pelaajan (minimoiva) vuoro

        Returns:
            tuple (int, int): (parhaan liikkeen sarake, 
                pelilaudan pistemäärä liikkeen jälkeen)
        """
        if depth == 0 or self.is_terminal(board):
            return None, 100 # TO DO

        possible_moves = self.get_moves(board)

        if maximizing_player:
            value = - inf
            column = 0
            for col in possible_moves:
                child_board = self.simulate_move(board, col, maximizing_player)
                new_value = self.minimax(child_board, depth - 1, alpha, beta, False)
                print("VALUES", new_value, value)

                if new_value[1] > value:
                    value = new_value[1]
                    column = col
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return column, value

        else:
            value = inf
            column = 0
            for col in possible_moves:
                child_board = self.simulate_move(board, col, maximizing_player)
                new_value = self.minimax(child_board, depth - 1, alpha, beta, True)
                print("VALUES", new_value, value)
                if new_value[1] < value:
                    value = new_value[1]
                    column = col
                if value <= alpha:
                    break
                beta = min(beta, value)
            return column, value



# TO DO:

    def is_terminal(self, board):
        print("is_terminal", board)
        return False

    def get_moves(self, board):
        """etsitään laudalta sarakkeet joihin voidaan tehdä siirto,
        eli sarakkeet jotka ei ole täynnä

        Args:
            board (matrix): pelilauta 6x7 matriisi

        Returns:
            list: lista sarakkeista mihin pelinappulan voi tiputtaa
        """
        print("get_moves", board)
        possible_moves = []
        for col in range(self.cols):
            if board[0][col] == 0:
                possible_moves.append(col)
        return possible_moves

    def simulate_move(self, board, col, maximizing_player):
        """simuloi siirron pelilaudalla annettuun kolmuniin
        ja oikean pelaajan nappulalla

        Args:
            board (matrix): 6x7 pelilauta 
            col (int): sarake mihin pelinappula tiputetaan
            maximizing_player (boolean): arvo on true,
            jos siirto on tekoälyn (merkataan 2), 
            muuten false (merkataan 1)

        Returns:
            matrix: kopio pelilaudasta missä on simuloitu siirto
        """
        print("simulate_move")
        for row in range(self.rows-1, -1, -1):
            if board[row][col] == 0:
                r = row
                break
        board_copy = deepcopy(board)
        print(board_copy, "OG", board)
        board_copy[r][col] = 2 if maximizing_player else 1
        return board_copy
