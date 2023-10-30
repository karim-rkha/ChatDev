'''
This is the main file of the Tic Tac Toe game application.
'''
import tkinter as tk
from tkinter import messagebox
from game import Game
class TicTacToeApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.game = Game()
        self.create_board()
    def create_board(self):
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", width=10, height=5,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    def make_move(self, row, col):
        if self.game.is_game_over():
            return
        if self.buttons[row][col].cget("text") != "":
            return
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.get_current_player())
            if self.game.is_game_over():
                self.show_result()
    def show_result(self):
        result = self.game.get_result()
        if result == "X":
            message = "Player X wins!"
        elif result == "O":
            message = "Player O wins!"
        else:
            message = "It's a draw!"
        messagebox.showinfo("Game Over", message)
        self.root.quit()
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()