'''
This is the main file that runs the ping pong game.
'''
import tkinter as tk
from game import Game
def main():
    root = tk.Tk()
    game = Game(root)
    game.update()  # Start the game update loop
    root.mainloop()
if __name__ == "__main__":
    main()