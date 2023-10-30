'''
This file contains the Food class, which represents the food in the game.
'''
import pygame
import random
class Food:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.size = 20
        self.position = self.generate_position()
    def generate_position(self):
        x = random.randint(0, self.window_width // self.size - 1) * self.size
        y = random.randint(0, self.window_height // self.size - 1) * self.size
        return (x, y)
    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.position[0], self.position[1], self.size, self.size))