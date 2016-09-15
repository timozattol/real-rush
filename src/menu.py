#!/usr/bin/env python3
"""Real-Rush menu"""

import pygame

BG_MOON = pygame.image.load("../assets/png/layers/parallax-mountain-bg.png")
BG_MOON_RES = BG_MOON.get_rect().size

BG_MOUNTAINS = pygame.image.load("../assets/png/layers/parallax-mountain-mountains.png")
BG_MOUNTAINS_RES = BG_MOUNTAINS.get_rect().size

BG_MOUNTAINS_FAR = pygame.image.load("../assets/png/layers/parallax-mountain-montain-far.png")
BG_MOUNTAINS_FAR_RES = BG_MOUNTAINS_FAR.get_rect().size

BG_TREES_FAR = pygame.image.load("../assets/png/layers/parallax-mountain-trees.png")
BG_TREES_FAR_RES = BG_TREES_FAR.get_rect().size

BG_TREES_FRONT = pygame.image.load("../assets/png/layers/parallax-mountain-foreground-trees.png")
BG_TREES_FRONT_RES = BG_TREES_FRONT.get_rect().size
class Menu():
    def __init__(self, player, display):
        self.player = player
        self.display = display
        # Background moon
        self.bg_moon = self._load_bg_images(BG_MOON,BG_MOON_RES)
        # Background mountains far
        self.bg_mountains_far = self._load_bg_images(BG_MOUNTAINS_FAR,BG_MOUNTAINS_FAR_RES)
        #Background mountains
        self.bg_mountains = self._load_bg_images(BG_MOUNTAINS,BG_MOUNTAINS_RES)
        #Background trees
        self.bg_trees_far = self._load_bg_images(BG_TREES_FAR,BG_TREES_FAR_RES)
        #Foreground trees
        self.bg_trees_front = self._load_bg_images(BG_TREES_FRONT,BG_TREES_FRONT_RES)

        self.bg_offset = 0.0
        self.tree_far_offset = 0.0
        self.tree_front_offset = 0.0

        self.mountains_speed = 5
        self.trees_far_speed = 8
        self.trees_front_speed = 30

    def update(self, elapsed_time):

        # Scroll and blit background
        self.display.blit(self.bg_moon, (0, 0))
        self.display.blit(self.bg_mountains_far, (0, 0))
        self.display.blit(self.bg_mountains, (-self.bg_offset, 0))
        self.display.blit(self.bg_trees_far, (-self.tree_far_offset, 0))
        self.display.blit(self.bg_trees_front, (-self.tree_front_offset, 0))

        self.bg_offset += self.mountains_speed * elapsed_time
        self.tree_far_offset += self.trees_far_speed * elapsed_time
        self.tree_front_offset += self.trees_front_speed * elapsed_time

        self.bg_offset %= self.bg_mountains.get_width()
        self.tree_far_offset %= self.bg_trees_far.get_width()
        self.tree_front_offset %= self.bg_trees_front.get_width()


    def _load_bg_images(self, image,res):
        ret = pygame.Surface(res, pygame.SRCALPHA, 32)
        ret = ret.convert_alpha()
        ret.blit(image, (0, 0))
        ratio = self.display.get_size()[1] / res[1]
        ret = pygame.transform.scale(image, (int(res[0] * ratio), int(res[1] * ratio)))
        return ret
