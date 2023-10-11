from game.cell import Cell
from game.models import Tile
from game.multipliers import Multipliers

class Board:
    def __init__(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]
        self.fillWithMultipliers()
        
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
            elif _.multiplier == None or _.multiplier_type == None:
                result += _.tile.value 
            elif _.multiplier_type=="word":
                mulres = _.multiplier
                result += _.tile.value
        return mulres * result ## multiplying the result when the score is already added

    def validate_word_inside_board(self, word, location, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        if orientation == "H":
            if position_x + len_word > 15:
                return False
            else:
                return True
        elif orientation == "V":
            if position_y + len_word > 15:
                return False;
            else:
                return True;

    def isEmpty(self):
        return self.checkIfEmpty()
    
    def applyMultipliersToCoords(self, Coords, multiplier, multiplier_type):
        for _ in Coords:
            (x, y) = _
            self.grid[x-1][y-1].multiplier = multiplier
            self.grid[x-1][y-1].multiplier_type =  multiplier_type

    def fillWithMultipliers(self):
        unpacking = [(Multipliers.doubleLetter, 2, "letter"),
            (Multipliers.tripleletter, 3, "letter"),
            (Multipliers.doubleWord, 2, "word"),
            (Multipliers.tripleWord, 3, "word")]
        for z in unpacking:
            self.applyMultipliersToCoords(*z)
            
    def addTileToBoard(self, x, y, tile=Tile):
        self.grid[x-1][y-1].addValue(tile)
    
    def getTileInBoard(self, x, y):
        return self.grid[x-1][y-1]