from tkinter import Tk
from ui import UI
from app import Connect4


def main():
    window = Tk()
    window.title("Connect4")

    game = Connect4()
    ui = UI(window, game)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
