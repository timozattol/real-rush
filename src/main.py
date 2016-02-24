"""Real-Rush main module"""
#!/usr/bin/env python3

import os
import pygame

from rush_game import RushGame
import colors

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

    PYGAME_DISPLAY.fill(colors.WHITE)
    RUNNING = True
    CLOCK = pygame.time.Clock()

    while RUNNING:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False

        CLOCK.tick(FRAME_RATE)
        pygame.display.update()



    pygame.quit()
    quit()
