import pygame

class SpriteSheetLoader:

    def __init__(self, path, im_size, sprite_size):
        self.sheet = pygame.image.load(path).convert_alpha()

        self.im_size = im_size
        self.sprite_size = sprite_size


    def load_sprite(self, position):
        """ Returns sprite image at position position from the sheet """
        left = position[0] * self.sprite_size[0]
        top = position[1] * self.sprite_size[1]
        rect = pygame.Rect(left, top, self.sprite_size[0], self.sprite_size[1])

        sprite = pygame.Surface(rect.size, pygame.SRCALPHA, 32).convert_alpha()
        sprite.blit(self.sheet, (0, 0), rect)

        return sprite

    def load_sprites(self, positions):
        sprites = []
        for position in positions:
            sprites.append(self.load_sprite(position))

        return sprites
