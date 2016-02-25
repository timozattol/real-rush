"""Block class used for debug"""
import pygame
import colors

class Block(pygame.sprite.Sprite):
    """Main constructor"""
    def __init__(self, color=colors.BLUE, width=16, height=16):
        super(Block, self).__init__()

        #pylint: disable-msg=E1121
        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def set_position(self, pos_x, pos_y):
        """Change position of the rectangle"""
        self.rect.x = pos_x
        self.rect.y = pos_y
    def set_center(self, pos_x, pos_y):
        """Change position of the center"""
        self.rect.centerx = pos_x
        self.rect.centery = pos_y
