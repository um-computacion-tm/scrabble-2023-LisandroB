import random
from unidecode import unidecode
from game.board import Board

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

    def turnIntoUnidecode(self, letter):
        if (letter == "ó"
                or letter == "é"
                or letter == "í" 
                or letter == "ú" 
                or letter == 'á'
            ):
                letter = unidecode(letter)
                return letter
        else:
            return letter

    def fillTiles(self, bagTiles, game):
        board = Board()
        random.shuffle(bagTiles.tiles)
        for i in range(7 - len(self.tiles)):
            if len(bagTiles.tiles) > len(self.tiles):
                self.tiles.append(bagTiles.tiles[i])
                bagTiles.tiles.pop(i)
            else:
                board.endGame(game)
            
    def hasWord(self, word):
        res = []
        chk = []
        ret = 0
        for _ in self.tiles:
            res += _.letter.lower()
        for _ in word:
            _ = self.turnIntoUnidecode(_)
            chk += _
        for _ in word:
            _ = self.turnIntoUnidecode(_)
            if _ in res:
                ret +=1
                res.pop(res.index(_))
        if ret >= len(chk):
            return True
        else:
            return False
    
    def swapTiles(self, bagTiles, game, startStop):
        params = list(startStop)
        res = []
        for _ in params:
            res.append(_-1)
        mapTiles = map(self.tiles.__getitem__, res)
        for _ in list(mapTiles):
            bagTiles.tiles.append(_)
            self.tiles.remove(_)
        self.fillTiles(bagTiles, game)