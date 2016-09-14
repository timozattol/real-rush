from pygame import Surface
from pygame.sprite import Sprite

from constants import TILE_WIDTH, TILE_HEIGHT, BG_SCROLL_SPEED
from utils import pos_convert


class Prefab:

    def new_sprite(self, pos):
        """Return a new Sprite from Prefab, at position pos"""
        pass


class BlockPrefab(Prefab):

    def __init__(self, sizex, sizey, color):
        super().__init__()
        self.sizex = sizex
        self.sizey = sizey
        self.color = color

    def new_sprite(self, pos):
        return Block(self.sizex, self.sizey, self.color, pos)


class Block(Sprite):
    def __init__(self, sizex, sizey, color, pos):
        super().__init__()
        self.image = Surface([sizex * TILE_WIDTH, sizey * TILE_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pos = pos_convert(pos)
        self.rect.x, self.rect.y = self.pos[0], self.pos[1]

    def update(self, delta_pos):
        self.pos = (self.pos[0] - delta_pos, self.pos[1])
        self.rect.x = int(self.pos[0])
        self.rect.y = int(self.pos[1])
