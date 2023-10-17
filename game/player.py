import random

class Player:
    def __init__(self, bagTiles, id): 
        self.tiles = [];
        self.id = id;
        self.score = 0;
        self.getTiles(bagTiles)
    
    def getTiles(self, bagTiles):
        random.shuffle(bagTiles.tiles)
        for i in range(0, 7):
            self.tiles.append(bagTiles.tiles[i])
            bagTiles.tiles.pop(i)
        return self.tiles
    
    def shuffleTiles(self):
        return random.shuffle(self.tiles)

    def fillTiles(self, bagTiles):
        for i in range(7 - len(self.tiles)):
            self.tiles.append(bagTiles.tiles[i])
            bagTiles.tiles.pop(i)

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