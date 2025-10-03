from tkinter import Frame, Canvas, Label


class UI:
    """käyttöliittymä Connect 4 pelille
    sisältää pelilaudan piirtämisen tkinterillä
    """

    def __init__(self, root, game):
        self.game = game
        self.gameboard = False

        self.frame = Frame(root, bg="lightblue")
        self.frame.pack(fill="both", expand=True)

        self.topframe = Frame(self.frame, bg="lightblue")
        self.topframe.pack()
        self.toplabel = Label(self.topframe,
                              text="",
                              fg="blue",
                              bg="lightblue",
                              font=("Arial", 15, "bold"))
        self.toplabel.pack(padx=20, pady=20)

    def start(self):
        """käynnistää käyttöliittymän
        - piirtää sinisen taustan
        - sitoo hiiren klikkauksen siitä vastaavaan funktioon
        """
        self.gameboard = Canvas(self.frame,
                                bg="blue",
                                height=self.game.rows*self.game.piece_size,
                                width=self.game.cols*self.game.piece_size)
        self.gameboard.pack(padx=20, pady=20)

        self.gameboard.bind("<Button-1>", self.game.handle_click)
        self.draw_board(self.game.board)
        print("Start the game")

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

    def update_topbar(self, text):
        self.toplabel.config(text=text)
