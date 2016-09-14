"""Level 1 class"""
import pygame

import colors
from level import Level
from prefabs import BlockPrefab
from constants import BG_SCROLL_SPEED

BG_IMAGE = pygame.image.load("../assets/city-background.png")
BG_RESOLUTION = BG_IMAGE.get_rect().size

class Level01(Level):
    def __init__(self, player, display):
        super().__init__(player, display)

        BLUE_BLOCK_PREFAB = BlockPrefab(1, 2, colors.BLUE)

        # Sprites of the level
        sprites = [BLUE_BLOCK_PREFAB.new_sprite((5, 2)), BLUE_BLOCK_PREFAB.new_sprite((10, 2))]

        for sprite in sprites:
            self.object_group.add(sprite)

        # Background
        self.bg = pygame.Surface(BG_RESOLUTION)
        self.bg = self.bg.convert()
        self.bg.blit(BG_IMAGE, (0, 0))
        ratio = self.display.get_size()[1] / BG_RESOLUTION[1]
        self.bg = pygame.transform.scale(self.bg, (int(BG_RESOLUTION[0] * ratio), int(BG_RESOLUTION[1] * ratio)))
        self.bg_offset = 0.0


    def update(self, elapsed_time):
        super().update(elapsed_time)

        # Scroll and blit background
        self.display.blit(self.bg, (-self.bg_offset, 0))
        self.display.blit(self.bg, (self.bg.get_width() - self.bg_offset, 0))
        self.bg_offset += BG_SCROLL_SPEED * elapsed_time
        self.bg_offset %= self.bg.get_width()
