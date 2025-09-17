from math import inf
from copy import deepcopy

class AI:
    def __init__(self):
        self.cols = 7
        self.rows = 6

    def minimax(self, board, depth, alpha, beta, maximizing_player, last_move):
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
        terminal = self.is_terminal(board, depth, last_move)
        if terminal is not False:
            return None, terminal

        possible_moves = self.get_moves(board)

        if maximizing_player:
            value = - inf
            column = 0 # TO DO: alottaa keskeltä
            for col in possible_moves:
                child_board, (r, c) = self.simulate_move(board, col, maximizing_player)
                new_value = self.minimax(child_board, depth - 1, alpha, beta, False, (r, c))
                # print("VALUES", new_value, value)

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
                child_board, (r, c) = self.simulate_move(board, col, maximizing_player)
                new_value = self.minimax(child_board, depth - 1, alpha, beta, True, (r, c))
                # print("VALUES", new_value, value)
                if new_value[1] < value:
                    value = new_value[1]
                    column = col
                if value <= alpha:
                    break
                beta = min(beta, value)
            return column, value

    def is_terminal(self, board, depth, last_move): # TO DO
        # print("is_terminal", board)
        # tarkista oliko edellinen siirto voittosiirto, palauta true
        # jos lauta täysi, palautetaan 0 tasapeli
        if last_move:
            row, column = last_move
            if self.winning_move(board, row, column):
                return 100000 if board[row][column] == 2 else -100000
        
        if len(self.get_moves(board)) == 0:
            return 0 # tasapeli

        if depth == 0:
            return self.heuristic_value(board)
    
        return False
    
    def winning_move(self, board, row, column):
        # print("winning_move", board, row, column)
        player = board[row][column]
        # directions = [vaaka, pysty, ylösviisto, alasviisto]
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for drow, dcol in directions:
            count = 1
            
            # positiiviseen suuntaan
            r = row + drow
            c = column + dcol
            while 0 <= r < self.rows and 0 <= c < self.cols:
                if board[r][c] != player:
                    break
                count += 1
                r += drow
                c += dcol

            # negatiiviseen suuntaan
            r = row - drow
            c = column - dcol
            while 0 <= r < self.rows and 0 <= c < self.cols:
                if board[r][c] != player:
                    break
                count += 1
                r -= drow
                c -= dcol

            if count >= 4:
                return True

        return False

    def heuristic_value(self, board):
        score = 0

        # keskikolumni
        center_column = [board[row][3] for row in range(self.rows)]
        # print("center", center_column)
        count = center_column.count(2)
        score += count * 5

        # vaaka
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [board[row][col],
                          board[row][col + 1],
                          board[row][col + 2],
                          board[row][col + 3]]
                score += self.score_window(window)
            
        # pysty
        for row in range(self.rows - 3):
            for col in range(self.cols):
                window = [board[row][col],
                          board[row + 1][col],
                          board[row + 2][col],
                          board[row + 3][col]]
                score += self.score_window(window)

        # yläviisto
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [board[row][col],
                          board[row - 1][col + 1],
                          board[row - 2][col + 2],
                          board[row - 3][col + 3]]
                score += self.score_window(window)
        
        # alaviisto
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [board[row][col],
                          board[row + 1][col + 1],
                          board[row + 2][col + 2],
                          board[row + 3][col + 3]]
                score += self.score_window(window)
        # print("SCORE", score)
        return score

    def score_window(self, window):
        # 0 = tyhjä, 1 = player, 2 = AI
        score = 0

        if window.count(2) == 4:
            score += 100
        elif window.count(2) == 3 and window.count(0) == 1:
            score += 10
        elif window.count(2) == 2 and window.count(0) == 2:
            score += 5
        
        if window.count(1) == 4:
            score -= 100
        elif window.count(1) == 3 and window.count(0) == 1:
            score -= 10
        elif window.count(1) == 2 and window.count(0) == 2:
            score -= 5

        return score
    
    def get_moves(self, board):
        """etsitään laudalta sarakkeet joihin voidaan tehdä siirto,
        eli sarakkeet jotka ei ole täynnä

        Args:
            board (matrix): pelilauta 6x7 matriisi

        Returns:
            list: lista sarakkeista mihin pelinappulan voi tiputtaa
        """
        # print("get_moves", board)
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
        # print("simulate_move")
        for row in range(self.rows-1, -1, -1):
            if board[row][col] == 0:
                r = row
                break
        board_copy = deepcopy(board)
        # print(board_copy, "OG", board)
        board_copy[r][col] = 2 if maximizing_player else 1
        return board_copy, (r, col)
