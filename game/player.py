from game.models import BagTiles
import random

class Player:
    def __init__(self): 
        self.tiles = [];
        self.id = 0;
    
    def rellenar(self):
        self.tiles += BagTiles.take(7 - len(BagTiles));
    
    def getTiles(self):
        bag = BagTiles()
        random.shuffle(bag.tiles)
        for _ in range(0, 91):
            bag.tiles.pop()
        self.tiles = bag.tiles
        return self.tiles

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
    
    def hasWord(self, word):
        res = []
        chk = []
        for _ in self.tiles:
            res += _.letter
        for _ in word:
            chk += _
        for _ in chk:
            if _ in chk:
                return True;