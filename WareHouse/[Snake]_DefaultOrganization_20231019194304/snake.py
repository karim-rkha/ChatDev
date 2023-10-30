'''
This file contains the Snake class, which represents the snake in the game.
'''
import pygame
class Snake:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.size = 20
        self.x = window_width // 2
        self.y = window_height // 2
        self.dx = self.size
        self.dy = 0
        self.body = [(self.x, self.y)]
    def update(self):
        self.x += self.dx
        self.y += self.dy
        # Wrap around the screen
        if self.x < 0:
            self.x = self.window_width - self.size
        elif self.x >= self.window_width:
            self.x = 0
        if self.y < 0:
            self.y = self.window_height - self.size
        elif self.y >= self.window_height:
            self.y = 0
        # Update the body
        self.body.insert(0, (self.x, self.y))
        self.body.pop()
    def check_collision(self, food):
        if self.body[0] == food.position:
            self.body.append(food.position)
            food.generate_position()
    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, (0, 255, 0), (segment[0], segment[1], self.size, self.size))