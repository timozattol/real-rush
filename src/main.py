#!/usr/bin/env python3

import pygame
from rush_game import RushGame

if __name__ == "__main__":
    
    pygame.init()
    game = RushGame(800,600)
    pygameDisplay = pygame.display.set_mode((game.height,game.width))


