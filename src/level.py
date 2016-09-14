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

        spritecollide = pygame.sprite.spritecollide(self.player, self.deadly_blocks, False)
        if len(spritecollide) > 0:
            self.player.kill()

        # TODO maybe refactor ;)
        spritecollide = pygame.sprite.spritecollide(self.player, self.platform_blocks, False)
        if len(spritecollide) > 0:
            diff_vert = spritecollide[0].rect.top - self.player.rect.bottom
            diff_hor = spritecollide[0].rect.left - self.player.rect.right

            if  diff_hor > diff_vert :
                # Colision from the left
                self.player.set_position(spritecollide[0].rect.x - 32, self.player.rect.y)
            else:
                self.player.set_position(self.player.rect.x, spritecollide[0].rect.top - self.player.rect.height)
                self.player.state = "running"

    def draw(self):
        self.deadly_blocks.draw(self.display)
        self.platform_blocks.draw(self.display)
        self.player_group.draw(self.display)

    def delta_pos(self, elapsed_time):
        return self.speed * elapsed_time
