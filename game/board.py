from game.cell import Cell
from game.models import Tile
from game.multipliers import Multipliers

class Board:
    def __init__(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]
        self.fillWithMultipliers()
        
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

    def fillWithMultipliers(self):
        for _ in Multipliers.doubleLetter:
            (x, y) = _
            self.grid[x-1][y-1].multiplier = 2
            self.grid[x-1][y-1].multiplier_type = "letter"
        for _ in Multipliers.tripleletter:
            (x, y) = _
            self.grid[x-1][y-1].multiplier = 3
            self.grid[x-1][y-1].multiplier_type = "letter"
        for _ in Multipliers.doubleWord:
            (x, y) = _
            self.grid[x-1][y-1].multiplier = 2
            self.grid[x-1][y-1].multiplier_type = "word"
        for _ in Multipliers.tripleWord:
            (x, y) = _
            self.grid[x-1][y-1].multiplier = 3
            self.grid[x-1][y-1].multiplier_type = "word"
            
    def addTile(self, x, y, tile=Tile):
        self.grid[x-1][y-1].addValue(tile)
    
    def getTile(self, x, y):
        return self.grid[x-1][y-1]