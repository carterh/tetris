import pygame

#Constants
#make sure the size and board dimensions are the correct ratio, i.e. 2w = h
SIZE = WIDTH, HEIGHT = (300, 600)
BOARD = BWIDTH, BHEIGHT = (10, 20)
square = swidth, sheight = (WIDTH//BWIDTH, HEIGHT//BHEIGHT)
square_fill = fwidth, fheight = (WIDTH//BWIDTH - 1, HEIGHT//BHEIGHT - 1)

#line_buffer = 2 # this was going to be used for spacing during drawing
BACKGROUND_COLOR = pygame.Color('blue')
BORDER_WIDTH = 5

#Game Mechanics
GAME_TICK = pygame.USEREVENT
INCREASE_SPEED = pygame.USEREVENT + 1
STARTING_TICK_MS = 500
INCREASE_SPEED_INTERVAL = 60000
TICK_SPAN_DECREASE = 95
