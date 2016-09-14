from pygame import Surface
from pygame.sprite import Sprite

from constants import TILE_WIDTH, TILE_HEIGHT
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
        sprite = Sprite()
        sprite.image = Surface([self.sizex * TILE_WIDTH, self.sizey * TILE_HEIGHT])
        sprite.image.fill(self.color)
        sprite.rect = sprite.image.get_rect()

        raw_pos = pos_convert(pos)
        sprite.rect.x, sprite.rect.y = raw_pos[0], raw_pos[1]

        return sprite
