from tkinter import Canvas
from ai import AI
from math import inf

class UI:
    """käyttöliittymä"""

    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.rows = self.game.rows
        self.cols = self.game.cols
        self.piece_size = 80
        self.current_player = 1
        self.gameboard = False
        self.game_over = False
        self.ai = AI()

    def start(self):
        """aloittaa käyttöliittymän piirtämällä pelilaudan pohjan
        """
        self.gameboard = Canvas(self.root,
                                bg="blue",
                                height=self.rows*self.piece_size,
                                width=self.cols*self.piece_size)
        self.gameboard.pack()

        self.gameboard.bind("<Button-1>", self.handle_click)
        self.draw_board(self.game.board)

    def draw_board(self, board):
        """piirtää pelilaudalle pelaajien nappulat oikean värisinä

        Args:
            board (lista): 6x7 matriisi, missä 0=tyhjä=valkoinen,
             1=pelaaja=punainen, 2=tekoäly=keltainen
        """
        self.gameboard.delete("all")

        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * self.piece_size
                y1 = row * self.piece_size
                if board[row][col] == 1:
                    color = "red"
                elif board[row][col] == 2:
                    color = "yellow"
                else:
                    color = "white"

                self.gameboard.create_oval(x1 + 5,
                                           y1 + 5,
                                           x1 + self.piece_size - 5,
                                           y1 + self.piece_size - 5,
                                           fill=color
                                           )

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
            success, move = self.game.make_move(col, self.current_player)
            if success:
                print("PLAYER move")
                self.draw_board(self.game.board)
                self.root.update_idletasks()
                if self.ai.winning_move(self.game.board, move[0], move[1]):
                    self.game_over = True
                    self.win(self.current_player)
                    return

                if self.game.full_board():
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

        col, value = self.ai.minimax(self.game.board, 4, -inf, inf, True, None)
        print("col", col, "val", value)

        success, move = self.game.make_move(col, self.current_player)
        if success:
            print("AI move")
            self.draw_board(self.game.board)

            if self.ai.winning_move(self.game.board, move[0], move[1]):
                self.game_over = True
                self.win(self.current_player)
                return

            if self.game.full_board():
                self.game_over = True
                # TO DO: joku ilmotus
                return
            self.current_player = 1

    def win(self, current_player):
        print("PLAYER WON", current_player)
        # TO DO: joku teksti / ilmoitus näytölle voitosta
