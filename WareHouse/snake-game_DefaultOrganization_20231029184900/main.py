'''
This is the main file that runs the Snake game.
'''
import tkinter as tk
from snake import SnakeGame
def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
if __name__ == "__main__":
    main()