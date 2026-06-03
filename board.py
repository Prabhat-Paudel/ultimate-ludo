from tkinter import *


class Board:

    def __init__(self, root, game):

        self.game = game

        self.root = root

        self.size = min(
            root.winfo_screenwidth(),
            root.winfo_screenheight() - 200
        )

        self.cell = self.size // 15

        self.canvas = Canvas(
            root,
            width=self.size,
            height=self.size,
            bg="white"
        )

        self.draw_board()

    def draw_board(self):

        for row in range(15):

            for col in range(15):

                x1 = col * self.cell
                y1 = row * self.cell

                x2 = x1 + self.cell
                y2 = y1 + self.cell

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill="white",
                    outline="black"
                )