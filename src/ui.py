from tkinter import *

class UI:
    """käyttöliittymä"""
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.rows = self.game.rows
        self.cols = self.game.cols
        self.piece_size = 80
        self.current_player = 1

    def start(self):
        """aloittaa käyttöliittymän piirtämällä pelilaudan pohjan
        """
        self.gameboard = Canvas(self.root, bg="blue", height=self.rows*self.piece_size, width=self.cols*self.piece_size)
        self.gameboard.pack()

        self.gameboard.bind("<Button-1>", self.handle_click)
        self.draw_board(self.game.board)
              
    def draw_board(self, board):
        """piirtää pelilaudalle pelaajien nappulat oikean värisinä

        Args:
            board (lista): 6x7 matriisi, missä 0=tyhjä, 1=pelaaja, 2=tekoäly
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
                                           y1 +5,
                                           x1 + self.piece_size -5,
                                           y1 + self.piece_size -5,
                                           fill = color
                                           )
                
    def handle_click(self, event):
        """tutkii mitä saraketta klikattiin ja käsittelee hiiren klikkauksen

        Args:
            event (): olio klikkaukselle, sisältää esim koordinaatit
        """
        print("klikkaus", event)
        col = event.x // self.piece_size
        print(col)
        if self.game.make_move(col, self.current_player):
            print("onnistui")
            self.draw_board(self.game.board)
            if self.current_player == 1:
                self.current_player = 2
            else:
                self.current_player = 1

