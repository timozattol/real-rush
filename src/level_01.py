"""Level 1 class"""
import pygame
import constants
import colors
from level import Level
from block import Block

class Level01(Level):
    def __init__(self, player):
        super(Level01, self).__init__(player)

        # Objects of the level
        level = [[(200, 600), colors.BLACK, 16, 16]]

        for obj in level:
            obj = Block(obj[0], obj[1], obj[2], obj[3])
            self.object_group.add(obj)

    def update(self):
        self.object_group.update()

