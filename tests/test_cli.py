import unittest;
from unittest.mock import patch, MagicMock
from game.cli import *
from game.board import Board
from game.models import Tile

class testCli(unittest.TestCase):
    # se spawnea una instancia de board y game,
    # se agregan tiles a las celdas específicas, 
    # se muestra el board y se confirma que el board se creó
    def test_place_word_cross_vertical_fine(self):
        board = Board()
        board.addTileToCell(7, 7, Tile("C", 1))
        board.addTileToCell(7, 8, Tile("A", 1))
        board.addTileToCell(7, 9, Tile("S", 1))
        board.addTileToCell(7, 10, Tile("A", 1))
        self.assertTrue(board.validate_word_inside_board("facultad", (2, 11), "V"))

    def test_place_word_wrong(self):
        board = Board()
        with self.assertRaises(Exception):
            board.validate_word_inside_board("facultad", (2, 11), "H")

    @patch('builtins.input', side_effect=[0])
    def test_wrongStart(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()

    @patch('builtins.input', side_effect=[3])
    def test_initStartPlayerCount(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()

    @patch('builtins.input', side_effect=[2, "1", "papa", 8, 8, "V"])
    def test_firstTurnWordNotFound(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()
            
    @patch('builtins.input', side_effect=[4, "3"])
    def test_firstTurnShuffle(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()
    
    @patch('builtins.input', side_effect=[3, "4"])
    def test_firstTurnThenPass(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()
    
    @patch('builtins.input', side_effect=[2, "5", "Y"])
    def test_firstTurnThenExit(self, mock):
        game = Game()
        game.cli()
    
    @patch('builtins.input', side_effect=[3, "5", "n"])
    def test_firstTurnThenExitThenRegret(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()

    @patch('builtins.input', side_effect=[0, 4, "a"])
    def test_firstTurnThenWrongInput(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()
        
    @patch('builtins.input', side_effect=[2, "2", [1, 5]])
    def test_firstTurnThenSecondChoice(self, mock):
        game = Game()
        with self.assertRaises(Exception):
            game.cli()
    
    #wip
    @patch('builtins.input', side_effect=[2, "1", "papa", 8, 8, "V"])
    def test_firstTurnThenEnterWord(self, mock):
        game = Game()
        scrabbleGame = ScrabbleGame(3)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = MagicMock(return_value=[
            Tile("C", 8), 
            Tile("O", 1), 
            Tile("N", 8), 
            Tile("O", 3),
            Tile("S", 1), 
            Tile("D", 1), 
            Tile("B", 1)
        ])
        with self.assertRaises(Exception):
            game.cli()

if __name__ == '__main__':
    unittest.main()