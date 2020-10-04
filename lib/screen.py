import pygame
from constants import *

def color_piece(piece_value):
    if piece_value == 1:
        return pygame.Color('red')
    if piece_value == 2:
        return pygame.Color('orange')
    if piece_value == 3:
        return pygame.Color('yellow')
    if piece_value == 4:
        return pygame.Color('green')
    if piece_value == 5:
        return pygame.Color('purple')
    if piece_value == 6:
        return pygame.Color('cyan')
    if piece_value == 7:
        return pygame.Color('pink')
    else:
        return BACKGROUND_COLOR

def convert_rc_to_coords(row, col):
    y = row*sheight
    x = col*swidth
    return x, y

def draw_piece(row, col, value, canvas):
    x, y = convert_rc_to_coords(row, col)
    block = pygame.Rect(x,y,fwidth, fheight)
    border = pygame.draw.rect(canvas, pygame.Color('black'), block, BORDER_WIDTH)
    canvas.fill(color_piece(value), rect=border)

def draw_game(screen, state):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)
    
    for row in range(len(state)):
        for col in range(len(state[row])):
            piece_value = state[row][col]
            if piece_value:
                draw_piece(row, col, piece_value, background)

    screen.blit(background, (0,0))
    pygame.display.flip()

def create_screen():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Tetris at home')
    return screen

