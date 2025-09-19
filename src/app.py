from ui import UI
from ai import AI
from math import inf

class Connect4:
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
            boolean: palauttaa true jos liike onnistui, muuten false
        """
        print("COL", col, "PLA", player)
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return True, (row, col)
        print("ei tilaa tällä sarakkeella")
        return False, None

    def full_board(self):
        for col in range(self.cols):
            if self.board[0][col] == 0:
                return False
        return True
    
    def win(self, current_player):
        print("PLAYER WON", current_player)
        # TO DO: joku teksti / ilmoitus näytölle voitosta

    def handle_click(self, event):
        """tutkii mitä saraketta klikattiin ja käsittelee hiiren klikkauksen,
        jos pelaajan (1) vuoro
        tekee siirron jos mahdollista
        tutkii voittoa
        siirtää vuoron tekoälylle

        Args:
            event (): olio klikkaukselle, sisältää esim koordinaatit
        """
        if self.game_over:
            return
        
        if self.current_player == 1:
            col = event.x // self.piece_size
            print(col)
            success, move = self.make_move(col, self.current_player)
            if success:
                print("PLAYER move")
                self.ui.draw_board(self.board)
                self.root.update_idletasks()
                if self.ai.winning_move(self.board, move[0], move[1]):
                    self.game_over = True
                    self.win(self.current_player)
                    return

                if self.full_board():
                    self.game_over = True
                    # TO DO: joku ilmotus
                    return

                self.current_player = 2
                self.ai_turn()

    def ai_turn(self):
        """tekoälyn vuoro pelissä,
        tutkii minimaxilla mikä on paras liike ja suorittaa sen
        tutkii mahdollisen voiton
        siirtää vuoron pelaajalle
        """

        col, value = self.ai.minimax(self.board, 5, -inf, inf, True, None)
        print("col", col, "val", value)

        success, move = self.make_move(col, self.current_player)
        if success:
            print("AI move")
            self.ui.draw_board(self.board)

            if self.ai.winning_move(self.board, move[0], move[1]):
                self.game_over = True
                self.win(self.current_player)
                return

            if self.full_board():
                self.game_over = True
                # TO DO: joku ilmotus
                return
            self.current_player = 1
