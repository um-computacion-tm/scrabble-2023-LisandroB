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
        with self.assertRaises(Exception):
            board.validate_word_inside_board("Facultad", (4, 14), "H")

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual(board.isEmpty(), True)

    def test_board_is_not_empty(self):
        board = Board()
        board.addTileToCell(7, 7, Tile('C', 1))
        board.addTileToCell(8, 7, Tile('A', 1))
        board.addTileToCell(9, 7, Tile('S', 1))
        board.addTileToCell(10, 7, Tile('A', 1))
        self.assertEqual(board.isEmpty(), False)

    def test_addTileToCell(self):
        board = Board()
        board.addTileToCell(15, 15, Tile('C', 1))
        self.assertEqual(board.getCellInBoard(15, 15).tile.letter, "C")
        board.addTileToCell(15, 15, Tile('C', 1))
        self.assertEqual(board.getCellInBoard(15, 15).tile.letter, "C")

    def test_addTileInCorner(self):
        board = Board()
        board.addTileToCell(15, 15, Tile('C', 1))
        self.assertEqual(board.isEmpty(), False)
    
    def test_boardDoubleLetterMultiplier(self):
        board = Board()
        self.assertEqual(board.getCellInBoard(15, 4).multiplier, 2)
        self.assertEqual(board.getCellInBoard(15, 4).multiplier_type, "letter")

    def test_boardDoubleLetterMultiplier2(self):
        board = Board()
        self.assertEqual(board.getCellInBoard(7, 7).multiplier, 2)
        self.assertEqual(board.getCellInBoard(7, 7).multiplier_type, "letter")
    
    def test_boardTripleLetterMultiplier(self):
        board = Board()
        self.assertEqual(board.getCellInBoard(14, 6).multiplier, 3)
        self.assertEqual(board.getCellInBoard(14, 6).multiplier_type, "letter")

    def test_boardTripleLetterMultiplier2(self):
        board = Board()
        self.assertEqual(board.getCellInBoard(14, 6).multiplier, 3)
        self.assertEqual(board.getCellInBoard(14, 6).multiplier_type, "letter")

    def test_boardDoubleWordMultiplier(self):
        board = Board()
        self.assertEqual(board.getCellInBoard(14, 2).multiplier, 2)
        self.assertEqual(board.getCellInBoard(14, 2).multiplier_type, "word")

    def test_boardTripleWordMultiplier(self):
        board = Board()
        self.assertEqual(board.getCellInBoard(0, 0).multiplier, 3)
        self.assertEqual(board.getCellInBoard(0, 0).multiplier_type, "word")
        
    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (7, 4), "H"), True)

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        with self.assertRaises(Exception):
            board.validate_word_inside_board("Facultad", (4, 13), "H")

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (7, 4), "V"), True)

    def test_boardEmptyPlaceWrongVerticalWord(self):
        board = Board()
        with self.assertRaises(Exception):
            board.validate_word_inside_board("Facultad", (11, 6), "V")

    def test_boardNotEmptyPlaceRightHorizontalWord(self):
        board = Board()
        board.addTileToCell(7, 7, Tile('C', 1))
        board.addTileToCell(8, 7, Tile('A', 1))
        board.addTileToCell(9, 7, Tile('S', 1))
        board.addTileToCell(15, 7, Tile('A', 1))
        self.assertEqual(board.isEmpty(), False)
        self.assertEqual(board.validate_word_inside_board("Facultad", (6, 6), "H"), True)

    def test_wrongTileToCell(self):
        board = Board()
        board.addTileToCell(8, 8, Tile("A", 1))
        self.assertIsNone(board.addTileToCell(8, 8, Tile(123, 1)))

if __name__ == '__main__':
    unittest.main()