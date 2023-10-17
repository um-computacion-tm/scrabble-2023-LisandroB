import unittest
from game.board import Board
from game.cell import Cell
from game.models import Tile

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(tile=Tile('C', 1),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('S', 2),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
        ]
        value = Board.calculateWordValue(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        word = [
            Cell(tile=Tile('C', 1),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
            Cell(
                tile=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
        ]
        value = Board.calculateWordValue(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        word = [
            Cell(tile=Tile('C', 1),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
            Cell(
                tile=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
        ]
        value = Board.calculateWordValue(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                tile=Tile('C', 1)
            ),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
            Cell(
                tile=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
        ]
        value = Board.calculateWordValue(word)
        self.assertEqual(value, 14)

    def test_with_different_word(self):
        word = [
            Cell(tile=Tile('C', 1),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('A', 1),
                multiplier=2,
                multiplier_type='letter'
            ),
            Cell(
                tile=Tile('Z', 10),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(tile=Tile('U', 1),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('E', 1),
                multiplier="",
                multiplier_type=""),
            Cell(tile=Tile('L', 1),
                multiplier=3,
                multiplier_type='letter'
            ),
            Cell(tile=Tile('A', 1),
                multiplier="",
                multiplier_type=""),
        ]
        value = Board.calculateWordValue(word)
        self.assertEqual(value, 38)

if __name__ == '__main__':
    unittest.main()
