from game.models import Tile

class Cell:
    def __init__(self, multiplier=None, multiplier_type=None, tile=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.tile = tile

    def calculate_value(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.tile.value * self.multiplier
        else:
            return self.tile.value
    
    def addValue(self, tile):
        self.tile = tile;