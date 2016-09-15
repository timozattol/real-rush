#!/usr/bin/env python3
"""Real-Rush menu"""

import pygame

import colors
import random
from constants import TITLE_FONT_NAME, MENU_FONT_NAME


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
        self.bg_moon = self._load_bg_images(BG_MOON, BG_MOON_RES)
        # Background mountains far
        self.bg_mountains_far = self._load_bg_images(BG_MOUNTAINS_FAR, BG_MOUNTAINS_FAR_RES)
        # Background mountains
        self.bg_mountains = self._load_bg_images(BG_MOUNTAINS, BG_MOUNTAINS_RES)
        # Background trees
        self.bg_trees_far = self._load_bg_images(BG_TREES_FAR, BG_TREES_FAR_RES)
        # Foreground trees
        self.bg_trees_front = self._load_bg_images(BG_TREES_FRONT, BG_TREES_FRONT_RES)

        self.bg_offset = 0.0
        self.tree_far_offset = 0.0
        self.tree_front_offset = 0.0

        self.mountains_speed = 5
        self.trees_far_speed = 8
        self.trees_front_speed = 30

        # Menu offsets
        offset_menu_x = 55
        offset_menu_y = 138
        space_menu = 45

        # Fonts
        TITLE_FONT = pygame.font.Font(TITLE_FONT_NAME, 60)
        MENU_FONT = pygame.font.Font(MENU_FONT_NAME, 35)

        # Title
        self.real_rush_text = TITLE_FONT.render("real rush", True, colors.WHITE)

        # Menu start
        self.start_text = MENU_FONT.render("start", True, colors.WHITE)
        self.start_text_fade = MENU_FONT.render("start", True, colors.WHITE_PINKISH)
        self.start_rect = self.start_text.get_rect().move(offset_menu_x + 20, offset_menu_y)

        # Menu credits
        self.credits_text = MENU_FONT.render("credits", True, colors.WHITE)
        self.credits_text_fade = MENU_FONT.render("credits", True, colors.WHITE_PINKISH)
        self.credits_rect = self.credits_text.get_rect().move(offset_menu_x + 10, offset_menu_y + space_menu)

        # Menu exit
        self.exit_text = MENU_FONT.render("exit", True, colors.WHITE)
        self.exit_text_fade = MENU_FONT.render("exit", True, colors.WHITE_PINKISH)
        self.exit_rect = self.exit_text.get_rect().move(offset_menu_x, offset_menu_y + 2 * space_menu)

    def update(self, elapsed_time):

        # Scroll background
        self.bg_offset += self.mountains_speed * elapsed_time
        self.tree_far_offset += self.trees_far_speed * elapsed_time
        self.tree_front_offset += self.trees_front_speed * elapsed_time

        self.bg_offset %= self.bg_mountains.get_width()
        self.tree_far_offset %= self.bg_trees_far.get_width()
        self.tree_front_offset %= self.bg_trees_front.get_width()

    def draw(self):
        # Blit background
        self.display.blit(self.bg_moon, (0, 0))
        self.display.blit(self.bg_mountains_far, (0, 0))

        # Blit Text
        random_offset_title_x = random.randrange(0, 3)
        self.display.blit(self.real_rush_text, (450 + 2 + random_offset_title_x, 1))
        cursor_pos = pygame.mouse.get_pos()

        # Blit Menus
        self.blit_if_inside(self.start_text, self.start_text_fade, cursor_pos, self.start_rect)
        self.blit_if_inside(self.credits_text, self.credits_text_fade, cursor_pos, self.credits_rect)
        self.blit_if_inside(self.exit_text, self.exit_text_fade, cursor_pos, self.exit_rect)

        # Blit rest of background
        self.display.blit(self.bg_mountains, (-self.bg_offset, 0))
        self.display.blit(self.bg_trees_far, (-self.tree_far_offset, 0))
        self.display.blit(self.bg_trees_front, (-self.tree_front_offset, 0))

    def blit_if_inside(self, text_if_yes, text_if_no, cursor_pos, rect):
        """Blit one text if cursor is in rect, else the other text"""
        if self.is_inside(cursor_pos, rect):
            self.display.blit(text_if_yes, rect.topleft)
        else:
            self.display.blit(text_if_no, rect.topleft)

    def is_inside(self, cursor_pos, rect):
        """ Return True if cursor_pos is in rect """
        return rect.collidepoint(cursor_pos)


    def _load_bg_images(self, image, res):
        ret = pygame.Surface(res, pygame.SRCALPHA, 32)
        ret = ret.convert_alpha()
        ret.blit(image, (0, 0))
        ratio = self.display.get_size()[1] / res[1]
        ret = pygame.transform.scale(image, (int(res[0] * ratio), int(res[1] * ratio)))
        return ret
