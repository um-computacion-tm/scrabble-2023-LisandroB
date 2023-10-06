import unittest
from game.board import Board
from game.models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]),15)
        
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
        board.addTile(7, 7, Tile('C', 1))
        board.addTile(8, 7, Tile('A', 1))
        board.addTile(9, 7, Tile('S', 1))
        board.addTile(10, 7, Tile('A', 1))
        self.assertEqual(board.isEmpty(), False)

    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (7, 4), "H"), True)

    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (13, 4), "H"), False)

    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (4, 7), "V"), True)

    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        self.assertEqual(board.validate_word_inside_board("Facultad", (6, 11), "V"), False)
    
    def test_place_word_not_empty_board_horizontal_fine(self):
        board = Board()
        board.addTile(7, 7, Tile('C', 1))
        board.addTile(8, 7, Tile('A', 1))
        board.addTile(9, 7, Tile('S', 1))
        board.addTile(10, 7, Tile('A', 1))
        self.assertEqual(board.isEmpty(), False)
        self.assertEqual(board.validate_word_inside_board("Facultad", (6, 6), "H"), True)

if __name__ == '__main__':
    unittest.main()
