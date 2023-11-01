from game.cell import Cell
from game.models import Tile
from game.multipliers import Multipliers

class Board:
    def __init__(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]
        self.fillWithMultipliers()
        
    def checkIfWordInBoard(self, word, xy):
        if xy-1 + len(word) > 15:
            raise Exception("Palabra no entra en tablero!")
        else:
            return True

    def checkIfEmpty(self):
        res = []
        check = 0;
        for _ in self.grid:
            for x in _:
               res.append(x)
        for _ in res:
            if _.tile:
                check+=1
        if check > 0:
            return False;    
        else:
            return True;
        
    @staticmethod
    def calculateWordValue(word):
        result = 0;
        mulres = 1; ## creating a variable for adding whatever the _.multiplier throws back 
        for _ in word:
            if _.multiplier_type=="letter":
                result += _.tile.value * _.multiplier
            elif _.multiplier == "" or _.multiplier_type == "":
                result += _.tile.value 
            elif _.multiplier_type=="word":
                mulres = _.multiplier
                result += _.tile.value
        return mulres * result ## multiplying the result when the score is already added

    def validate_word_inside_board(self, word, location, orientation):
        (x, y) = location
        if orientation == "H" or orientation == "h":
            return self.checkIfWordInBoard(word, y)
        elif orientation == "V" or orientation == "v":
            return self.checkIfWordInBoard(word, x)

    def isEmpty(self):
        return self.checkIfEmpty()
    
    def applyMultipliersToCoords(self, Coords, multiplier, multiplier_type):
        for _ in Coords:
            (x, y) = _
            self.grid[x-1][y-1].multiplier, self.grid[x-1][y-1].multiplier_type  = multiplier, multiplier_type

    def deleteThenAddTile(self, x, y, tile):
        self.grid[x-1][y-1].noneTile()
        self.justAddTile(x, y, tile)

    def justAddTile(self, x, y, tile):
        self.grid[x-1][y-1].addTile(tile)

    def fillWithMultipliers(self):
        unpacking = [(Multipliers.doubleLetter, 2, "letter"),
            (Multipliers.tripleletter, 3, "letter"),
            (Multipliers.doubleWord, 2, "word"),
            (Multipliers.tripleWord, 3, "word")]
        for z in unpacking:
            self.applyMultipliersToCoords(*z)
            
    def addTileToCell(self, x, y, tile=Tile):
        if self.getCellInBoard(x, y).tile == "" or self.getCellInBoard(x, y).tile.letter == tile.letter:
            self.deleteThenAddTile(x, y, tile)
        else:
            raise Exception("Palabra mal puesta!")

    def getCellInBoard(self, x, y):
        return self.grid[x-1][y-1]