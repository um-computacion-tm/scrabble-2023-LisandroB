import unittest
from game.board import Board
from game.models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)
        
    def test_word_inside_board(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (5, 4), "H"), True)
    
    def test_word_out_of_board(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (14, 4), "H"), False)

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.isEmpty(), True)

    def test_board_is_not_empty(self):
        board = Board()
        board.addTileToBoard(7, 7, Tile('C', 1))
        board.addTileToBoard(8, 7, Tile('A', 1))
        board.addTileToBoard(9, 7, Tile('S', 1))
        board.addTileToBoard(10, 7, Tile('A', 1))
        self.assertEqual(board.isEmpty(), False)

    def test_addTileInCorner(self):
        board = Board()
        board.addTileToBoard(15, 15, Tile('C', 1))
        self.assertEqual(board.isEmpty(), False)
    
    def test_boardDoubleLetterMultiplier(self):
        board = Board()
        self.assertEqual(board.getTileInBoard(15, 4).multiplier, 2)
        self.assertEqual(board.getTileInBoard(15, 4).multiplier_type, "letter")

    # este test se rompe, por qué el valor no es el mismo?
    # doubleWord de Multipliers lo está overrideando
    """ 
    def test_boardDoubleLetterMultiplier2(self):
        board = Board()
        self.assertEqual(board.getTileInBoard(7, 7).multiplier, 2)
        self.assertEqual(board.getTileInBoard(7, 7).multiplier_type, "letter")
    """
    def test_boardTripleLetterMultiplier(self):
        board = Board()
        self.assertEqual(board.getTileInBoard(14, 6).multiplier, 3)
        self.assertEqual(board.getTileInBoard(14, 6).multiplier_type, "letter")

    def test_boardTripleLetterMultiplier2(self):
        board = Board()
        self.assertEqual(board.getTileInBoard(13, 8).multiplier, 3)
        self.assertEqual(board.getTileInBoard(13, 8).multiplier_type, "letter")

    def test_boardDoubleWordMultiplier(self):
        board = Board()
        self.assertEqual(board.getTileInBoard(14, 2).multiplier, 2)
        self.assertEqual(board.getTileInBoard(14, 2).multiplier_type, "word")

    def test_boardTripleWordMultiplier(self):
        board = Board()
        self.assertEqual(board.getTileInBoard(0, 0).multiplier, 3)
        self.assertEqual(board.getTileInBoard(0, 0).multiplier_type, "word")
        
    def test_boardTripleWordMultiplier2(self):
        board = Board()
        self.assertEqual(board.getTileInBoard(0, 0).multiplier, 3)
        self.assertEqual(board.getTileInBoard(0, 0).multiplier_type, "word")
        
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (7, 4), "H"), True)

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (13, 4), "H"), False)

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (4, 7), "V"), True)

    def test_boardEmptyPlaceWrongVerticalWord(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (6, 11), "V"), False)
    
    def test_boardNotEmptyPlaceRightHorizontalWord(self):
        board = Board()
        board.addTileToBoard(7, 7, Tile('C', 1))
        board.addTileToBoard(8, 7, Tile('A', 1))
        board.addTileToBoard(9, 7, Tile('S', 1))
        board.addTileToBoard(15, 7, Tile('A', 1))
        self.assertEqual(board.isEmpty(), False)
        self.assertEqual(board.validate_word_inside_board("Facultad", (6, 6), "H"), True)
    
    def test_showBoard(self):
        board = Board()
        board.showBoard()
if __name__ == '__main__':
    unittest.main()
