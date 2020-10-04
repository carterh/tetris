#!/usr/bin/env python3
import pygame
import sys
import engine

#Constants
#make sure the size and board dimensions are the correct ratio, i.e. 2w = h
SIZE = WIDTH, HEIGHT = (300, 600)
BOARD = BWIDTH, BHEIGHT = (10, 20)
square = swidth, sheight = (WIDTH//BWIDTH, HEIGHT//BHEIGHT)
square_fill = fwidth, fheight = (WIDTH//BWIDTH - 1, HEIGHT//BHEIGHT - 1)
#line_buffer = 2
BACKGROUND_COLOR = pygame.Color('blue')
GAME_TICK = pygame.USEREVENT
BORDER_WIDTH = 5

def color_piece(piece_value):
    if piece_value == 0:
        return pygame.Color('blue')
    elif piece_value == 1:
        return pygame.Color('red')
    else:
        return pygame.Color('green')

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

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Tetris at home')
    game = engine.Game(BHEIGHT, BWIDTH)
    
    # If you want to change the speed, set this timer back to 0 and create a new one in the game loop (maybe a SPEED_UP event?)
    pygame.time.set_timer(GAME_TICK, 1000)
    playing = True
    while playing:

        # If too many events are happening before the draw happens, I may need to convert this to a 
        # pygame.event.poll(), handle one event, then redraw
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                game.on_input(engine.User_action.LEFT)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                game.on_input(engine.User_action.RIGHT)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                game.on_input(engine.User_action.DOWN)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.on_input(engine.User_action.ROTATE)
            elif event.type == GAME_TICK:
                playing = game.on_tick()
        
        draw_game(screen, game.game_state())
    
    print(str(engine.static_game()))
    pygame.quit()

if __name__ == '__main__':
    main()
