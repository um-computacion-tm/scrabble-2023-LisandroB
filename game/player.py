from game.models import BagTiles
import random

class Player:
    def __init__(self): 
        self.tiles = [];
        self.id = 0;
    
    def getTiles(self):
        bag = BagTiles()
        random.shuffle(bag.tiles)
        for _ in range(0, 94):
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
        ret = 0
        for _ in self.tiles:
            res += _.letter
        for _ in word:
            chk += _
        for _ in res:
            if _.lower() in chk:
                ret +=1
        if ret >= len(chk):
            return True
        else:
            return False;