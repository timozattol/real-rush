"""Level 1 class"""
import pygame

import colors
from level import Level
from prefabs import BlockPrefab
from constants import BG_SCROLL_SPEED
from utils import load_bg_images_scale_y

BG = pygame.image.load("../assets/png/city-background-tests.png")
BG_RES = BG.get_rect().size

BG_FAR = pygame.image.load("../assets/png/cemetary.png")
BG_FAR_RES = BG_FAR.get_rect().size

class Level01(Level):
    def __init__(self, player, display):
        super().__init__(player, display)

        BLUE_PREFAB = BlockPrefab(1, 2, colors.RED)
        BLACK_PREFAB = BlockPrefab(5, 2, colors.BLACK)

        # Sprites of the level
        deadly_sprites = [
            BLUE_PREFAB.new_sprite((20, 2)),
            BLUE_PREFAB.new_sprite((25, 4)),
            BLUE_PREFAB.new_sprite((30, 4)),
            BLUE_PREFAB.new_sprite((35, 2)),
            BLUE_PREFAB.new_sprite((40, 4)),
            BLUE_PREFAB.new_sprite((50, 2)),
            BLUE_PREFAB.new_sprite((60, 2)),
            BLUE_PREFAB.new_sprite((100, 4)),
            BLUE_PREFAB.new_sprite((120, 4)),
            BLUE_PREFAB.new_sprite((150, 2)),
            BLUE_PREFAB.new_sprite((200, 4)),
        ]

        platform_sprites = [
            BLACK_PREFAB.new_sprite((10, 2))
        ]

        for sprite in deadly_sprites:
            self.deadly_blocks.add(sprite)

        for sprite in platform_sprites:
            self.platform_blocks.add(sprite)

        # Background
        self.bg = load_bg_images_scale_y(BG, BG_RES, self.display)

        ratio = 0.7
        ret = pygame.Surface(BG_FAR_RES, pygame.SRCALPHA, 32)
        ret = ret.convert_alpha()
        ret = pygame.transform.scale(BG_FAR, (int(ratio * BG_FAR_RES[0]), int(ratio * BG_FAR_RES[1])))
        self.bg_far = ret

        # Scrolling parameter
        self.bg_offset = 0.0

        self.speed = BG_SCROLL_SPEED


    def update(self, elapsed_time):
        super().update(elapsed_time)

        if self.player.state == "dead":
            if self.speed <= 0:
                self.speed = 0
            else:
                self.speed -= 10.0

        # Scroll and blit background
        self.display.blit(self.bg_far, (-350, 0))
        self.display.blit(self.bg, (-self.bg_offset, 0))
        self.display.blit(self.bg, (self.bg.get_width() - self.bg_offset, 0))
        self.bg_offset += self.delta_pos(elapsed_time)
        self.bg_offset %= self.bg.get_width()
