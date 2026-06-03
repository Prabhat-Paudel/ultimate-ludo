from tkinter import *

from board import Board
from dice import Dice


class Game:

    def __init__(self, root):

        self.root = root

        self.dice = Dice()

        self.current_player = 0

        self.dice_value = 0

        self.build_ui()

    def build_ui(self):

        self.top_frame = Frame(
            self.root,
            bg="#222222"
        )

        self.top_frame.pack(fill=X)

        self.status = Label(
            self.top_frame,
            text="ULTIMATE LUDO",
            fg="white",
            bg="#222222",
            font=("Arial", 22, "bold")
        )

        self.status.pack(pady=10)

        self.board = Board(
            self.root,
            self
        )

        self.board.canvas.pack()

        controls = Frame(
            self.root
        )

        controls.pack(pady=10)

        Button(
            controls,
            text="ROLL DICE",
            command=self.roll_dice,
            font=("Arial", 18, "bold")
        ).pack(side=LEFT, padx=10)

    def roll_dice(self):

        self.dice_value = self.dice.roll()

        self.status.config(
            text=f"Dice: {self.dice_value}"
        )