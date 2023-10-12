import unittest
from game.scrabble import ScrabbleGame
from game.models import Tile

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
        scrabbleGame.current_player.tiles = [Tile("P", 1), Tile("A", 1), Tile("A", 1), Tile("P", 1), Tile("G", 4), Tile("F", 1), Tile("A", 1)]
        self.assertEqual(scrabbleGame.validateWord("papa", (8, 7), "V"), True)    
    
    def test_validateWordFalse(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[0]
        scrabbleGame.current_player.tiles = [Tile("P", 1), Tile("A", 1), Tile("A", 1), Tile("P", 1), Tile("G", 4), Tile("F", 1), Tile("A", 1)]
        self.assertEqual(scrabbleGame.validateWord("empanada", (15, 7), "H"), False)
    
    def test_lastPlayer(self):
        scrabbleGame = ScrabbleGame(playerCount=3)
        scrabbleGame.current_player = scrabbleGame.players[-1]
        scrabbleGame.next_turn()
        assert scrabbleGame.current_player == scrabbleGame.players[0]
    
    def test_putWords(self):
        scrabbleGame = ScrabbleGame(playerCount=2)
        scrabbleGame.current_player = scrabbleGame.players[1]
        scrabbleGame.current_player.tiles = [Tile("P", 1), Tile("A", 1), Tile("A", 1), Tile("P", 1), Tile("G", 4), Tile("F", 1), Tile("A", 1)]
        scrabbleGame.putWords("papa", (5, 6), "V")

if __name__ == '__main__':
    unittest.main()