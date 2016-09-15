#!/usr/bin/env python3
"""Real-Rush main module"""

import os
import pygame

from rush_game import RushGame
from player import Player
from level_01 import Level01
from menu import Menu
from game_manager import GameManager
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


    # Add the player
    PLAYER = Player()
    # Set Player height right "on the floor"
    PLAYER_HEIGHT = WINDOW_SIZE[1] - constants.FLOOR_HEIGHT - PLAYER.image.get_height()
    PLAYER.set_position(constants.PLAYER_LEFT_OFFSET, PLAYER_HEIGHT)

    menu = Menu(PLAYER, PYGAME_DISPLAY)
    levels = [Level01(PLAYER, PYGAME_DISPLAY)]
    manager = GameManager(menu, levels)
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                ## if mouse is pressed get position of cursor ##
               if pygame.mouse.get_pressed()[0] == 1:
                   pos = pygame.mouse.get_pos()
                   manager.mouse_pressed(pos)

        KEYS_PRESSED = pygame.key.get_pressed()

        # Jump
        if KEYS_PRESSED[pygame.K_SPACE] or KEYS_PRESSED[pygame.K_w]:
            PLAYER.jump()
        if KEYS_PRESSED[pygame.K_k]:
            PLAYER.kill()
        if KEYS_PRESSED[pygame.K_r]:
            manager.reset_level()
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
