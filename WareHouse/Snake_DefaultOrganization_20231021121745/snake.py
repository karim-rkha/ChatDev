'''
Snake Class
'''
import random
class Snake:
    def __init__(self, screen_width, screen_height):
        self.size = 1
        self.segments = [(screen_width // 2, screen_height // 2)]
        self.direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
    def move(self):
        x, y = self.segments[0]
        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10
        self.segments.insert(0, (x, y))
        if len(self.segments) > self.size:
            self.segments.pop()
    def change_direction(self, direction):
        if direction == "UP" and self.direction != "DOWN":
            self.direction = direction
        elif direction == "DOWN" and self.direction != "UP":
            self.direction = direction
        elif direction == "LEFT" and self.direction != "RIGHT":
            self.direction = direction
        elif direction == "RIGHT" and self.direction != "LEFT":
            self.direction = direction