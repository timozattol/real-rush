"""Generic level class"""
import pygame

class Level(object):
    def __init__(self, player):
        self.object_group = pygame.sprite.Group()
        self.player_object = player

    def update(self):
        self.object_group.update()

