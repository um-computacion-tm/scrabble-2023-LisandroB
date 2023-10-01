from game.models import BagTiles

class Player:
    def __init__(self):
        s = BagTiles();
        self.tiles = s.getTiles();
        
    def rellenar(self):
        self.tiles += BagTiles.take(
            7 - len(BagTiles)
        );