"""Block class used for debug"""
import pygame
import colors
import constants

class Block(pygame.sprite.Sprite):
    """Main constructor"""
    def __init__(self, color=colors.BLUE, width=16, height=16):
        super(Block, self).__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.state = "running"

        # The floor is scrolling left, thus velocity = 0 in x-axis
        self.velocity = (0, 0)

    def update(self, elapsed_time):
        """ Update the sprite at every frame, according to elapsed_time between
        last frame and current frame """
        # Move according to velocity
        self.rect.move_ip(self.velocity[0] * elapsed_time, self.velocity[1] * elapsed_time)

        # If touches floor, is running
        if self.is_on_floor():
            self.velocity = (0, 0)
            self.state = "running"
        # If in the air, subject to gravity
        else:
            self.velocity = (self.velocity[0], self.velocity[1] + (constants.GRAVITY * elapsed_time))


    def is_on_floor(self):
        return self.rect.bottom > constants.WINDOW_SIZE[1] - constants.FLOOR_HEIGHT

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

    def jump(self):
        """Make a jump"""
        # Can jump only if is running
        if self.state == "running":
            self.state = "jumping"
            self.velocity = (self.velocity[0], -constants.JUMPING_POWER)
