#!/usr/bin/env python3

import pygame
import os

from rush_game import RushGame
import colors

if __name__ == "__main__":
    
    # Tell X11 to center window
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    # Game base settings
    frameRate = 60
    frameMode = pygame.NOFRAME
    windowSize = (800,600)

    game = RushGame(windowSize)

    # Set up the display
    pygameDisplay = pygame.display.set_mode((windowSize),frameMode)
    pygame.display.set_caption("Real Rush")

    running = True


    while running:
        
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygameDisplay.fill(colors.white) 



    pygame.quit()
    quit()
