'''
Snake Game
'''
import pygame
import random
from snake import Snake
from food import Food
# Initialize the game
pygame.init()
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")
# Create the Snake and Food objects
snake = Snake(screen_width, screen_height)
food = Food(screen_width, screen_height)
# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
    snake.move()
    if snake.segments[0] == food.position:
        snake.size += 1
        food.position = food.generate_position(screen_width, screen_height)
    if snake.segments[0][0] < 0 or snake.segments[0][0] >= screen_width or snake.segments[0][1] < 0 or snake.segments[0][1] >= screen_height:
        running = False
    for segment in snake.segments[1:]:
        if segment == snake.segments[0]:
            running = False
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    pygame.display.flip()
    clock.tick(20)
pygame.quit()