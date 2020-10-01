#!/usr/bin/env python3
import pygame
import sys
import engine

#Constants
size = width, height = (300, 600)
black = 0,0,0

def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tetris at home')

    background = pygame.Surface(screen.get_size())
    #what does this do?
    background = background.convert()
    background.fill(black)

    #Is this necessary after the fill call?
    screen.blit(background, (0,0))
    pygame.display.flip()

    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                playing = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                print('left')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                print('right')
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                print('space')
    print(str(engine.static_game()))
    pygame.quit()

if __name__ == '__main__':
    main()
