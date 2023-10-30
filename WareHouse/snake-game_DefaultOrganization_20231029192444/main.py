'''
This is the main file of the Snake game application.
'''
import tkinter as tk
from game import Game, Food
def main():
    root = tk.Tk()
    root.title("Snake Game")
    game = Game(root)
    food = Food(root, game.snake)
    game.set_food(food)
    root.mainloop()
if __name__ == "__main__":
    main()