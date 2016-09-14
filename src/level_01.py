"""Level 1 class"""
import colors
from level import Level
from prefabs import BlockPrefab

class Level01(Level):
    def __init__(self, player):
        super(Level01, self).__init__(player)

        BLUE_BLOCK_PREFAB = BlockPrefab(1, 2, colors.BLUE)

        # Sprites of the level
        sprites = [BLUE_BLOCK_PREFAB.new_sprite((2, 2)), BLUE_BLOCK_PREFAB.new_sprite((5, 2))]

        for sprite in sprites:
            self.object_group.add(sprite)
