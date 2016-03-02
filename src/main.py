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

    BACKGROUND = pygame.Surface(PYGAME_DISPLAY.get_size())
    BACKGROUND = BACKGROUND.convert()
    BACKGROUND.fill(colors.WHITE)
    #Need a class for groups
    BLOCK_SPRITE_GROUP = pygame.sprite.Group()
    BLOCK_TEST = Block()
    BLOCK_TEST.set_position(200, 200)
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

        KEYS_PRESSED = pygame.key.get_pressed()

        if KEYS_PRESSED[pygame.K_d]:

            BLOCK_TEST.move_right(2)

        if KEYS_PRESSED[pygame.K_s]:

            # This should not be used
            pass

        if KEYS_PRESSED[pygame.K_a]:

            BLOCK_TEST.move_left(2)

        if KEYS_PRESSED[pygame.K_w]:

            BLOCK_TEST.jump(2)






        BLOCK_SPRITE_GROUP.draw(PYGAME_DISPLAY)
        pygame.display.update()



    pygame.quit()
    quit()
