import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.models import Tile
from game.cli import Game 

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        self.assertIsNotNone(scrabbleGame.board)
        self.assertEqual(len(scrabbleGame.players), 3)
        self.assertIsNotNone(scrabbleGame.bagTiles)
    
    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[0]
    
    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 4 jugadores, luego del jugador 3, le toca al jugador 4
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[3]
    
    def test_validateWordRight(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("G", 4), 
            Tile("A", 1), 
            Tile("F", 1), 
            Tile("P", 1), 
            Tile("P", 1),
            Tile("A", 1), 
            Tile("A", 1)
        ]
        self.assertEqual(scrabbleGame.validateWord("papa", (8, 7), "V"), True)    
    
    def test_getScore(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("G", 4), 
            Tile("A", 1), 
            Tile("F", 1), 
            Tile("P", 1), 
            Tile("P", 1),
            Tile("A", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("papa", (8, 7), "V")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("H", 1), 
            Tile("P", 1), 
            Tile("I", 1), 
            Tile("A", 4),
            Tile("A", 1)
        ]
        scrabbleGame.putWord("chipa", (5, 6), "H")
        self.assertEqual(scrabbleGame.getScore(), True)

    def test_validateWordFalse(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.current_player.tiles = [
            Tile("P", 1), 
            Tile("A", 1), 
            Tile("A", 1), 
            Tile("P", 1),
            Tile("G", 4), 
            Tile("F", 1), 
            Tile("A", 1)
        ]
        self.assertEqual(scrabbleGame.validateWord("empanada", (15, 7), "H"), False)
    
    def test_lastPlayer(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[-1]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[0]

    def test_validateTurn(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("R", 1), 
            Tile("P", 1), 
            Tile("R", 1), 
            Tile("A", 4),
            Tile("O", 1)
        ]
        self.assertEqual(scrabbleGame.validateTurn("carro", (3, 2), "V"), True)

    def test_validateTurnRight(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.current_player.tiles = [
            Tile("G", 1), 
            Tile("I", 1), 
            Tile("R", 1), 
            Tile("R", 1), 
            Tile("R", 1), 
            Tile("A", 4),
            Tile("O", 1)
        ]
        self.assertEqual(scrabbleGame.validateTurn("reloj", (3, 2), "V"), False)

    def test_validateTurnWrong(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.bagTiles.tiles = []
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("R", 1), 
            Tile("P", 1), 
            Tile("R", 1), 
            Tile("A", 4),
            Tile("O", 1)
        ]
        self.assertEqual(scrabbleGame.validateTurn("carro", (3, 2), "V"), False)

    def test_putWord(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("H", 1), 
            Tile("P", 1), 
            Tile("I", 1), 
            Tile("A", 4),
            Tile("A", 1)
        ]
        scrabbleGame.putWord("chipa", (5, 6), "H")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(5, 6).tile), "C")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(5, 7).tile), "H")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(5, 8).tile), "I")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(5, 9).tile), "P")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(5, 10).tile), "A")

    def test_putWordAgain(self):
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.current_player.tiles = [
           Tile("U", 4),
           Tile("H", 1), 
           Tile("E", 1), 
           Tile("A", 1), 
           Tile("E", 1), 
           Tile("L", 1), 
           Tile("G", 1)
       ]
        scrabbleGame.putWord("huelga", (3, 2), "V")
        self.assertTrue(scrabbleGame.board.getCellInBoard(3, 2).tile, "H:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(4, 2).tile, "U:4")
        self.assertTrue(scrabbleGame.board.getCellInBoard(5, 2).tile, "E:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(6, 2).tile, "L:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(7, 2).tile, "G:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(8, 2).tile, "A:1")

    def test_putWordFalse(self):
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.current_player.tiles = [
           Tile("N", 1), 
           Tile("R", 1),
           Tile("B", 1), 
           Tile("I", 4),
           Tile("A", 1), 
           Tile("C", 1), 
           Tile("A", 1)
       ]
        scrabbleGame.putWord("carro", (3, 2), "V")
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(3, 2).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(4, 2).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(5, 2).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(6, 2).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(7, 2).tile), 0)

    def test_putWordFalseAgain(self):
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.current_player.tiles = [
           Tile("N", 1), 
           Tile("R", 1),
           Tile("B", 1), 
           Tile("I", 4),
           Tile("A", 1), 
           Tile("C", 1), 
           Tile("O", 1)
       ]
        scrabbleGame.putWord("barca", (3, 2), "H")
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(3, 2).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(3, 3).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(3, 4).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(3, 5).tile), 0)
        self.assertEqual(len(scrabbleGame.board.getCellInBoard(3, 6).tile), 0)

    def test_putWordGetScore(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
           Tile("U", 1),
           Tile("H", 2), 
           Tile("E", 1), 
           Tile("A", 1), 
           Tile("E", 1), 
           Tile("L", 8), 
           Tile("G", 2)
        ]
        scrabbleGame.putWord("huelga", (3, 2), "V")
        self.assertEqual(scrabbleGame.current_player.score, 31)

    def test_validateGameHuh(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.current_player.tiles = [
            Tile("D", 2), 
            Tile("A", 1), 
            Tile("G", 2), 
            Tile("H", 4),
            Tile("T", 1), 
            Tile("X", 8), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("gata", (8, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("N", 1), 
            Tile("N", 1), 
            Tile("A", 1),
            Tile("N", 1), 
            Tile("O", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("nota", (10, 6), "h")


    def test_validateGameFixed(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.current_player.tiles = [
            Tile("D", 2), 
            Tile("A", 1), 
            Tile("G", 2), 
            Tile("F", 4),
            Tile("S", 1), 
            Tile("A", 8), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("gafas", (8, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("U", 1), 
            Tile("N", 1), 
            Tile("E", 1), 
            Tile("A", 1),
            Tile("G", 1), 
            Tile("O", 1), 
            Tile("S", 1)
        ]
        scrabbleGame.putWord("fuegos", (8, 8), "v")

    def test_validateGameVertical(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.current_player.tiles = [
            Tile("N", 1), 
            Tile("O", 1), 
            Tile("H", 4), 
            Tile("O", 1),
            Tile("R", 8), 
            Tile("X", 8), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("honor", (8, 8), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("O", 1), 
            Tile("E", 1), 
            Tile("A", 1), 
            Tile("J", 8),
            Tile("N", 1), 
            Tile("O", 1), 
            Tile("L", 1)
        ]
        scrabbleGame.putWord("ojo", (8, 9), "v")
    
    def test_validateGameHorizontal(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.current_player.tiles = [
            Tile("T", 8), 
            Tile("E", 1), 
            Tile("R", 8), 
            Tile("C", 3),
            Tile("O", 1), 
            Tile("X", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("terco", (8, 8), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("U", 1), 
            Tile("U", 1), 
            Tile("N", 1), 
            Tile("A", 8),
            Tile("I", 1), 
            Tile("E", 1), 
            Tile("H", 4)
        ]
        scrabbleGame.putWord("tan", (8, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.current_player.tiles = [
            Tile("E", 1), 
            Tile("J", 8), 
            Tile("M", 3), 
            Tile("D", 2),
            Tile("O", 1), 
            Tile("E", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("moda", (9, 5), "h")
        game.showBoard(scrabbleGame.board)

if __name__ == '__main__':
    unittest.main()