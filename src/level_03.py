"""Level 3 class"""
import pygame
from pygame.mixer import music
import colors
from level import Level
from prefabs import BlockPrefab
from constants import BG_SCROLL_SPEED, LEVEL3_MUSIC
from utils import load_bg_images_scale_y

BG = pygame.image.load("../assets/png/city-background-tests.png")
BG_RES = BG.get_rect().size

BG_FAR = pygame.image.load("../assets/png/night_house.png")
BG_FAR_RES = BG_FAR.get_rect().size

class Level03(Level):
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
        self.bg_far = load_bg_images_scale_y(BG_FAR, BG_FAR_RES, self.display)

        # Scrolling parameter
        self.bg_offset = 0.0

        self.speed = BG_SCROLL_SPEED

    def load_music(self):
        music.load(LEVEL3_MUSIC)
        music.play(-1)


    def update(self, elapsed_time):
        super().update(elapsed_time)

        if self.player.state == "dead":
            if self.speed <= 0:
                self.speed = 0
            else:
                self.speed -= 10.0

        # Scroll and blit background
        self.display.blit(self.bg_far, (-self.bg_offset, 0))
        self.display.blit(self.bg_far, (self.bg_far.get_width() - self.bg_offset, 0))
        self.bg_offset += self.delta_pos(elapsed_time)
        self.bg_offset %= self.bg_far.get_width()
