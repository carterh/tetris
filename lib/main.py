#!/usr/bin/env python3
import pygame
import sys
import engine
from constants import *
from screen import create_screen, draw_game

def main():
    pygame.init()
    screen = create_screen()
    game = engine.Game(BHEIGHT, BWIDTH)
   
    pygame.time.set_timer(INCREASE_SPEED, INCREASE_SPEED_INTERVAL)
    tickspeed = STARTING_TICK_MS
    pygame.time.set_timer(GAME_TICK, tickspeed)
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
            elif event.type == INCREASE_SPEED:
                pygame.time.set_timer(GAME_TICK, 0)
                tickspeed = tickspeed - TICK_SPAN_DECREASE
                pygame.time.set_timer(GAME_TICK, tickspeed)

        
        draw_game(screen, game.game_state())
    
    pygame.quit()

if __name__ == '__main__':
    main()
