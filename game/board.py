from game.cell import Cell
from game.models import Tile
class Board:
    def __init__(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]

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
        doubleLetter = [(4, 1), 
                        (12, 1),
                        (1, 4),
                        (8, 4),
                        (15, 4),
                        (3, 7),
                        (7, 7),
                        (9, 7),
                        (13, 7),
                        (4, 10),
                        (12, 10),
                        (0, 12),
                        (7, 12),
                        (14, 12),
                        (3, 15),
                        (11, 15)]
        tripleletter = [(6, 2),
                        (10, 2),
                        (2, 6),
                        (6, 6), 
                        (10, 6), 
                        (14, 6), 
                        (1, 8), 
                        (5, 8), 
                        (9, 8), 
                        (13, 8), 
                        (2, 10), 
                        (6, 10), 
                        (10, 10), 
                        (14, 10), 
                        (6, 14), 
                        (10, 14)]
        doubleWord = [(1, 1), 
                      (8, 1), 
                      (15, 1), 
                      (2, 2), 
                      (14, 2), 
                      (3, 3), 
                      (13, 3), 
                      (4, 4), 
                      (12, 4), 
                      (7, 7), 
                      (11, 7), 
                      (4, 12), 
                      (12, 12), 
                      (1, 15), 
                      (8, 15), 
                      (15, 15)]
        tripleWord = [(0, 0), 
                    (7, 0), 
                    (14, 0), 
                    (0, 7), 
                    (14, 7), 
                    (0, 14), 
                    (7, 14), 
                    (14, 14)]
        for _ in doubleLetter:
            print(_)
            
    def addTile(self, x, y, tile=Tile):
        self.grid[x][y].addValue(tile)