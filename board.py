from tkinter import *

HOME_POSITIONS = {
    "red": [(2, 2), (4, 2), (2, 4), (4, 4)],
    "green": [(10, 2), (12, 2), (10, 4), (12, 4)],
    "yellow": [(2, 10), (4, 10), (2, 12), (4, 12)],
    "blue": [(10, 10), (12, 10), (10, 12), (12, 12)]
}

PATH = [
    (6,13),(6,12),(6,11),(6,10),(6,9),
    (5,8),(4,8),(3,8),(2,8),(1,8),(0,8),
    (0,7),(0,6),(1,6),(2,6),(3,6),(4,6),
    (5,6),(6,5),(6,4),(6,3),(6,2),(6,1),
    (6,0),(7,0),(8,0),(8,1),(8,2),(8,3),
    (8,4),(8,5),(9,6),(10,6),(11,6),(12,6),
    (13,6),(14,6),(14,7),(14,8),(13,8),
    (12,8),(11,8),(10,8),(9,8),(8,9),
    (8,10),(8,11),(8,12),(8,13),(8,14),
    (7,14),(6,14)
]

SAFE_CELLS = [0, 8, 13, 21, 26, 34, 39, 47]


class Board:

    def __init__(self, root, game):

        self.root = root
        self.game = game

        self.size = min(
            root.winfo_screenwidth(),
            root.winfo_screenheight() - 220
        )

        self.cell = self.size // 15

        self.canvas = Canvas(
            root,
            width=self.size,
            height=self.size,
            bg="white",
            highlightthickness=0
        )

        self.draw_board()

    def draw_board(self):

        self.canvas.delete("all")

        for row in range(15):

            for col in range(15):

                x1 = col * self.cell
                y1 = row * self.cell

                x2 = x1 + self.cell
                y2 = y1 + self.cell

                color = "white"

                if row < 6 and col < 6:
                    color = "#ffb3b3"

                elif row < 6 and col > 8:
                    color = "#b3ffb3"

                elif row > 8 and col < 6:
                    color = "#ffffb3"

                elif row > 8 and col > 8:
                    color = "#b3d1ff"

                self.canvas.create_rectangle(
                    x1, y1,
                    x2, y2,
                    fill=color,
                    outline="#555"
                )

        for i, (x, y) in enumerate(PATH):

            x1 = x * self.cell
            y1 = y * self.cell

            x2 = x1 + self.cell
            y2 = y1 + self.cell

            fill = "#eeeeee"

            if i in SAFE_CELLS:
                fill = "#99ff99"

            self.canvas.create_rectangle(
                x1, y1,
                x2, y2,
                fill=fill,
                outline="#444",
                width=2
            )

        self.draw_center()
        self.draw_tokens()

    def draw_center(self):

        c = self.cell

        self.canvas.create_polygon(
            7*c,6*c,
            9*c,7*c,
            7*c,9*c,
            6*c,7*c,
            fill="gold",
            outline="black",
            width=3
        )

    def draw_tokens(self):

        for color, player in self.game.players.items():

            for i, token in enumerate(player["tokens"]):

                pos = token.position

                if pos == -1:

                    x, y = HOME_POSITIONS[color][i]

                else:

                    index = (
                        self.game.start_index[color]
                        + pos
                    ) % len(PATH)

                    x, y = PATH[index]

                x1 = x*self.cell + 10
                y1 = y*self.cell + 10

                x2 = x1 + self.cell - 20
                y2 = y1 + self.cell - 20

                active = (
                    color ==
                    self.game.player_order[
                        self.game.current_player
                    ]
                )

                self.canvas.create_oval(
                    x1, y1,
                    x2, y2,
                    fill=color,
                    outline="gold" if active else "black",
                    width=5 if active else 2
                )

                self.canvas.create_text(
                    (x1+x2)//2,
                    (y1+y2)//2,
                    text=str(i+1),
                    fill="white",
                    font=("Arial", 12, "bold")
                )