#!/usr/bin/env python3
"""Real-Rush main module"""

import os
import pygame

from rush_game import RushGame
from block import Block
import colors
import constants

if __name__ == "__main__":

    # Tell X11 to center window
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    # Game base settings
    FRAME_MODE = pygame.NOFRAME
    WINDOW_SIZE = constants.WINDOW_SIZE

    GAME = RushGame(WINDOW_SIZE)

    # Set up the display
    PYGAME_DISPLAY = pygame.display.set_mode((WINDOW_SIZE), FRAME_MODE)
    pygame.display.set_caption("Real Rush")

    BG_IMAGE = pygame.image.load("../assets/urban-background.png")
    BG_RESOLUTION = (384, 224)

    BACKGROUND = pygame.Surface(BG_RESOLUTION)
    BACKGROUND = BACKGROUND.convert()
    BACKGROUND.blit(BG_IMAGE, (0, 0))
    BACKGROUND = pygame.transform.scale(BACKGROUND, PYGAME_DISPLAY.get_size())

    #Need a class for groups
    BLOCK_SPRITE_GROUP = pygame.sprite.Group()
    BLOCK_TEST = Block()
    BLOCK_SPRITE_GROUP.add(BLOCK_TEST)

    # Set Block height right "on the floor"
    BLOCK_HEIGHT = WINDOW_SIZE[1] - constants.FLOOR_HEIGHT - BLOCK_TEST.image.get_height()
    BLOCK_TEST.set_position(constants.BLOCK_LEFT_OFFSET, BLOCK_HEIGHT)

    PYGAME_DISPLAY.fill(colors.WHITE)

    BLOCK_SPRITE_GROUP.draw(PYGAME_DISPLAY)

    RUNNING = True
    CLOCK = pygame.time.Clock()

    while RUNNING:

        CLOCK.tick(constants.FRAME_RATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False

        KEYS_PRESSED = pygame.key.get_pressed()

        # Jump
        if KEYS_PRESSED[pygame.K_SPACE] or KEYS_PRESSED[pygame.K_w]:
            BLOCK_TEST.jump()

        # Clear Screen
        PYGAME_DISPLAY.fill(colors.WHITE)
        PYGAME_DISPLAY.blit(BACKGROUND, (0, 0))

        # Updates & draw everything in the group
        BLOCK_SPRITE_GROUP.update(CLOCK.get_time() / 1000)
        BLOCK_SPRITE_GROUP.draw(PYGAME_DISPLAY)
        pygame.display.update()



    pygame.quit()
    quit()
