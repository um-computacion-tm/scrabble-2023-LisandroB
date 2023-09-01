from game.models import BagTiles

class Player:
    def __init__(self, BagTiles):
        self.tiles = BagTiles.take(7);
        self.BagTiles = BagTiles;
    def rellenar(self):
        self.tiles += BagTiles.take(
            7 - len(BagTiles)
        );