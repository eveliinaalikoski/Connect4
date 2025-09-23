from tkinter import Canvas


class UI:
    """käyttöliittymä Connect 4 pelille
    sisältää pelilaudan piirtämisen tkinterillä
    """

    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.gameboard = False

    def start(self):
        """käynnistää käyttöliittymän
        - piirtää sinisen taustan
        - sitoo hiiren klikkauksen siitä vastaavaan funktioon
        """
        self.gameboard = Canvas(self.root,
                                bg="blue",
                                height=self.game.rows*self.game.piece_size,
                                width=self.game.cols*self.game.piece_size)
        self.gameboard.pack()

        self.gameboard.bind("<Button-1>", self.game.handle_click)
        self.draw_board(self.game.board)

    def draw_board(self, board):
        """piirtää pelilaudalle pelaajien nappulat oikean värisinä

        Args:
            board (matrix): 6x7 pelilauta, missä 
            0 = tyhjä = valkoinen,
            1 = pelaaja = punainen,
            5 = tekoäly = keltainen
        """
        self.gameboard.delete("all")

        for row in range(self.game.rows):
            for col in range(self.game.cols):
                x1 = col * self.game.piece_size
                y1 = row * self.game.piece_size
                if board[row][col] == 1:
                    color = "red"
                elif board[row][col] == 5:
                    color = "yellow"
                else:
                    color = "white"

                self.gameboard.create_oval(x1 + 5,
                                           y1 + 5,
                                           x1 + self.game.piece_size - 5,
                                           y1 + self.game.piece_size - 5,
                                           fill=color
                                           )
