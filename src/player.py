"""Player class"""
import pygame
import colors
import constants
from sprites import SpriteSheetLoader, SpriteAnimation

# Duration before sprite animation changes
SPRITE_ANIM_DURATION = 0.035

class Player(pygame.sprite.Sprite):
    """Main constructor"""
    def __init__(self, color=colors.BLUE, width=16, height=16, lives=3, stamina=2):
        super().__init__()

        loader = SpriteSheetLoader("../assets/png/player_spritesheet_cape.png",
                                   (512, 576), (64, 64))

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

        dying_positions = [
                (0, 2),(1, 2),(2, 2),(3, 2),(4, 2),(5, 2),(6, 2),(7, 2)
        ]



        # Animations
        self.run_animation = SpriteAnimation(loader, running_positions,
                                              looping=True)
        self.jump_animation = SpriteAnimation(loader, jumping_positions,
                                              looping=False)
        self.stand_animation = SpriteAnimation(loader, standing_positions,
                                              looping=True)
        self.die_animation = SpriteAnimation(loader, dying_positions,looping=False)

        # Elapsed time since last sprite animation
        self.sprite_elapsed_time = 0

        # Start with a running image
        self.state = "running"
        self.image = self.run_animation.next_image()
        self.rect = self.image.get_rect()

        # TODO remove hack
        self.rect.width = self.rect.width / 1.5

        # The floor is scrolling left, thus velocity = 0 in x-axis
        self.velocity = (0, 0)

        # Set Player height right "on the floor"
        height = constants.WINDOW_SIZE[1] - constants.FLOOR_HEIGHT - self.image.get_height()
        self.set_position(constants.PLAYER_LEFT_OFFSET, height)

    def update(self, elapsed_time):
        """ Update the sprite at every frame, according to elapsed_time between
        last frame and current frame """
        # Move according to velocity
        self.rect.move_ip(self.velocity[0] * elapsed_time, self.velocity[1] * elapsed_time)

        # If touches floor, starts running
        if self.is_on_floor():
            self.set_position(self.rect.x, constants.WINDOW_SIZE[1] \
            - constants.FLOOR_HEIGHT - self.image.get_height())

            self.velocity = (0, 0)
            self.state = "running"
        # Else if jumping, subject to gravity
        elif self.state == "jumping":
            self.velocity = (
                self.velocity[0],
                self.velocity[1] + (constants.GRAVITY * elapsed_time)
            )

        # Update sprite elapsed time
        self.sprite_elapsed_time += elapsed_time

        # Animate sprite if enough elapsed time
        if self.sprite_elapsed_time >= SPRITE_ANIM_DURATION:
            self.sprite_elapsed_time = 0

            # Animate sprite according to current state
            if self.state == "running":
                self.image = self.run_animation.next_image()
            elif self.state == "jumping":
                self.image = self.jump_animation.next_image()
            elif self.state == "dead":
                self.image = self.die_animation.next_image()

    def handle_collision(self, sprite):
        diff_vert = self.rect.bottom - sprite.rect.top
        safety_pixels = 40

        # Check if collision is from the top, meaning that the rect of the
        # player is above or slightly (safety_pixels) below the top of the
        # rect of the sprite.
        if diff_vert > 0 + safety_pixels :
            # Collision from the left, stick to the rect
            self.set_position(sprite.rect.x - self.rect.width, self.rect.y)
        else:
            # Collision from the top, start running on block
            self.set_position(self.rect.x, sprite.rect.top - self.rect.height)
            self.state = "running"

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

    def kill(self):
        self.velocity = (0, 0)
        self.state = "dead"
