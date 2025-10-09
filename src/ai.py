from math import inf
from copy import deepcopy


class AI:
    """luokka Connect 4 pelin tekoälylle, missä lasketaan paras mahdollinen siirto tekoälylle
    laskentaan käytetään minimax-algoritmia alfa-beta -karsinnalla
     ja iteratiivisella syvenemisellä
    """

    def __init__(self):
        self.cols = 7
        self.rows = 6
        self.keys = {}

    def minimax(self, board, depth, alpha, beta, maximizing_player, last_move):
        """minimax-algoritmi alfa-beta karsinnalla,
        arvioi parasta siirtoa maksivoivan pelaajan (tekoälyn) kannalta,

        tutkii, onko pelitilanteessa oltu aikaisemmin ennen kuin aloittaa
        laskennan --> jos ollaan oltu, aloitetaan laskenta sen 
        pelitilanteen parhaimmasta sarakkeesta

        Args:
            board (matrix): 6x7 pelilauta
            depth (int): syvyys eli kuinka monta pelisiirtoa eteenpäin tutkitaan
            alpha (int): alfa-arvo, maksimoitavan solmun arvon alaraja,
                aluksi miinus ääretön
            beta (int): beta-arvo, minimoitavan arvon yläraja,
                aluksi ääretön
            maximizing_player (boolean): true jos tekoälyn (maksimoiva) vuoro,
                false jos pelaajan (minimoiva) vuoro
            last_move (tuple): viimeisin siirto muodossa (row, column)

        Returns:
            tuple (int, int): (col = parhaan liikkeen sarake, 
                value = pelilaudan pistemäärä liikkeen jälkeen)
        """
        possible_moves = self.get_moves(board)

        if last_move:
            if self.winning_move(board, last_move[0], last_move[1]):
                return (None, 100000) if board[last_move[0]][last_move[1]] == 5 else (None, -100000)

        if len(possible_moves) == 0:
            return None, 0  # tasapeli

        if depth == 0:
            return None, self.heuristic_value(board)

        # tarkistetaan onko pelitilanne laskettu aiemmin
        board_key = str(board)
        if board_key in self.keys:
            possible_moves.remove(self.keys[board_key])
            possible_moves.insert(0, self.keys[board_key])

        if maximizing_player:
            value = - inf
            column = 0
            for col in possible_moves:
                child_board, (r, c) = self.simulate_move(
                    board, col, maximizing_player)
                new_value = self.minimax(
                    child_board, depth - 1, alpha, beta, False, (r, c))
                if new_value[1] > value:
                    value = new_value[1]
                    column = col
                if value >= beta:
                    break
                alpha = max(alpha, value)

            self.keys[board_key] = column
            return column, value

        value = inf
        column = 0
        for col in possible_moves:
            child_board, (r, c) = self.simulate_move(
                board, col, maximizing_player)
            new_value = self.minimax(
                child_board, depth - 1, alpha, beta, True, (r, c))
            if new_value[1] < value:
                value = new_value[1]
                column = col
            if value <= alpha:
                break
            beta = min(beta, value)

        self.keys[board_key] = column
        return column, value

    def winning_move(self, board, row, column):
        """tarkistaa oliko viime siirto voittosiirto

        Args:
            board (matrix): 6x7 pelilauta
            row (int): viimesiirron rivi
            column (int): viimesiirron sarake

        Returns:
            boolean: palauttaa true, jos 4 samaa nappulaa peräkkäin, muuten false
        """
        player = board[row][column]
        if player == 0:
            return False

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
        """laskee heuristisen arvon pelitilanteelle apulistan
        sum_scores avulla, missä pistemäärä saadaan ikkunan summan indeksistä,

        tekoälyn (5) suorista saa positiivisia pisteitä ja pelaajan (1) negatiivisia

        Args:
            board (matrix): 6x7 pelilauta

        Returns:
            int: pelitilanteen pistemäärä
        """
        sum_scores = [0, -10, -30, -50, 0, 10,
                      0, 0, 0, 0, 30, 0, 0, 0, 0, 50, 0]
        score = 0

        # vaaka
        for row in range(self.rows):
            for col in range(self.cols - 3):
                window = [board[row][col],
                          board[row][col + 1],
                          board[row][col + 2],
                          board[row][col + 3]]
                score += sum_scores[sum(window)]

        # pysty
        for row in range(self.rows - 3):
            for col in range(self.cols):
                window = [board[row][col],
                          board[row + 1][col],
                          board[row + 2][col],
                          board[row + 3][col]]
                score += sum_scores[sum(window)]

        # yläviisto
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                window = [board[row][col],
                          board[row - 1][col + 1],
                          board[row - 2][col + 2],
                          board[row - 3][col + 3]]
                score += sum_scores[sum(window)]

        # alaviisto
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                window = [board[row][col],
                          board[row + 1][col + 1],
                          board[row + 2][col + 2],
                          board[row + 3][col + 3]]
                score += sum_scores[sum(window)]

        return score

    def get_moves(self, board):
        """etsitään laudalta sarakkeet joihin voidaan tehdä siirto,
        eli sarakkeet jotka ei ole täynnä,
        etsitään keskisarakkeesta alkaen

        Args:
            board (matrix): pelilauta 6x7 matriisi

        Returns:
            list: lista sarakkeista mihin pelinappulan voi tiputtaa
        """
        possible_moves = []
        for col in [3, 2, 4, 1, 5, 0, 6]:
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
                jos siirto on tekoälyn (merkataan 5), 
                muuten false (merkataan 1)

        Returns:
            matrix: kopio pelilaudasta missä on simuloitu siirto
        """
        for row in range(self.rows-1, -1, -1):
            if board[row][col] == 0:
                r = row
                break
        board_copy = deepcopy(board)
        board_copy[r][col] = 5 if maximizing_player else 1
        return board_copy, (r, col)
