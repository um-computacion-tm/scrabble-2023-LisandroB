import unittest;
from game.cli import Game
from game.board import Board
from game.models import Tile

class testCli(unittest.TestCase):
    # se spawnea una instancia de board y game,
    # se agregan tiles a las celdas específicas, 
    # se muestra el board y se confirma que el board se creó
    def test_place_word_cross_vertical_fine(self):
        board = Board()
        client = Game()
        board.addTileToCell(7, 7, Tile("C", 1))
        board.addTileToCell(7, 8, Tile("A", 1))
        board.addTileToCell(7, 9, Tile("S", 1))
        board.addTileToCell(7, 10, Tile("A", 1))
        client.showBoard(board)
        self.assertTrue(board.validate_word_inside_board("facultad", (11, 2), "V"))

    def test_place_word_wrong(self):
        board = Board()
        self.assertFalse(board.validate_word_inside_board("facultad", (2, 11), "V"))

if __name__ == '__main__':
    unittest.main() 