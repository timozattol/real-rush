"""Player class"""
import pygame
import colors
import constants
from sprite_sheet import SpriteSheetLoader

# Duration before sprite animation changes
SPRITE_ANIM_DURATION = 0.035

class Player(pygame.sprite.Sprite):
    """Main constructor"""
    def __init__(self, color=colors.BLUE, width=16, height=16, lives=3, stamina=2):
        super(Player, self).__init__()

        running_positions = [
            (4, 0), (5, 0), (6, 0), (7, 0),
            (0, 1), (1, 1), (2, 1), (3, 1),
        ]

        jumping_positions = [
            (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5)
        ]

        standing_positions = [
            (0, 8)
        ]

        loader = SpriteSheetLoader("../assets/player_spritesheet.png", (512, 576), (64, 64))

        self.run_sprites = loader.load_sprites(running_positions)
        self.jump_sprites = loader.load_sprites(jumping_positions)
        self.stand_sprites = loader.load_sprites(standing_positions)
        self.sprite_index = 0
        self.sprite_elapsed_time = 0
        self.image = self.run_sprites[self.sprite_index]

        self.rect = self.image.get_rect()

        self.state = "running"

        # The floor is scrolling left, thus velocity = 0 in x-axis
        self.velocity = (0, 0)

    def update(self, elapsed_time):
        """ Update the sprite at every frame, according to elapsed_time between
        last frame and current frame """
        # Move according to velocity
        self.rect.move_ip(self.velocity[0] * elapsed_time, self.velocity[1] * elapsed_time)

        # If not running and touches floor, starts running
        if self.state != "running" and self.is_on_floor():
            self.set_position(self.rect.x, constants.WINDOW_SIZE[1] \
            - constants.FLOOR_HEIGHT - self.image.get_height())

            self.velocity = (0, 0)
            self.state = "running"
        # Else if jumping, subject to gravity
        elif self.state == "jumping":
            self.velocity = (self.velocity[0], self.velocity[1] \
            + (constants.GRAVITY * elapsed_time))

        # Update sprite elapsed time
        self.sprite_elapsed_time += elapsed_time

        # Animate sprite if enough elapsed time
        if self.sprite_elapsed_time >= SPRITE_ANIM_DURATION:
            self.sprite_elapsed_time = 0

            # Animate sprite according to current state
            if self.state == "running":
                self.sprite_index = (self.sprite_index + 1) % len(self.run_sprites)
                self.image = self.run_sprites[self.sprite_index]
            elif self.state == "jumping":
                # TODO factor out a set of sprite images into a class SpriteAnimation,
                # and allow for "non loop" animations (for jumping)
                self.sprite_index = (self.sprite_index + 1) % len(self.jump_sprites)
                self.image = self.jump_sprites[self.sprite_index]
            else:
                self.sprite_index = 0
                self.image = self.stand_sprites[0]

    def is_on_floor(self):
        return self.rect.bottom > constants.WINDOW_SIZE[1] - constants.FLOOR_HEIGHT

    def set_position(self, pos_x, pos_y):
        """Change position of the rectangle"""
        self.rect.x = pos_x
        self.rect.y = pos_y

    def jump(self):
        """Make a jump"""
        # Can jump only if is running
        if self.state == "running":
            self.state = "jumping"
            self.velocity = (self.velocity[0], -constants.JUMPING_POWER)
