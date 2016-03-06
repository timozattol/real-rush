"""Generic level class"""
import pygame

class Level():
    def __init__(self, player):
        self.object_group = pygame.sprite.Groupe()
        self.player_object = player

    def update(self):
        self.object_group.update()

