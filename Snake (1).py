import pygame
import random
import pygame.locals as keys

WIDTH = 500
HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

CELL_SIZE = 20

SNAKE_COLOR = pygame.Color('green')  
FOOD_COLOR = pygame.Color('red')
BG_COLOR = pygame.Color('black')

class Snake:

    def __init__(self):
        self.pos = [(4,4)]
        self.direction = 'right'

    def change_direction(self, direction):
        self.direction = direction
  
    def move(self):


class Food:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.generate()

    def generate(self):
        self.x = random.randint(0, WIDTH-CELL_SIZE) 
        self.y = random.randint(0, HEIGHT-CELL_SIZE)

snake = Snake()
food = Food()

running = True

while running:

  clock.tick(10)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
    if event.type == pygame.KEYDOWN:
      if event.key == keys.K_LEFT:
        snake.change_direction('left')
      # и т.д. для других клавиш

  screen.fill(BG_COLOR)
  
  # отрисовка змейки
  for pos in snake.pos:
    pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))  
  
  pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food.x, food.y, CELL_SIZE, CELL_SIZE))
  
  pygame.display.update()

pygame.quit()
