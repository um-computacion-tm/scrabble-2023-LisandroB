from game.cell import Cell
from game.models import Tile
class Board:
    def __init__(self):
        self.grid = [[Cell(1, "", "") for _ in range(15)] for _ in range(15)]

    @staticmethod
    def calculate_word_value(word):
        result = 0;
        mulres = 1; ## creating a variable for adding whatever the _.multiplier throws back 
        for _ in word:
            if _.multiplier_type=="letter":
                result += _.letter.value * _.multiplier
            elif _.multiplier == None or _.multiplier_type == None:
                result += _.letter.value 
            elif _.multiplier_type=="word":
                mulres = _.multiplier
                result += _.letter.value
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
        else:
            pass

    def is_empty(self):
        print(self.grid[0][1].letter(Tile("A", 1)))
        for _ in self.grid:
            for x in _:
                if x.letter == "":
                    print("Sí!")
                else: 
                    print("No!")