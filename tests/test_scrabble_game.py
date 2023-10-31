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
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("G", 4), 
            Tile("A", 1), 
            Tile("F", 1), 
            Tile("P", 1), 
            Tile("P", 1),
            Tile("A", 1), 
            Tile("A", 1)
        ]
        self.assertEqual(scrabbleGame.validateWord("papa", (7, 8), "V"), True) 

    def test_validateWordWrong(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("G", 4), 
            Tile("A", 1), 
            Tile("F", 1), 
            Tile("P", 1), 
            Tile("P", 1),
            Tile("A", 1), 
            Tile("A", 1)
        ]
        with self.assertRaises(Exception):
            scrabbleGame.validateWord("palco", (8, 7), "V")
    
    def test_putWordWrong(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("G", 4), 
            Tile("A", 1), 
            Tile("F", 1), 
            Tile("P", 1), 
            Tile("P", 1),
            Tile("A", 1), 
            Tile("A", 1)
        ]
        with self.assertRaises(Exception):
            scrabbleGame.putWord("palco", (8, 7), "V")

    def test_getScore(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("G", 4), 
            Tile("A", 1), 
            Tile("F", 1), 
            Tile("P", 1), 
            Tile("P", 1),
            Tile("A", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("papa", (8, 8), "V")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("H", 1), 
            Tile("P", 1), 
            Tile("I", 1), 
            Tile("A", 4),
            Tile("A", 1)
        ]
        scrabbleGame.putWord("chipa", (8, 5), "H")
        self.assertIsNone(scrabbleGame.getScore(), True)

    def test_validateWordFalse(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("P", 1), 
            Tile("A", 1), 
            Tile("A", 1), 
            Tile("P", 1),
            Tile("G", 4), 
            Tile("F", 1), 
            Tile("A", 1)
        ]
        with self.assertRaises(Exception):
            scrabbleGame.validateWord("empanada", (15, 7), "H")
    
    def test_lastPlayer(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[-1]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[0]

    def test_validateTurn(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("R", 1), 
            Tile("P", 1), 
            Tile("R", 1), 
            Tile("A", 4),
            Tile("O", 1)
        ]
        self.assertEqual(scrabbleGame.validateTurn(), True)

    def test_validateTurnWrong(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
        ]
        with self.assertRaises(Exception):
            scrabbleGame.validateTurn("carro", (3, 2), "V")
    
    def test_wrongTurnLowTiles(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.bagTiles.tiles = []
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("R", 1), 
            Tile("O", 1)
        ]
        with self.assertRaises(Exception):
            scrabbleGame.validateTurn("carro", (8, 8), "V")

    def test_wrongTurnEndGame(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 3), 
            Tile("M", 2), 
            Tile("C", 1), 
            Tile("I", 1),
            Tile("E", 1), 
            Tile("L", 2), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("miel", (8, 7), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("P", 8), 
            Tile("E", 1), 
            Tile("E", 8),
            Tile("C", 5), 
            Tile("E", 1), 
            Tile("C", 1)
        ]
        scrabbleGame.putWord("pie", (7, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("C", 8), 
            Tile("A", 1), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("L", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("piel", (7, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("E", 8), 
            Tile("C", 1), 
            Tile("E", 8),
            Tile("C", 5), 
            Tile("V", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("vale", (6, 10), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("C", 8), 
            Tile("A", 1), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("E", 1), 
            Tile("T", 1)
        ]
        scrabbleGame.putWord("cela", (10, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("C", 1), 
            Tile("E", 8), 
            Tile("C", 5), 
            Tile("O", 8),
            Tile("U", 1), 
            Tile("U", 1)
        ]
        scrabbleGame.putWord("eco", (9, 6), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("T", 1),
            Tile("O", 8), 
            Tile("A", 1), 
            Tile("E", 1), 
        ]
        scrabbleGame.putWord("tío", (11, 4), "h")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 2), 
            Tile("C", 1), 
            Tile("O", 8), 
            Tile("U", 5), 
            Tile("U", 8),
            Tile("O", 8), 
            Tile("R", 1), 
        ]
        scrabbleGame.putWord("turco", (11, 4), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("Z", 8),
            Tile("O", 8), 
            Tile("A", 1), 
            Tile("E", 1), 
            Tile("Q", 5), 
            Tile("R", 1),
        ]
        scrabbleGame.putWord("voraz", (6, 10), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("E", 1), 
            Tile("E", 8), 
            Tile("T", 5), 
            Tile("F", 8),
            Tile("R", 8), 
            Tile("A", 1), 
        ]
        scrabbleGame.putWord("fuerte", (12, 3), "h")
        scrabbleGame.bagTiles.tiles = []
        scrabbleGame.current_player.tiles = []
        with self.assertRaises(AssertionError):
            scrabbleGame.validateTurn()

    def test_wrongTurnNoTilesEndGame(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 3), 
            Tile("M", 2), 
            Tile("C", 1), 
            Tile("I", 1),
            Tile("E", 1), 
            Tile("L", 2), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("miel", (8, 7), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("P", 8), 
            Tile("E", 1), 
            Tile("E", 8),
            Tile("C", 5), 
            Tile("E", 1), 
            Tile("C", 1)
        ]
        scrabbleGame.putWord("pie", (7, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("C", 8), 
            Tile("A", 1), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("L", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("piel", (7, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("E", 8), 
            Tile("C", 1), 
            Tile("E", 8),
            Tile("C", 5), 
            Tile("V", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("vale", (6, 10), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("C", 8), 
            Tile("A", 1), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("E", 1), 
            Tile("T", 1)
        ]
        scrabbleGame.putWord("cela", (10, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("C", 1), 
            Tile("E", 8), 
            Tile("C", 5), 
            Tile("O", 8),
            Tile("U", 1), 
            Tile("U", 1)
        ]
        scrabbleGame.putWord("eco", (9, 6), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("T", 1),
            Tile("O", 8), 
            Tile("A", 1), 
            Tile("E", 1), 
        ]
        scrabbleGame.putWord("tío", (11, 4), "h")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 2), 
            Tile("C", 1), 
            Tile("O", 8), 
            Tile("U", 5), 
            Tile("U", 8),
            Tile("O", 8), 
            Tile("R", 1), 
        ]
        scrabbleGame.putWord("turco", (11, 4), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("Z", 8),
            Tile("O", 8), 
            Tile("A", 1), 
            Tile("E", 1), 
            Tile("Q", 5), 
            Tile("R", 1),
        ]
        scrabbleGame.putWord("voraz", (6, 10), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("E", 1), 
            Tile("E", 8), 
            Tile("T", 5), 
            Tile("F", 8),
            Tile("R", 8), 
            Tile("A", 1), 
        ]
        scrabbleGame.putWord("fuerte", (12, 3), "h")
        scrabbleGame.bagTiles.tiles = []
        with self.assertRaises(AssertionError):
            scrabbleGame.validateTurn()

    def test_putWord(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("C", 1), 
            Tile("H", 1), 
            Tile("P", 1), 
            Tile("I", 1), 
            Tile("A", 4),
            Tile("A", 1)
        ]
        scrabbleGame.putWord("chipa", (8, 8), "H")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(8, 8).tile), "C")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(8, 9).tile), "H")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(8, 10).tile), "I")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(8, 11).tile), "P")
        self.assertEqual(str(scrabbleGame.board.getCellInBoard(8, 12).tile), "A")

    def test_putWordAgain(self):
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
           Tile("U", 4),
           Tile("H", 1), 
           Tile("E", 1), 
           Tile("A", 1), 
           Tile("E", 1), 
           Tile("L", 1), 
           Tile("G", 1)
       ]
        scrabbleGame.putWord("huelga", (8, 8), "V")
        self.assertTrue(scrabbleGame.board.getCellInBoard(8, 8).tile, "H:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(9, 8).tile, "U:4")
        self.assertTrue(scrabbleGame.board.getCellInBoard(10, 8).tile, "E:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(11, 8).tile, "L:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(12, 8).tile, "G:1")
        self.assertTrue(scrabbleGame.board.getCellInBoard(13, 8).tile, "A:1")

    def test_putWordFalse(self):
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
       ]
        with self.assertRaises(Exception):
            scrabbleGame.validateTurn("reloj", (3, 2), "V")
        
    def test_putWordFalseAgain(self):
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
           Tile("N", 1), 
           Tile("R", 1),
           Tile("B", 1), 
           Tile("I", 4),
           Tile("A", 1), 
           Tile("C", 1), 
           Tile("O", 1)
       ]
        with self.assertRaises(Exception):
            scrabbleGame.putWord("barca", (3, 2), "H")
            
    def test_putWordGetScore(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
           Tile("U", 1),
           Tile("H", 2), 
           Tile("E", 1), 
           Tile("A", 1), 
           Tile("E", 1), 
           Tile("L", 8), 
           Tile("G", 2)
        ]
        scrabbleGame.putWord("huelga", (8, 8), "V")
        self.assertEqual(scrabbleGame.current_player.score, 17)

    def test_validateGameHuh(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
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
        scrabbleGame.next_turn()
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
        self.assertTrue(scrabbleGame.board.getCellInBoard(10, 7).tile)
        self.assertTrue(scrabbleGame.board.getCellInBoard(10, 7).tile)

    def test_validateGameFixed(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
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
        scrabbleGame.next_turn()
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
        self.assertTrue(scrabbleGame.board.getCellInBoard(9, 8).tile)

    def test_putWordThroughCenter(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("D", 2), 
            Tile("A", 1), 
            Tile("G", 2), 
            Tile("F", 4),
            Tile("S", 1), 
            Tile("A", 8), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("gafas", (8, 8), "h")
        game.showBoard(scrabbleGame.board)
        
    def test_putWordThroughCenterWrong(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("D", 2), 
            Tile("A", 1), 
            Tile("G", 2), 
            Tile("F", 4),
            Tile("S", 1), 
            Tile("A", 8), 
            Tile("A", 1)
        ]
        with self.assertRaises(Exception):
            scrabbleGame.putWord("gafas", (1, 1), "h")

    def test_validateGameVertical(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
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
        scrabbleGame.next_turn()
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
        self.assertTrue(scrabbleGame.board.getCellInBoard(10, 9).tile)
    
    def test_validateGameHorizontal1(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.next_turn()
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
        scrabbleGame.next_turn()
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
        scrabbleGame.next_turn()
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
        self.assertTrue(scrabbleGame.board.getCellInBoard(9, 8).tile)
        
    def test_validateGameHorizontalAndVertical(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 1), 
            Tile("D", 2), 
            Tile("T", 1), 
            Tile("E", 1),
            Tile("A", 1), 
            Tile("S", 1), 
            Tile("L", 1)
        ]
        scrabbleGame.putWord("salta", (8, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("T", 1), 
            Tile("R", 1), 
            Tile("S", 1), 
            Tile("U", 1),
            Tile("O", 1), 
            Tile("T", 1), 
            Tile("I", 1)
        ]
        scrabbleGame.putWord("trato", (6, 7), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("S", 1), 
            Tile("R", 1), 
            Tile("S", 1), 
            Tile("A", 1),
            Tile("G", 1), 
            Tile("T", 1), 
            Tile("X", 1)
        ]
        scrabbleGame.putWord("saltar", (8, 6), "h")
        self.assertTrue(scrabbleGame.board.getCellInBoard(8, 10).tile)

    def test_validateGameHorizontalAndVerticalWithDoubleLetter(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 3), 
            Tile("M", 2), 
            Tile("C", 1), 
            Tile("I", 1),
            Tile("E", 1), 
            Tile("L", 2), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("miel", (8, 7), "h")
        game.showBoard(scrabbleGame.board)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("P", 8), 
            Tile("E", 1), 
            Tile("E", 8),
            Tile("C", 5), 
            Tile("E", 1), 
            Tile("C", 1)
        ]
        scrabbleGame.putWord("pie", (7, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("C", 8), 
            Tile("A", 1), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("L", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("piel", (7, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("E", 8), 
            Tile("C", 1), 
            Tile("E", 8),
            Tile("C", 5), 
            Tile("V", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("vale", (6, 10), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("C", 8), 
            Tile("A", 1), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("E", 1), 
            Tile("T", 1)
        ]
        scrabbleGame.putWord("cela", (10, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 2), 
            Tile("C", 1), 
            Tile("E", 8), 
            Tile("C", 5), 
            Tile("O", 8),
            Tile("U", 1), 
            Tile("U", 1)
        ]
        scrabbleGame.putWord("eco", (9, 6), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("Z", 8),
            Tile("I", 5), 
            Tile("T", 1),
            Tile("O", 8), 
            Tile("A", 1), 
            Tile("E", 1), 
        ]
        scrabbleGame.putWord("tío", (11, 4), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 2), 
            Tile("C", 1), 
            Tile("O", 8), 
            Tile("U", 5), 
            Tile("U", 8),
            Tile("O", 8), 
            Tile("R", 1), 
        ]
        scrabbleGame.putWord("turco", (11, 4), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("Z", 8),
            Tile("O", 8), 
            Tile("A", 1), 
            Tile("E", 1), 
            Tile("Q", 5), 
            Tile("R", 1),
        ]
        scrabbleGame.putWord("voraz", (6, 10), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 2), 
            Tile("E", 1), 
            Tile("E", 8), 
            Tile("T", 5), 
            Tile("F", 8),
            Tile("R", 8), 
            Tile("A", 1), 
        ]
        scrabbleGame.putWord("fuerte", (12, 3), "h")
        self.assertTrue(scrabbleGame.board.getCellInBoard(12, 8).tile)

    def test_validateGameHorizontalConEñe(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("G", 8), 
            Tile("M", 1), 
            Tile("A", 8), 
            Tile("I", 3),
            Tile("H", 1), 
            Tile("E", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("magia", (8, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("U", 1), 
            Tile("E", 1), 
            Tile("A", 1), 
            Tile("A", 8),
            Tile("Ñ", 1), 
            Tile("E", 1), 
            Tile("C", 4)
        ]
        scrabbleGame.putWord("maña", (8, 6), "v")
        self.assertTrue(scrabbleGame.board.getCellInBoard(8, 9).tile)
    
    def test_validateGameHorizontalConTilde(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("D", 8), 
            Tile("J", 1), 
            Tile("E", 8), 
            Tile("L", 3),
            Tile("S", 1), 
            Tile("D", 1), 
            Tile("B", 1)
        ]
        scrabbleGame.putWord("del", (8, 7), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("I", 8), 
            Tile("O", 1), 
            Tile("H", 8), 
            Tile("R", 3),
            Tile("O", 1), 
            Tile("S", 1), 
            Tile("V", 1)
        ]
        scrabbleGame.putWord("oído", (6, 7), "v")
        self.assertTrue(scrabbleGame.board.getCellInBoard(8, 7).tile)
        
    def test_validateGameHorizontalConExtra(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("O", 1), 
            Tile("N", 8), 
            Tile("O", 3),
            Tile("S", 1), 
            Tile("D", 1), 
            Tile("B", 1)
        ]
        scrabbleGame.putWord("cono", (8, 7), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("T", 8), 
            Tile("A", 1), 
            Tile("N", 8), 
            Tile("R", 3),
            Tile("O", 1), 
            Tile("S", 1), 
            Tile("V", 1)
        ]
        scrabbleGame.putWord("tano", (5, 10), "v")
        self.assertTrue(scrabbleGame.board.getCellInBoard(8, 10).tile)

    def test_validateGameHorizontalConExtra(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("O", 1), 
            Tile("N", 8), 
            Tile("O", 3),
            Tile("S", 1), 
            Tile("D", 1), 
            Tile("B", 1)
        ]
        scrabbleGame.putWord("cono", (8, 7), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("T", 8), 
            Tile("A", 1), 
            Tile("N", 8), 
            Tile("R", 3),
            Tile("O", 1), 
            Tile("S", 1), 
            Tile("V", 1)
        ]
        scrabbleGame.putWord("tano", (5, 10), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("O", 1), 
            Tile("C", 8), 
            Tile("O", 3),
            Tile("S", 1), 
            Tile("D", 1), 
            Tile("B", 1)
        ]
        scrabbleGame.putWord("coco", (7, 8), "v")
        game.showBoard(scrabbleGame.board)
    
    def test_validateGameHorizontalConExtra(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("O", 1), 
            Tile("R", 8), 
            Tile("A", 3),
            Tile("B", 1), 
            Tile("O", 1), 
            Tile("M", 1)
        ]
        scrabbleGame.putWord("marco", (8, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("G", 1), 
            Tile("R", 8), 
            Tile("D", 3),
            Tile("O", 1), 
            Tile("L", 1), 
            Tile("P", 1)
        ]
        scrabbleGame.putWord("palco", (7, 7), "v")
        game.showBoard(scrabbleGame.board)
    
    def test_validateIsNextToTile(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("O", 1), 
            Tile("R", 8), 
            Tile("A", 3),
            Tile("B", 1), 
            Tile("O", 1), 
            Tile("M", 1)
        ]
        scrabbleGame.putWord("marco", (8, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("U", 1), 
            Tile("R", 8), 
            Tile("D", 3),
            Tile("O", 1), 
            Tile("L", 1), 
            Tile("P", 1)
        ]
        with self.assertRaises(Exception):
            scrabbleGame.putWord("crudo", (3, 2), "v")

    def test_validateWordWithTildeAndÑ(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("Ñ", 8), 
            Tile("A", 1), 
            Tile("N", 8), 
            Tile("D", 3),
            Tile("U", 1), 
            Tile("O", 1), 
            Tile("M", 1)
        ]
        scrabbleGame.putWord("ñandú", (8, 6), "h")
        scrabbleGame.next_turn()
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [
            Tile("Ñ", 8), 
            Tile("O", 1), 
            Tile("Q", 8), 
            Tile("U", 3),
            Tile("I", 1), 
            Tile("O", 1), 
            Tile("M", 1)
        ]
        scrabbleGame.putWord("ñoqui", (8, 6), "v")
        game.showBoard(scrabbleGame.board)
        
    def test_validateWordMuchasTildes(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 8), 
            Tile("V", 1), 
            Tile("I", 8), 
            Tile("O", 3),
            Tile("C", 1), 
            Tile("N", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("avión", (8, 8), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 8), 
            Tile("N", 1), 
            Tile("D", 8), 
            Tile("A", 3),
            Tile("U", 1), 
            Tile("O", 1), 
            Tile("M", 1)
        ]
        scrabbleGame.putWord("andá", (8, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 8), 
            Tile("R", 1), 
            Tile("E", 8), 
            Tile("A", 3),
            Tile("U", 1), 
            Tile("O", 1), 
            Tile("M", 1)
        ]
        scrabbleGame.putWord("área", (11, 8), "h")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 8), 
            Tile("R", 1), 
            Tile("A", 8), 
            Tile("Ñ", 3),
            Tile("U", 1), 
            Tile("A", 1), 
            Tile("M", 1)
        ]
        scrabbleGame.putWord("araña", (11, 11), "v")
        game.showBoard(scrabbleGame.board)
    
    def test_validateWord0a100(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=4)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("R", 8), 
            Tile("O", 1), 
            Tile("P", 8), 
            Tile("E", 3),
            Tile("N", 1), 
            Tile("U", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("pero", (8, 8), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("L", 8), 
            Tile("L", 1), 
            Tile("F", 8), 
            Tile("D", 3),
            Tile("M", 1), 
            Tile("C", 1), 
            Tile("N", 1)
        ]
        scrabbleGame.putWord("del", (7, 9), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("C", 8), 
            Tile("I", 1), 
            Tile("N", 8), 
            Tile("S", 3),
            Tile("E", 1), 
            Tile("O", 1), 
            Tile("R", 1)
        ]
        scrabbleGame.putWord("coso", (7, 11), "v")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("N", 8), 
            Tile("C", 1), 
            Tile("R", 8), 
            Tile("U", 3),
            Tile("S", 1), 
            Tile("I", 1), 
            Tile("S", 1)
        ]
        scrabbleGame.putWord("no", (10, 10), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("N", 8), 
            Tile("U", 1), 
            Tile("A", 8), 
            Tile("E", 3),
            Tile("Y", 1), 
            Tile("A", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("suya", (9, 11), "h")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("I", 8), 
            Tile("N", 1), 
            Tile("E", 8), 
            Tile("R", 3),
            Tile("Z", 1), 
            Tile("S", 1), 
            Tile("O", 1)
        ]
        scrabbleGame.putWord("sano", (8, 14), "v")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("R", 8), 
            Tile("S", 1), 
            Tile("I", 8), 
            Tile("H", 3),
            Tile("C", 1), 
            Tile("C", 1), 
            Tile("T", 1)
        ]
        scrabbleGame.putWord("sanos", (8, 14), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("N", 8), 
            Tile("E", 1), 
            Tile("O", 8), 
            Tile("A", 3),
            Tile("R", 1), 
            Tile("A", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("cenar", (7, 11), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("I", 8), 
            Tile("E", 1), 
            Tile("R", 8), 
            Tile("Z", 3),
            Tile("I", 1), 
            Tile("B", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("pire", (8, 8), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("R", 8), 
            Tile("I", 1), 
            Tile("H", 8), 
            Tile("C", 3),
            Tile("C", 1), 
            Tile("T", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("cierta", (11, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("O", 8), 
            Tile("A", 1), 
            Tile("E", 8), 
            Tile("T", 3),
            Tile("O", 1), 
            Tile("E", 1), 
            Tile("D", 1)
        ]
        scrabbleGame.putWord("toca", (9, 6), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("J", 8), 
            Tile("D", 1), 
            Tile("C", 8), 
            Tile("R", 3),
            Tile("V", 1), 
            Tile("G", 1), 
            Tile("N", 1)
        ]
        scrabbleGame.putWord("tocar", (9, 6), "v")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("Z", 8), 
            Tile("I", 1), 
            Tile("B", 8), 
            Tile("E", 3),
            Tile("A", 1), 
            Tile("E", 1), 
            Tile("T", 1)
        ]
        scrabbleGame.putWord("zar", (13, 4), "h")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("E", 8), 
            Tile("O", 1), 
            Tile("E", 8), 
            Tile("D", 3),
            Tile("C", 1), 
            Tile("M", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("remo", (11, 9), "v")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("I", 8), 
            Tile("B", 1), 
            Tile("E", 8), 
            Tile("E", 3),
            Tile("T", 1), 
            Tile("S", 1), 
            Tile("H", 1)
        ]
        scrabbleGame.putWord("zares", (13, 4), "h")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("H", 8), 
            Tile("C", 1), 
            Tile("O", 8), 
            Tile("O", 3),
            Tile("O", 1), 
            Tile("N", 1), 
            Tile("L", 1)
        ]
        scrabbleGame.putWord("loco", (10, 3), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("E", 8), 
            Tile("D", 1), 
            Tile("C", 8), 
            Tile("E", 3),
            Tile("A", 1), 
            Tile("O", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("celda", (8, 3), "v")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("I", 8), 
            Tile("B", 1), 
            Tile("H", 8), 
            Tile("P", 3),
            Tile("I", 1), 
            Tile("T", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("bicha", (8, 1), "h")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("H", 8), 
            Tile("O", 1), 
            Tile("O", 8), 
            Tile("N", 3),
            Tile("R", 1), 
            Tile("G", 1), 
            Tile("E", 1)
        ]
        scrabbleGame.putWord("robe", (6, 1), "v")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("E", 8), 
            Tile("O", 1), 
            Tile("A", 8), 
            Tile("L", 3),
            Tile("A", 1), 
            Tile("H", 1), 
            Tile("F", 1)
        ]
        scrabbleGame.putWord("hola", (5, 5), "v")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("I", 8), 
            Tile("T", 1), 
            Tile("E", 8), 
            Tile("V", 3),
            Tile("R", 1), 
            Tile("P", 1), 
            Tile("L", 1)
        ]
        scrabbleGame.putWord("pero", (6, 2), "h")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("H", 8), 
            Tile("O", 1), 
            Tile("N", 8), 
            Tile("G", 3),
            Tile("U", 1), 
            Tile("S", 1), 
            Tile("A", 1)
        ]
        scrabbleGame.putWord("tocarás", (9, 6), "v")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 8), 
            Tile("C", 1), 
            Tile("E", 8), 
            Tile("U", 3),
            Tile("T", 1), 
            Tile("S", 1), 
            Tile("H", 1)
        ]
        scrabbleGame.putWord("sueca", (15, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("I", 8), 
            Tile("T", 1), 
            Tile("V", 8), 
            Tile("L", 3),
            Tile("Q", 1), 
            Tile("S", 1), 
            Tile("T", 1)
        ]
        scrabbleGame.putWord("suecas", (15, 6), "h")
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("H", 8), 
            Tile("O", 1), 
            Tile("N", 8), 
            Tile("G", 3),
            Tile("O", 1), 
            Tile("L", 1), 
            Tile("X", 1)
        ]
        scrabbleGame.putWord("hongo", (5, 5), "h")
        scrabbleGame.current_player = scrabbleGame.players[2]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("E", 8), 
            Tile("A", 1), 
            Tile("A", 8), 
            Tile("F", 3),
            Tile("I", 1), 
            Tile("E", 1), 
            Tile("I", 1)
        ]
        scrabbleGame.putWord("fiera", (3, 4), "v")
        scrabbleGame.current_player = scrabbleGame.players[3]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("A", 8), 
            Tile("E", 1), 
            Tile("F", 8), 
            Tile("D", 3),
            Tile("Q", 1), 
            Tile("S", 1), 
            Tile("H", 1)
        ]
        scrabbleGame.putWord("fea", (14, 4), "h")
        game.showBoard(scrabbleGame.board)

    def test_validateWordNotFoundInDictionary(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("S", 8), 
            Tile("A", 1), 
            Tile("D", 8), 
            Tile("U", 3),
            Tile("O", 1), 
            Tile("E", 1), 
            Tile("B", 1)
        ]
        with self.assertRaises(Exception):
            scrabbleGame.putWord("duos", (8, 8), "h")
    
    def test_validateWordNotFoundInDictionary(self):
        game = Game()
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("S", 8), 
            Tile("A", 1), 
            Tile("D", 8), 
            Tile("U", 3),
            Tile("O", 1), 
            Tile("E", 1), 
            Tile("B", 1)
        ]
        scrabbleGame.putWord("dúos", (8, 8), "h")
        game.showBoard(scrabbleGame.board)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.next_turn()
        scrabbleGame.current_player.tiles = [
            Tile("G", 8), 
            Tile("R", 1), 
            Tile("U", 8), 
            Tile("A", 3),
            Tile("S", 1), 
            Tile("E", 1), 
            Tile("B", 1)
        ]
        scrabbleGame.putWord("grúas", (7, 9), "v")
        game.showBoard(scrabbleGame.board)

if __name__ == '__main__':
    unittest.main()