from constants import WINDOW_SIZE, FLOOR_HEIGHT, TILE_WIDTH, TILE_HEIGHT, PLAYER_LEFT_OFFSET

def pos_convert(pos):
    """Convert from pos in the tile world to a raw pos in pygame world"""
    x = pos[0] * TILE_WIDTH + PLAYER_LEFT_OFFSET
    y = WINDOW_SIZE[1] - FLOOR_HEIGHT - pos[1] * TILE_HEIGHT

    return (x, y)
