"""Generic level class"""
import pygame

class Level(object):
    def __init__(self, player, display):
        self.deadly_blocks = pygame.sprite.Group()
        self.platform_blocks = pygame.sprite.Group()
        self.player = player
        self.player_group = pygame.sprite.Group([player])
        self.display = display
        self.speed = 0.0

    def update(self, elapsed_time):
        delta_pos = self.delta_pos(elapsed_time)
        self.deadly_blocks.update(delta_pos)
        self.platform_blocks.update(delta_pos)
        self.player.update(elapsed_time)
        self.handle_collisions()

        # If dead, gradually slow down scroll to zero
        if self.player.state == "dead":
            if self.speed <= 0:
                self.speed = 0
            else:
                self.speed -= 10.0

    def handle_collisions(self):
        # Count number of collisions
        collide_deadly = pygame.sprite.spritecollide(self.player, self.deadly_blocks, False)
        collide_platform = pygame.sprite.spritecollide(self.player, self.platform_blocks, False)
        if len(collide_deadly) > 0:
            self.player.kill()
        elif len(collide_platform) > 0:
            for sprite in collide_platform:
                self.player.handle_collision(sprite)

    def draw(self):
        self.deadly_blocks.draw(self.display)
        self.platform_blocks.draw(self.display)
        self.player_group.draw(self.display)

    def delta_pos(self, elapsed_time):
        return self.speed * elapsed_time

    def mouse_left_click(self, cursor_pos, game_manager):
        # No mouse interaction in levels by default
        pass
