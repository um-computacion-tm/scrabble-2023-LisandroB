from game.models import BagTiles

class Player:
    def __init__(self): 
        self.tiles = []
    def rellenar(self):
        self.tiles += BagTiles.take(
            7 - len(BagTiles)
        );
    def has_letters(self, tiles):
        res = []
        bagtiles = []
        for _ in range(0, len(tiles)):
            res += tiles[_].letter
        for _ in range(0, len(self.tiles)):
            bagtiles += self.tiles[_].letter
        for _ in res:
            if _ in bagtiles:
                return True;
            else:
                return False;