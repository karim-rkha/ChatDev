'''
Food Class
'''
import random
import pygame
class Food:
    def __init__(self, screen_width, screen_height):
        self.position = self.generate_position(screen_width, screen_height)
    def generate_position(self, screen_width, screen_height):
        x = random.randint(0, screen_width - 10)
        y = random.randint(0, screen_height - 10)
        return x // 10 * 10, y // 10 * 10
    def draw(self):
        pygame.draw.rect(screen, RED, (self.position[0], self.position[1], 10, 10))