"""Block class used for debug"""
import pygame
import colors

class Block(pygame.sprite.Sprite):
    """Main constructor"""
    def __init__(self, color=colors.BLUE, width=16, height=16):
        super(Block, self).__init__()

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

    def move_right(self, dist):
        """Move block to the right"""
        self.rect.centerx = self.rect.centerx + dist

    def move_left(self, dist):
        """Move block to the left"""
        self.rect.centerx = self.rect.centerx - dist

    def move_down(self, dist):
        """Move block down"""
        self.rect.centery = self.rect.centery + dist

    def jump(self, dist):
        """Make a jump"""
        self.rect.centery = self.rect.centery - dist

