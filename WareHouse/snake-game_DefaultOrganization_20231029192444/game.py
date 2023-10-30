'''
This file contains the Game class which manages the game logic and GUI.
'''
import tkinter as tk
import random
class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.food = None
        self.direction = "Right"
        self.canvas.bind_all("<Key>", self.on_key_press)
        self.update()
    def on_key_press(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.direction = key
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
    def set_food(self, food):
        self.food = food
class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"
        self.color = "green"
        self.canvas.bind_all("<Key>", self.on_key_press)
    def on_key_press(self, event):
        key = event.keysym
        if key in ["Up", "Down", "Left", "Right"]:
            self.direction = key
    def move(self, direction):
        head = self.body[0]
        x, y = head
        if direction == "Up":
            y -= 10
        elif direction == "Down":
            y += 10
        elif direction == "Left":
            x -= 10
        elif direction == "Right":
            x += 10
        self.body.insert(0, (x, y))
        self.canvas.delete(tk.ALL)
        self.draw()
    def draw(self):
        for x, y in self.body:
            self.canvas.create_rectangle(x, y, x + 10, y + 10, fill=self.color)
    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)
    def is_collision(self):
        head = self.body[0]
        x, y = head
        return x < 0 or x >= 400 or y < 0 or y >= 400 or head in self.body[1:]
    def is_eating(self, food):
        head = self.body[0]
        return head == food.position
class Food:
    def __init__(self, canvas, snake):
        self.canvas = canvas
        self.snake = snake
        self.position = self.spawn()
        self.color = "red"
    def spawn(self):
        x = random.randint(0, 39) * 10
        y = random.randint(0, 39) * 10
        self.canvas.create_rectangle(x, y, x + 10, y + 10, fill=self.color)
        return x, y