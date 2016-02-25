"""Real-Rush main module"""
#!/usr/bin/env python3

import os
import random
import pygame

from rush_game import RushGame
import colors
from block import Block

if __name__ == "__main__":

    # Tell X11 to center window
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    # Game base settings
    FRAME_RATE = 60
    FRAME_MODE = pygame.NOFRAME
    WINDOW_SIZE = (800, 600)

    GAME = RushGame(WINDOW_SIZE)

    # Set up the display
    PYGAME_DISPLAY = pygame.display.set_mode((WINDOW_SIZE), FRAME_MODE)
    pygame.display.set_caption("Real Rush")

    #pylint: disable-msg=E1121
    BACKGROUND = pygame.Surface(PYGAME_DISPLAY.get_size())
    BACKGROUND = BACKGROUND.convert()
    BACKGROUND.fill(colors.WHITE)
    #Need a class for groups
    BLOCK_SPRITE_GROUP = pygame.sprite.Group()
    BLOCK_TEST = Block()
    BLOCK_SPRITE_GROUP.add(BLOCK_TEST)


    PYGAME_DISPLAY.fill(colors.WHITE)

    BLOCK_SPRITE_GROUP.draw(PYGAME_DISPLAY)

    RUNNING = True
    CLOCK = pygame.time.Clock()

    while RUNNING:

        CLOCK.tick(FRAME_RATE)
        BLOCK_SPRITE_GROUP.clear(PYGAME_DISPLAY, BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False

        BLOCK_TEST.set_center(random.randint(WINDOW_SIZE[0]/2, WINDOW_SIZE[0]/2+40),
                              random.randint(WINDOW_SIZE[1]/2, WINDOW_SIZE[1]/2+100))

        BLOCK_SPRITE_GROUP.draw(PYGAME_DISPLAY)
        pygame.display.update()



    pygame.quit()
    quit()
