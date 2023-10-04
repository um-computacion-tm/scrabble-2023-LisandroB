from game.models import BagTiles

class Player:
    def __init__(self): 
        self.tiles = []
    def rellenar(self):
        self.tiles += BagTiles.take(
            7 - len(BagTiles)
        );
    def has_letters(self):
        print(self.tiles)