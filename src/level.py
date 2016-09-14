"""Generic level class"""
import pygame

class Level(object):
    def __init__(self, player, display):
        self.object_group = pygame.sprite.Group()
        self.player = player
        self.player_group = pygame.sprite.Group([player])
        self.display = display

    def update(self, elapsed_time):
        self.object_group.update()
        self.player.update(elapsed_time)

    def draw(self):
        self.object_group.draw(self.display)
        self.player_group.draw(self.display)
