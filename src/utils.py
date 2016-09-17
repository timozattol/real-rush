import pygame

from constants import WINDOW_SIZE, FLOOR_HEIGHT, TILE_WIDTH, TILE_HEIGHT, PLAYER_LEFT_OFFSET

def pos_convert(pos):
    """Convert from pos in the tile world to a raw pos in pygame world"""
    x = pos[0] * TILE_WIDTH + PLAYER_LEFT_OFFSET
    y = WINDOW_SIZE[1] - FLOOR_HEIGHT - pos[1] * TILE_HEIGHT

    return (x, y)

def load_bg_images_scale_y(image, res, display, custom_ratio=None):
    bg = pygame.Surface(res, pygame.SRCALPHA, 32)
    bg = bg.convert_alpha()
    if custom_ratio:
        ratio = custom_ratio
    else:
        ratio = display.get_size()[1] / res[1]
    bg = pygame.transform.scale(image, (int(res[0] * ratio), int(res[1] * ratio)))
    return bg
