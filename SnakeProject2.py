# This is the basic fun version of snake (SnakeProject3 will be the advanced version)
import pygame, sys, random
from pygame.math import Vector2
pygame.init()

cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number))
clock = pygame.time.Clock()

class SNAKE():
    def __init__(self):
        self.body = [Vector2(5,3), Vector2(4,3), Vector2(3,3)] # the first one is the head
        self.direction = Vector2(1,0) # moves one to the right
        self.new_block = False

    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            snake_rect = pygame.Rect((x_pos, y_pos, cell_size, cell_size))
            pygame.draw.rect(screen, pygame.Color(100,40,100),snake_rect)

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] # we only copy the first two elements as the third one will be deleted
            body_copy.insert(0,body_copy[0] + self.direction) # the first 0 makes sure that the element will be at the front (head)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

class FRUIT():
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect((int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size))
        pygame.draw.rect(screen, pygame.Color(100,0,50),fruit_rect)

    def randomize(self):
        self.x = random.randint(0,cell_number - 1) # minus 1 makes sure that the fruit is always on the screen (since the top bottom)
        self.y = random.randint(0,cell_number - 1)
        self.pos = Vector2(self.x, self.y) # we create a two dimensional vector because it makes movement easy

class MAIN():
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()  #so when we create an object from class MAIN we are also creating the snake and fruit

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            # reposition fruit
            self.fruit.randomize()
            # make snake longer
            self.snake.add_block()

    def check_fail(self):
        # check if snake is outside of screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
            pygame.quit()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)

    screen.fill((0,100,70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
