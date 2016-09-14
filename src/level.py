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
        self.deadly_blocks.update(self.delta_pos(elapsed_time))
        self.platform_blocks.update(self.delta_pos(elapsed_time))
        self.player.update(elapsed_time)

        spritecollide = pygame.sprite.spritecollide(self.player, self.deadly_blocks, False)
        if len(spritecollide) > 0:
            self.player.kill()

    def draw(self):
        #debug
        for obj in self.player_group:
            pygame.draw.rect(self.display, (200, 0, 0), obj.rect, 1)

        self.deadly_blocks.draw(self.display)
        self.platform_blocks.draw(self.display)
        self.player_group.draw(self.display)

    def delta_pos(self, elapsed_time):
        return self.speed * elapsed_time
