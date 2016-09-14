"""Level 1 class"""
import pygame

import colors
from level import Level
from prefabs import BlockPrefab
from constants import WINDOW_SIZE

BG_IMAGE = pygame.image.load("../assets/urban-background.png")
BG_RESOLUTION = (384, 224)
BG_SCROLL_SPEED = 350

class Level01(Level):
    def __init__(self, player, display):
        super().__init__(player, display)

        BLUE_BLOCK_PREFAB = BlockPrefab(1, 2, colors.BLUE)

        # Sprites of the level
        sprites = [BLUE_BLOCK_PREFAB.new_sprite((2, 2)), BLUE_BLOCK_PREFAB.new_sprite((5, 2))]

        for sprite in sprites:
            self.object_group.add(sprite)

        # Background
        self.bg = pygame.Surface(BG_RESOLUTION)
        self.bg = self.bg.convert()
        self.bg.blit(BG_IMAGE, (0, 0))
        self.bg = pygame.transform.scale(self.bg, self.display.get_size())
        self.bg_offset = 0


    def update(self, elapsed_time):
        super().update(elapsed_time)

        # Scroll and blit background
        self.display.blit(self.bg, (-self.bg_offset, 0))
        self.display.blit(self.bg, (WINDOW_SIZE[0] - self.bg_offset, 0))
        self.bg_offset += BG_SCROLL_SPEED * elapsed_time
        self.bg_offset %= WINDOW_SIZE[0]
