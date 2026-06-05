from tkinter import *

from board import Board
from dice import Dice
from token import Token


class Game:

    def __init__(self, root):

        self.root = root

        self.dice = Dice()

        self.player_order = [
            "red",
            "green",
            "yellow",
            "blue"
        ]

        self.current_player = 0

        self.dice_value = 0

        self.start_index = {
            "red": 0,
            "green": 13,
            "yellow": 26,
            "blue": 39
        }

        self.players = {}

        self.create_players()

        self.build_ui()

    def create_players(self):

        for color in self.player_order:

            self.players[color] = {
                "tokens": [
                    Token(),
                    Token(),
                    Token(),
                    Token()
                ],
                "kills": 0,
                "finished": 0
            }

    def build_ui(self):

        self.top_frame = Frame(
            self.root,
            bg="#222222"
        )

        self.top_frame.pack(fill=X)

        self.status = Label(
            self.top_frame,
            text="ULTIMATE LUDO",
            bg="#222222",
            fg="white",
            font=("Arial", 22, "bold")
        )

        self.status.pack(pady=10)

        self.board = Board(
            self.root,
            self
        )

        self.board.canvas.pack()

        controls = Frame(self.root)
        controls.pack(pady=10)

        Button(
            controls,
            text="ROLL DICE",
            font=("Arial", 18, "bold"),
            command=self.roll_dice
        ).pack()

    def roll_dice(self):

        self.dice_value = self.dice.roll()

        player = self.player_order[
            self.current_player
        ]

        self.status.config(
            text=f"{player.upper()} rolled {self.dice_value}"
        )