#!/usr/bin/env python3
"""Real-Rush main module"""

import os
import pygame

from rush_game import RushGame
from game_manager import GameManager
import colors
import constants

if __name__ == "__main__":

    # Tell X11 to center window
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.mixer.pre_init(44100, -16, 2, 4096)
    pygame.init()

    # Game base settings
    FRAME_MODE = pygame.NOFRAME
    WINDOW_SIZE = constants.WINDOW_SIZE

    GAME = RushGame(WINDOW_SIZE)

    # Set up the display
    PYGAME_DISPLAY = pygame.display.set_mode((WINDOW_SIZE), FRAME_MODE)
    pygame.display.set_caption("Real Rush")

    manager = GameManager(PYGAME_DISPLAY)
    RUNNING = True
    CLOCK = pygame.time.Clock()

    while RUNNING:

        # Tick Clock
        CLOCK.tick(constants.FRAME_RATE)
        ELAPSED_TIME = CLOCK.get_time() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUNNING = False
                if event.key == pygame.K_r:
                    manager.reset_level()
                if event.key == pygame.K_n:
                    manager.next_level()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ## if mouse is pressed get position of cursor ##
               if pygame.mouse.get_pressed()[0] == 1:
                   pos = pygame.mouse.get_pos()
                   manager.mouse_left_click(pos)

        KEYS_PRESSED = pygame.key.get_pressed()
        # Jump
        if KEYS_PRESSED[pygame.K_SPACE] or KEYS_PRESSED[pygame.K_w]:
            manager.player.jump()
        if KEYS_PRESSED[pygame.K_k]:
            manager.player.kill()
        if KEYS_PRESSED[pygame.K_m]:
            manager.open_menu()

        # Clear Screen
        PYGAME_DISPLAY.fill(colors.WHITE)

        # Update & draw the current_level
        manager.update(ELAPSED_TIME)
        # Update & draw platforms
        pygame.display.update()


    pygame.quit()
    quit()
