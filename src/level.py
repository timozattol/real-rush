"""Generic level class"""
import pygame

class Level(object):
    def __init__(self, player, display):
        self.object_group = pygame.sprite.Group()
        self.player_object = player
        self.display = display

    def update(self, elapsed_time):
        self.object_group.update()

    def draw(self):
        self.object_group.draw(self.display)
