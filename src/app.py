
class Connect4:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[0 for col in range(self.cols)] for row in range(self.rows)]
        # print(self.board)
        self.make_move(3, 2)
        self.make_move(3, 1)
        self.make_move(3, 2)
        self.make_move(5, 2)
        self.make_move(3, 1)
        self.make_move(3, 1)
        self.make_move(3, 2)
        self.make_move(3, 1)

    def make_move(self, col, player):
        """lisää pelinappulan annettuun sarakkeeseen
        alimpaan tyhjään kohtaan, jos semmoinen on

        Args:
            col (int): sarakkeen numero 0-6
            player (int): pelaajan identifoiva numero 1=pelaaja ja 2=tekoäly
        """
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == 0:
                print("COL", self.board[row][col])
                self.board[row][col] = player
                print("onnistui")
                return
        print("ei tilaa tällä sarakkeella")