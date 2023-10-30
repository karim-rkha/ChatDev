'''
This file contains the SnakeGame class which represents the game logic and GUI.
'''
import tkinter as tk
import random
class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)
        self.direction = "Right"
        self.canvas.bind_all("<KeyPress>", self.on_key_press)
        self.update()
    def on_key_press(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            self.direction = event.keysym
    def update(self):
        if self.snake.is_collision():
            self.game_over()
        else:
            self.snake.move(self.direction)
            if self.snake.is_eating(self.food):
                self.snake.grow()
                self.food.spawn()
            self.canvas.after(100, self.update)
    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(200, 200, text="Game Over", fill="white", font=("Arial", 20))
class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.color = "white"
        self.canvas.create_rectangle(self.body[0][0], self.body[0][1], self.body[0][0]+10, self.body[0][1]+10, fill=self.color)
    def move(self, direction):
        head = self.body[0]
        x, y = head[0], head[1]
        if direction == "Up":
            y -= 10
        elif direction == "Down":
            y += 10
        elif direction == "Left":
            x -= 10
        elif direction == "Right":
            x += 10
        self.body.insert(0, (x, y))
        self.canvas.create_rectangle(x, y, x+10, y+10, fill=self.color)
        self.canvas.create_rectangle(self.body[-1][0], self.body[-1][1], self.body[-1][0]+10, self.body[-1][1]+10, fill="black")
        self.body.pop()
    def grow(self):
        self.body.append((0, 0))
    def is_collision(self):
        head = self.body[0]
        x, y = head[0], head[1]
        return x < 0 or x >= 400 or y < 0 or y >= 400 or head in self.body[1:]
    def is_eating(self, food):
        return self.body[0] == food.position
class Food:
    def __init__(self, canvas):
        self.canvas = canvas
        self.position = (0, 0)
        self.color = "red"
        self.spawn()
    def spawn(self):
        self.canvas.delete("food")
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        self.position = (x, y)
        self.canvas.create_rectangle(x, y, x+10, y+10, fill=self.color, tags="food")