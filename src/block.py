"""Block class"""
import pygame
import colors
import constants


class Block(pygame.sprite.Sprite):

    """Constructor"""
    def __init__(self, color=colors.BLUE, width=16, height=16):
        super(Block, self).__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def set_position(self, pos_x, pos_y):
        """Change position of the rectangle"""
        self.rect.x = pos_x
        self.rect.y = pos_y


