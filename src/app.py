from math import inf
import time
from ui import UI
from ai import AI


class Connect4:
    """luokka Connect 4 pelille
    sisältää pelilogiikkaan liittyvät funktiot
    """

    def __init__(self, root):
        self.root = root
        self.rows = 6
        self.cols = 7
        self.board = [[0 for col in range(self.cols)]
                      for row in range(self.rows)]
        self.piece_size = 80
        self.current_player = 1
        self.game_over = False
        self.ui = UI(self.root, self)
        self.ai = AI()

    def make_move(self, col, player):
        """lisää pelinappulan annettuun sarakkeeseen
        alimpaan tyhjään kohtaan, jos semmoinen on

        Args:
            col (int): sarakkeen numero 0-6
            player (int): pelaajan identifoiva numero 1=pelaaja ja 5=tekoäly

        Returns:
            tuple (boolean, (int, int)):
            - jos tilaa annetulla sarakkeella: (true, (eka vapaa rivi, annettu kolumni))
            - jos ei tilaa sarakkeella: (false, none)
        """
        # print("COL", col, "PLA", player)
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return True, (row, col)
        return False, None

    def full_board(self):
        """tarkistaa onko pelilauta täysi

        Returns:
            boolean: true, jos lauta täynnä, muuten false
        """
        for col in range(self.cols):
            if self.board[0][col] == 0:
                return False
        return True

    def handle_click(self, event):
        """käsittelee pelaajan hiiren klikkauksen
        jos pelaajan (1) vuoro ja peli ei ole ohi:
        - tekee siirron pelaajan klikkaamaan sarakkeeseen, jos mahdollista
        - tutkii voittoa tai tasapeliä
        - siirtää vuoron tekoälylle

        Args:
            event: tkinter-olio klikkaukselle, sisältää esim koordinaatit
        """
        if self.current_player == 1 and not self.game_over:
            col = event.x // self.piece_size
            success, move = self.make_move(col, self.current_player)
            if success:
                # print("PLAYER move")
                self.ui.draw_board(self.board)
                self.root.update_idletasks()
                if self.ai.winning_move(self.board, move[0], move[1]):
                    self.game_over = True
                    self.ui.draw_text_box("You win!")
                    return

                if self.full_board():
                    self.game_over = True
                    self.ui.draw_text_box("No more moves!")
                    return

                self.current_player = 5
                self.ai_turn()

    def ai_turn(self):
        """tekoälyn vuoro pelissä
        - käytetään iteratiivista syvenemistä aikarajalla ja syvyydestä 3 alkaen
        - tutkii minimaxilla mikä on paras siirto --> tekee siirron
        - tutkii voittoa tai tasapeliä
        - siirtää vuoron pelaajalle
        """
        start = time.time()
        depth = 3
        max_time = 2

        while True:
            if time.time() - start > max_time:
                break
            col, _ = self.ai.minimax(
                self.board, depth, -inf, inf, True, None)

            depth += 1

        # end = time.time()
        # print("TIME", end - start)
        # print("col", col, "val", value)

        success, move = self.make_move(col, self.current_player)
        if success:
            # print("AI move")
            self.ui.draw_board(self.board)

            if self.ai.winning_move(self.board, move[0], move[1]):
                self.game_over = True
                self.ui.draw_text_box("AI wins!")
                return

            if self.full_board():
                self.game_over = True
                self.ui.draw_text_box("No more moves!")
                return
            self.current_player = 1
