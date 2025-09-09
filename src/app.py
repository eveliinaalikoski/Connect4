
class Connect4:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[0 for col in range(self.cols)]
                      for row in range(self.rows)]
        # print(self.board)

    def make_move(self, col, player):
        """lisää pelinappulan annettuun sarakkeeseen
        alimpaan tyhjään kohtaan, jos semmoinen on

        Args:
            col (int): sarakkeen numero 0-6
            player (int): pelaajan identifoiva numero 1=pelaaja ja 2=tekoäly
        """
        print("C", col, "PLA", player)
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == 0:
                self.board[row][col] = player
                return True
        print("ei tilaa tällä sarakkeella")
        return False
