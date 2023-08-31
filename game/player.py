from game.models import BagTiles

class Player:
    def __init__(self, BagTiles):
        self.BagTiles = BagTiles;
    def rellenar(self):
        self.tiles += BagTiles.take(
            7 - len(BagTiles)
        );
        