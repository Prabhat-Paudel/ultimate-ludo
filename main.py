from tkinter import *
from game import Game

root = Tk()

root.title("Ultimate Ludo")

root.attributes("-fullscreen", True)

root.bind(
    "<Escape>",
    lambda e: root.attributes("-fullscreen", False)
)

game = Game(root)

root.mainloop()