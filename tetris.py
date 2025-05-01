#INSTRUCTIONS
#press "UP" to rotate the block clockwise
#press "LEFT" and "RIGHT" to move the blocks sideways
#press "DOWN" to make the block move faster
#clearing each row gives the player 10 points
#game over, if the blocks reach the top of the grid

#importing libraries
import pygame
import random

#initialize the pygame window
pygame.font.init()

#defining the size of the game window (full one and game window)and objects
s_width = 800
s_height = 700
play_width = 300
play_height = 600
block_size = 30
top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height

#defining the shapes
A = [['.....','.....','..00.','.00..','.....'],
     ['.....','..0..','..00.','...0.','.....']]

B = [['.....','.....','.00..','..00.','.....'],
     ['.....','..0..','.00..','.0...','.....']]

C = [['..0..','..0..','..0..', '..0..','.....'],
     ['.....','0000.','.....','.....','.....']]

D = [['.....','.....','.00..','.00..','.....']]

E = [['.....','.0...','.000.','.....','.....'],
     ['.....','..00.','..0..','..0..','.....'],
     ['.....','.....','.000.','...0.','.....'],
     ['.....','..0..','..0..','.00..', '.....']]

F = [['.....','...0.','.000.','.....','.....'],
     ['.....','..0..','..0..','..00.','.....'],
     ['.....','.....','.000.','.0...', '.....'],
     ['.....','.00..','..0..','..0..', '.....']]

G = [['.....','..0..','.000.','.....','.....'],
     ['.....','..0..','..00.','..0..','.....'],
     ['.....','.....','.000.','..0..','.....'],
     ['.....','..0..','.00..','..0..','.....'],
     ]
H = [['.....','..0..','.000.','..0..','.....']]

#putting shapes and colors in an array so we can use their indices
shape_colors = [(255, 60, 60), (255, 150, 60), (255, 255, 50), (160, 255, 128), (0, 180, 255), (166, 120, 255), (140, 220, 255) , (255,150,220)]
shapes = [A, B, C, D, E, F, G, H]

#defining a class of shapes than we later randomly select from
class Piece(object):
    #size of the game window (height is 600, so 20 rows * 30, width is 300, so 10 columns * 30)
    rows = 20
    columns = 10

    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

#defining the grid (possible positions for blocks)
def create_grid(locked_positions={}):
    grid = [[(255, 255, 255) for x in range(10)] for x in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid

def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    #converting shapes array into blocks positions in x and y direction
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions

#defining in what positions can blocks be
def valid_space(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == (255, 255, 255)] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

#generating one of possible block shapes randomly
def get_shape():
    global shapes, shape_colors
    return Piece(5, 0, random.choice(shapes))

#defining the text layout displayed after the player loses
def draw_text_middle(text, size, color, surface):
    font = pygame.font.SysFont('calibri', size, bold=True)
    label = font.render(text, 1, color)
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), top_left_y + play_height / 2 - label.get_height() / 2))

#drawing the lines on the grid of play window
def draw_grid(surface, row, col):
    for i in range(row):
        pygame.draw.line(surface, (128, 128, 128), (top_left_x, top_left_y + i * 30),
                         (top_left_x + play_width, top_left_y + i * 30))
        for j in range(col):
            pygame.draw.line(surface, (128, 128, 128), (top_left_x + j * 30, top_left_y),
                             (top_left_x + j * 30, top_left_y + play_height))

#clearing the window if there are no white pixels in it
def clear_rows(grid, locked,score):
    inc = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if (255, 255, 255) not in row:
            inc += 1
            ind = i
            score[0] = score[0] + 10;
            print(score)
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)


def draw_right_side(shape, surface,score):
    #defining variables to place the score in the window
    font = pygame.font.SysFont('calibri', 30)
    label1 = font.render("SCORE", 1, (255, 255, 255))
    label2 = font.render(score, 1, (255, 255, 255))
    #viewing the score in the game window
    surface.blit(label1, (top_left_x + play_width+label1.get_width()/2, s_height / 2))
    surface.blit(label2, (top_left_x + play_width+label1.get_width()/2, (s_height / 2) + block_size))

#defining the play window (title label and grid)
def draw_window(surface):
    surface.fill((64, 64, 64))
    font = pygame.font.SysFont('calibri', 60)
    label = font.render('T E T R I S', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * 30, top_left_y + i * 30, 30, 30), 0)
    draw_grid(surface, 20, 10)
    pygame.draw.rect(surface, (100, 100, 100), (top_left_x, top_left_y, play_width, play_height), 5)

#main loop of the tetris
def main():
    global grid
    Score = [0]
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    #defining fall of the blocks
    while run:
        fall_speed = 0.3
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            #changing to a new piece after it reaches the bottom
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
        #quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                #moving the piece in x-direction (left and right)
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                #rotating the piece clockwise
                elif event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
                #moving the piece one block down(speeding it up)
                if event.key == pygame.K_DOWN:
                    # move shape down
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1

        shape_pos = convert_shape_format(current_piece)
        #changing color of the grid of the window to the color of the shape
        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        #switching to a new shape and checking if the row is full (if can be cleared)
        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions,Score)

        #calling the function displaying the game window
        draw_window(win)
        score = str(Score[0])
        draw_right_side(next_piece, win,score)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    #displaying score and quitting pygame after losing the game
    draw_text_middle("You Lost : " + str(Score[0]), 40, (0, 0, 0), win)
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('T E T R I S')

#running the tetris loop
main()
