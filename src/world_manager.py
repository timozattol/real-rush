#!/usr/bin/env python3
"""Real-Rush main module"""

import os
import pygame

from rush_game import RushGame
from player import Player
from block import Block
from level_01 import Level01
import colors
import constants

BG_MOON = pygame.image.load("../assets/png/layers/parallax-mountain-bg.png")
BG_MOON_RES = BG_MOON.get_rect().size

BG_MOUNTAINS = pygame.image.load("../assets/png/layers/parallax-mountain-mountains.png")
BG_MOUNTAINS_RES = BG_MOUNTAINS.get_rect().size

class WorldManager():
    def __init__(self,player,display):
        self.player = player
        self.display = display
        # Background moon
        self.bg_moon = pygame.Surface(BG_MOON_RES,pygame.SRCALPHA,32)
        self.bg_moon = self.bg_moon.convert_alpha()
        self.bg_moon.blit(BG_MOON, (0, 0))
        ratio = self.display.get_size()[1] / BG_MOON_RES[1]
        self.bg_moon = pygame.transform.scale(self.bg_moon, (int(BG_MOON_RES[0] * ratio), int(BG_MOON_RES[1] * ratio)))
        self.bg_offset = 0.0
        # Background mountains
        self.bg_mountains = pygame.Surface(BG_MOUNTAINS_RES,pygame.SRCALPHA,32)
        self.bg_mountains = self.bg_mountains.convert_alpha()
        self.bg_mountains.blit(BG_MOUNTAINS, (0, 0))
        ratio = self.display.get_size()[1] / BG_MOUNTAINS_RES[1]
        self.bg_mountains = pygame.transform.scale(self.bg_mountains, (int(BG_MOUNTAINS_RES[0] * ratio), int(BG_MOUNTAINS_RES[1] * ratio)))
        self.bg_offset = 0.0

    def update(self, elapsed_time):

        # Scroll and blit background
        self.display.blit(self.bg_moon, (0, 0))
        self.display.blit(self.bg_mountains, (0, 0))
