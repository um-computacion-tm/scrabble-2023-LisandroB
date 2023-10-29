import random
from unidecode import unidecode

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
        random.shuffle(bagTiles.tiles)
        for i in range(7 - len(self.tiles)):
            self.tiles.append(bagTiles.tiles[i])
            bagTiles.tiles.pop(i)
    
    def hasWord(self, word):
        res = []
        chk = []
        ret = 0
        for _ in self.tiles:
            res += _.letter.lower()
        for _ in word:
            if (_ == "ó"
                or _ == "é"
                or _ == "í" 
                or _ == "ú" 
                or _ == 'á'
            ):
                _ = unidecode(_)
            chk += _
        for _ in word:
            if (_ == "ó"
                or _ == "é"
                or _ == "í" 
                or _ == "ú" 
                or _ == 'á'
            ):
                _ = unidecode(_)
            if _ in res:
                ret +=1
                res.pop(res.index(_))
        if ret >= len(chk):
            return True
        else:
            return False
    
    def swapTiles(self, bagTiles, startStop):
            params = list(startStop)
            res = []
            for _ in params:
                res.append(_-1)
            list3 = map(self.tiles.__getitem__, res)
            for _ in list(list3):
                bagTiles.tiles.append(_)
                self.tiles.remove(_)
            self.fillTiles(bagTiles)
