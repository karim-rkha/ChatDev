'''
This file contains the Game class that manages the game logic and GUI.
'''
import tkinter as tk
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Pong Game")
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="black")
        self.canvas.pack()
        self.ball = self.canvas.create_oval(390, 190, 410, 210, fill="white")
        self.paddle = self.canvas.create_rectangle(0, 0, 10, 60, fill="white")
        self.canvas.bind_all("<KeyPress-Up>", self.move_paddle_up)
        self.canvas.bind_all("<KeyPress-Down>", self.move_paddle_down)
        self.canvas.bind_all("<KeyRelease-Up>", self.stop_paddle)
        self.canvas.bind_all("<KeyRelease-Down>", self.stop_paddle)
        self.canvas.bind_all("<Button-1>", self.start_game)
        self.ball_dx = 1
        self.ball_dy = 1
        self.paddle_dy = 0
        self.game_started = False
    def move_ball(self):
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_pos = self.canvas.coords(self.ball)
        if ball_pos[1] <= 0 or ball_pos[3] >= 400:
            self.ball_dy *= -1
        if ball_pos[0] <= 0 or ball_pos[2] >= 800:
            self.ball_dx *= -1
        if self.check_collision():
            self.ball_dx *= -1
    def move_paddle_up(self, event):
        self.paddle_dy = -1
    def move_paddle_down(self, event):
        self.paddle_dy = 1
    def stop_paddle(self, event):
        self.paddle_dy = 0
    def start_game(self, event):
        self.game_started = True
    def check_collision(self):
        ball_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(self.paddle)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[1] <= paddle_pos[3]:
                return True
        return False
    def update_paddle(self):
        self.canvas.move(self.paddle, 0, self.paddle_dy)
        paddle_pos = self.canvas.coords(self.paddle)
        if paddle_pos[1] <= 0 or paddle_pos[3] >= 400:
            self.paddle_dy = 0
    def update(self):
        if self.game_started:
            self.move_ball()
            self.update_paddle()
        self.root.after(10, self.update)