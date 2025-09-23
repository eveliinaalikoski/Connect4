from tkinter import Tk
from app import Connect4


def main():
    window = Tk()
    window.title("Connect4")

    game = Connect4(window)
    game.ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
