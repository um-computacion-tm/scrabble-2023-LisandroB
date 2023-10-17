from game.models import Tile

class Cell:
    def __init__(self, multiplier=None, multiplier_type=None, tile=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.tile = tile
        
    def __repr__(self):
        if self.tile:
            return repr(self.tile)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '

    def calculate_value(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.tile.value * self.multiplier
        else:
            return self.tile.value
    
    def addTile(self, tile):
        self.tile = tile;

    def noneTile(self):
        self.tile = None;