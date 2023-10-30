'''
This is the main file of the Snake game application. It initializes the game and starts the game loop.
'''
import pygame
from snake import Snake
from food import Food
# Initialize pygame
pygame.init()
# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")
# Set up the game clock
clock = pygame.time.Clock()
# Initialize the snake and food
snake = Snake(window_width, window_height)
food = Food(window_width, window_height)
# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Detect key press events
            if event.key == pygame.K_UP and snake.dy == 0:     # Arrow up
                snake.dx, snake.dy = 0, -snake.size
            elif event.key == pygame.K_DOWN and snake.dy == 0: # Arrow down
                snake.dx, snake.dy = 0, snake.size
            elif event.key == pygame.K_LEFT and snake.dx == 0: # Arrow left
                snake.dx, snake.dy = -snake.size, 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:# Arrow right
                snake.dx, snake.dy = snake.size, 0


    # Update the snake and food
    snake.update()
    snake.check_collision(food)
    # Clear the window
    window.fill((0, 0, 0))
    # Draw the snake and food
    snake.draw(window)
    food.draw(window)
    # Update the display
    pygame.display.update()
    # Limit the frame rate
    clock.tick(10)
# Quit the game
pygame.quit()